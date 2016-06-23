from ..api_request.riot_api_fetcher import MatchFetcher

def parse_team(teams, teamId):
    if (teams[0]["teamId"] == teamId):
        return "bottom"
    return "top"

def parse_role(lane, role):
    if role == "DUO_CARRY":
        return "marksman"
    if role == "DUO_SUPPORT":
        return "support"
    if lane == "TOP":
        return "top"
    if lane == "MID" or lane == "MIDDLE":
        return "mid"
    if lane == "JUNGLE":
        return "jungle"
    return None

def retrieve(api_key, days_ago = 14, matches_per_region = 10):
    fetcher = MatchFetcher(api_key)
    distance = days_ago * 24 * 60 * 60 * 1000

    results = fetcher.fetch_matches(distance, matches_per_region)

    parsed = []
    for region, matches in results.iteritems():
        for match_id, match in matches.iteritems():
            teams = {
                match["teams"][0]["teamId"]: match["teams"][0],
                match["teams"][1]["teamId"]: match["teams"][1]
            }
            for participant in match['participants']:
                team = teams[participant["teamId"]]
                timeline = participant["timeline"]

                # Parse the role to one of top, mid, jungle, marksman, support
                role = parse_role(timeline["lane"], timeline["role"])
                parsed.append({
                    "match_id": match_id,
                    "champion_id": participant["championId"],
                    "region": region,
                    "winner": team["winner"],
                    "team": parse_team(match["teams"], participant["teamId"]),
                    "role": role,
                    "rank": participant["highestAchievedSeasonTier"]
                })
    print parsed

if __name__ == "__main__":
    from ...config.settings import keys
    retrieve(keys['riot'], 1, 2)
