import requests
import json
import time
import threading
from collections import deque

class MatchFetcher:


    RANKED_PARAM = "?rankedQueues=TEAM_BUILDER_DRAFT_RANKED_5x5&beginTime="
    API_KEY = "" #Put your API key here

    # These are all of the LoL regions. Deleting from this list and the corresponding
    # SUMMONERS_BY_REGION dictionary will reduce the number of servers being queried.
    # Current, the furthest regions are commented out as their response times are
    # considerably longer. For a full query, add them back in.
    REGIONS = {"BR": "br", "EUNE": "eune", "EUW": "euw", "JP": "jp", "KR": "kr",
    "LAN": "lan", "LAS": "las", "NA": "na", "OCE": "oce", "RU": "ru", "TR": "tr"}

    # Using these summoners to start our queries. They play a lot of ranked Solo Queue.
    #  The summoners for each region are as follows: RED Eryon for BR, HitooN for EUNE,
    #  FNC Rekkles for EUW, Rainbrain for JP, Hideonbush (Faker) for KR, C3 Oni for LAN,
    #  Rakyl y Ken Y for LAS, Voyboy for NA, LGC Chuchuz for OCE, IT'S ONLY A GAME for RU,
    #  and Yuki for TR.
    SUMMONERS_BY_REGION = {"BR": "488302", "EUNE": "22536759", \
        "EUW": "20717177", "JP": "6160658", "KR": "4460427",  "LAN": "135857", \
        "LAS": "135412", "NA": "19134540", "OCE": "293100", "RU": "4780139", \
        "TR": "2130246"}



    def __init__(self):
        self.total_matches = {}

    def fetch_matches(self, query_distance, match_number_per_region):
        total_query_distance = int((time.time() * 1000) - query_distance)

        threads = []

        regions = MatchFetcher.REGIONS.keys()
        for region in regions:
            threads.append(RequestThread(region, region, self.SUMMONERS_BY_REGION[region], total_query_distance, match_number_per_region))
            self.total_matches[region] = {}
        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()
            self.total_matches[thread.region].update(thread.total_matches)

        return self.total_matches


exitFlag = 0

class RequestThread(threading.Thread):
    def __init__(self, region, threadName, starting_summoner, query_distance, matches_requested):
        threading.Thread.__init__(self)
        self.region = region
        self.name = threadName
        self.request_tracker = deque([])
        self.big_request_tracker = deque([])
        self.query_distance = query_distance
        self.starting_summoner = starting_summoner
        self.total_matches = {}
        self.lockout_counter = 0
        self.summoners = {}
        self.matches_requested = matches_requested


    def run(self):
        print ("Starting fetcher for " + "{0}" + " region \n").format(self.region)
        self.fetcher()
        print ("Exiting fetcher for " + "{0}" + " region \n").format(self.region)

    def build_regional_url(self, type):
        if type == "Matchlist":
            extension = "/v2.2/matchlist/by-summoner/"
        elif type == "Match":
            extension = "/v2.2/match/"
        elif type == "Summoner":
            extension = "v1.4/summoner/"

        return ("https://" + "{0}" + ".api.pvp.net/api/lol/" + "{0}" +  "{1}").format(MatchFetcher.REGIONS[self.region], extension)

    def track_request(self):
        self.request_tracker.append(time.time())
        self.big_request_tracker.append(time.time())

    def halt_requests(self):
        small_api_limit = {"requests": 9, "time": 10} # These numbers are based on your API key
        big_api_limit = {"requests": 499, "time": 600} # These numbers are also based on your API key
        self.check_helper(self.request_tracker, small_api_limit)
        self.check_helper(self.big_request_tracker, big_api_limit)

    def check_helper(self, tracker, api_limit):
        while len(tracker) > 0 and (time.time() - tracker[0]) > api_limit["time"]:
            tracker.popleft()

        buffer_time = 0.25
        if len(tracker) >= api_limit["requests"]:
            time.sleep(api_limit["time"] + buffer_time - (time.time() - tracker[0]))
            tracker.popleft()


    def extract_match_data(self, match_id, summoner_queue):
        regional_url = self.build_regional_url("Match")
        self.track_request()
        match_data = requests.get(("{0}" + "{1}" + "?" + "{2}").format(regional_url, match_id, MatchFetcher.API_KEY))
        print match_data.status_code
        if match_data.status_code == 200:
            match_details = json.loads(match_data.text)
            self.total_matches[match_id] = match_details
            for summoner in match_details["participantIdentities"]:
                summoner_queue.append(summoner["player"]["summonerId"])

            if len(self.total_matches) == self.matches_requested:
                return True

        elif match_data.status_code == 429: #break if getting rate limited. Don't want to get blacklisted!
            if self.check_for_lockout(match_data) == False:
                return True

        return False

    def fetch_matches(self, summoner_id = "none"):
        if summoner_id == "none":
            summoner_id = self.starting_summoner

            regional_url = self.build_regional_url("Matchlist")
            request_url = ("{0}" + "{1}" + "{2}" + "{3}" + "&" + "{4}").format(regional_url, summoner_id, MatchFetcher.RANKED_PARAM, self.query_distance, MatchFetcher.API_KEY)
            self.track_request()
            matches = requests.get(request_url)
            print matches.status_code
            if matches.status_code == 200:
                self.summoners[summoner_id] = True
                return json.loads(matches.text)["matches"]

            elif matches.status_code == 429: #break if getting rate limited. Don't want to get blacklisted!
                if self.check_for_lockout(matches) == False:
                    return False
                else: self.fetch_matches(summoner_id)

    def check_for_lockout(self, response):
        print response.headers
        if 'X-Rate-Limit-Type' in response.headers: # check to make sure it's the program exceeding the limit, not something internal
            print "Rate limit exceeded"
            return False

        else: # If it IS internal, give it a sec. Jeez.
            if self.lockout_counter < 4:
                self.lockout_counter += 1

            lockout_chart = {"1": 1, "2": 15, "3": 30, "4": 60}
            time.sleep(lockout_chart["{0}".format(self.lockout_counter)])

        return True


    def fetcher(self):
        finished = False
        match_queue = self.set_up_match_queue()
        summoner_queue = deque([])
        while finished == False:
            if exitFlag:
                self.name.exit()
            self.halt_requests()
            if len(match_queue) > 0:
                match_id = match_queue.popleft()
                if not match_id in self.total_matches:
                    finished = self.extract_match_data(match_id, summoner_queue)

            else: #only start finding more matches if there are none available.
                if len(summoner_queue) > 0:
                    summoner_id = summoner_queue.popleft()
                    if not summoner_id in self.summoners:
                        matches = self.fetch_matches(summoner_id)
                        if matches == False: #returns out if rate limited
                            finished = True
                        else:
                            for match in matches:
                                if not match["matchId"] in self.total_matches:
                                    match_queue.append(match["matchId"])

    def set_up_match_queue(self):
        match_queue = deque([])
        initial_matches = self.fetch_matches()
        if initial_matches == False:
            return match_queue
        while initial_matches is None:
            initial_matches = self.fetch_matches()
        for match in initial_matches:
            match_queue.append(match["matchId"])

        return match_queue




# For testing a single thread
# a = RequestThread("NA", "NA", MatchFetcher.SUMMONERS_BY_REGION["NA"] )
# a.start()
# a.join()

# For testing the fetcher class
# a = MatchFetcher()
# results = a.fetch_matches(1209600000, 10) # two weeks ago in milliseconds, finding 10 matches per region
# for region in results.keys():
#     print ("Matches for {0}:").format(region)
#     print results[region].keys()
