import requests
import json
import time
import threading
from collections import deque
import os

class MatchFetcher:


    RANKED_PARAM = "?rankedQueues=TEAM_BUILDER_DRAFT_RANKED_5x5&beginTime="

    # These are all of the LoL regions. Deleting from this list and the corresponding
    # SUMMONERS_BY_REGION dictionary will reduce the number of servers being queried.
    # Current, the furthest regions are commented out as their response times are
    # considerably longer. For a full query, add them back in.
    REGIONS = {"BR": "br", "EUNE": "eune", "EUW": "euw", "JP": "jp", "KR": "kr",
    "LAN": "lan", "LAS": "las", "NA": "na", "OCE": "oce", "RU": "ru", "TR": "tr"}

    # Using these summoners to start our queries. They play a lot of ranked Solo Queue.
    #  The summoners for each region are either pros or high-ranked players, as they
    #  tend to be quite active.
    SUMMONERS_BY_REGION = {"BR": deque(["488302", "522434", "410503", "9480188"]), \
        "EUNE": deque(["22536759", "36822759", "35943882", "38723598"]), \
        "EUW": deque(["20717177", "22659867", "25532701", "29776827"]), \
        "JP": deque(["6160658", "6170777", "6310312", "6181771"]), \
        "KR": deque(["4460427", "25291795", "7895259", "5310176"]), \
        "LAN": deque(["135857", "139360", "53010", "104671"]), \
        "LAS": deque(["135412", "185763", "167310", "110751"]), \
        "NA": deque(["19134540", "72749304", "51405", "65009177"]), \
        "OCE": deque(["346050", "293100", "432291", "484696"]), \
        "RU": deque(["4780139", "5420417", "312366", "483422"]), \
        "TR": deque(["2411323", "2024938", "2592438", "1883115"])}



    def __init__(self):

        self.total_matches = {}
        self.api_key = "api_key=" + os.environ['api_key'] #Be sure to set the API_Key as an environment variable before creating a MatchFetcher!

    def fetch_matches(self, query_distance, match_number_per_region):
        total_query_distance = int((time.time() * 1000) - query_distance)

        threads = []

        regions = MatchFetcher.REGIONS.keys()
        for region in regions:
            threads.append(RequestThread(region, region, self.SUMMONERS_BY_REGION[region], total_query_distance, match_number_per_region, self.api_key))
            self.total_matches[region] = {}
        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()
            self.total_matches[thread.region].update(thread.total_matches)

        return self.total_matches



class RequestThread(threading.Thread):
    def __init__(self, region, threadName, starting_summoners, query_distance, matches_requested, api_key):
        threading.Thread.__init__(self)
        self.api_key = api_key
        self.region = region
        self.name = threadName
        self.request_tracker = deque([])
        self.big_request_tracker = deque([])
        self.query_distance = query_distance
        self.starting_summoners = starting_summoners
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
        match_data = requests.get(("{0}" + "{1}" + "?" + "{2}").format(regional_url, match_id, self.api_key))
        print match_data.status_code
        if match_data.status_code == 200:
            match_details = json.loads(match_data.text)
            self.lockout_counter = 0
            self.total_matches[match_id] = match_details
            for summoner in match_details["participantIdentities"]:
                summoner_queue.append(summoner["player"]["summonerId"])

            if len(self.total_matches) == self.matches_requested:
                return True

        elif match_data.status_code == 429: #break if getting rate limited. Don't want to get blacklisted!
            if self.check_for_lockout(match_data) == False:
                return True

        elif match_data.status_code == 403 or match_data.status_code == 404:
            return True #Break if forbidden. This could be blacklisting or an api key error. Also break on bad input

        elif match_data.status_code == 500 or match_data.status_code == 503:
            self.check_for_lockout(match_data)
            return self.extract_match_data(match_id, summoner_queue)

        return False

    def fetch_matches(self, summoner_id = "none"):
        if summoner_id == "none":
            summoner_id = self.starting_summoners[0]

        regional_url = self.build_regional_url("Matchlist")
        request_url = ("{0}" + "{1}" + "{2}" + "{3}" + "&" + "{4}").format(regional_url, summoner_id, MatchFetcher.RANKED_PARAM, self.query_distance, self.api_key)
        self.track_request()
        matches = requests.get(request_url)
        print matches.status_code
        if matches.status_code == 200:
            self.lockout_counter = 0
            self.summoners[summoner_id] = True
            return json.loads(matches.text)["matches"]


        elif matches.status_code == 429: #break if getting rate limited. Don't want to get blacklisted!
            if self.check_for_lockout(matches) == False:
                return False

        elif matches.status_code == 403 or matches.status_code == 404:
            if summoner_id == self.starting_summoners[0]:
                return None
            else:
                return False

        elif matches.status_code == 500 or matches.status_code == 503:
            self.halt_requests()
            self.check_for_lockout(matches)
            return self.fetch_matches(summoner_id)



    def check_for_lockout(self, response):
        if response.status_code == 429:
            print response.headers['X-Rate-Limit-Count']
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
        if len(match_queue) == 0:
            return
        while finished == False:
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
                                if not match["matchId"] in self.total_matches and match["region"] == self.region:
                                    match_queue.append(match["matchId"])

    def set_up_match_queue(self):
        match_queue = deque([])
        initial_matches = None
        counter = 0
        while initial_matches is None:
            self.halt_requests()
            initial_matches = self.fetch_matches()
            if initial_matches == False:
                return match_queue

            self.starting_summoners.append(self.starting_summoners.popleft)
            counter += 1
            if counter == 4:
                print "Tried all summoners"
                return match_queue
        for match in initial_matches:
            if match["region"] == self.region: #This makes sure that if a player transfers, we don't append matches on the wrong servers.
                match_queue.append(match["matchId"])

        return match_queue




# For testing a single thread
# a = RequestThread("NA", "NA", MatchFetcher.SUMMONERS_BY_REGION["NA"], 1464039831476, 10, API_KEY)
# a.start()
# a.join()
#
# For testing the fetcher class
# a = MatchFetcher()
# results = a.fetch_matches(1209600000, 10) # two weeks ago in milliseconds, finding 10 matches per region
# for region in results.keys():
#     print ("Matches for {0}:").format(region)
#     print results[region].keys()
