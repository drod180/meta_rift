import time

class MetaScoreCalculator:

    def __init__(self, champion):
        self.champion = champion



    def find_rising_trend(self, champion, query_distance):
        if query_distance == time.time() * 1000 - 1209600000: #If it's already checking a full two weeks ago, don't check further. There is no trend
            return None

        elif abs(champion_win_rate(time.time()) - champion_win_rate(time.time() - query_distance)) > 2 / 100: #2% or more could be a trend
            return [champion_win_rate(time.time()) - champion_win_rate(time.time() - query_distance), query_distance] #weight it with how fast it happened

        else:
            return trend = find_rising_trend(champion, query_distance - 86400000) #If nothing was found and it's still within two weeks, check one day ago.


    def is_meta(self, champion):
        if champion.pick_rate + (champion.ban_rate / 2) > 1 / 10:
            return True
        else:
            return False


#         Important Features (for max being 1)
#             win rate vs meta picks (.45)
#             win rate trend if there is one (.25)
#             pick/ban rate difference (.2)
#             win rate, if above a certain cutoff (.1)
#
#
# 53% win rate vs meta picks
#
# difference of pick/ban is 4%
#
# trend is 2% up over 3 days
#
# win rate is 56%
#
# difference from 50% * 10, baseline is 100. Win rate difference below 40% should seriously hurt a metascore even if there's a rising win rate trend.
#
# rising win rate trends gain force for shorter amounts of time. the number being multiplied by .25 will be increased by the inverse of the time.
#
# In this case, 120 * (1 + (1/3)), or 160. Were it over 4 days, it would be 150. Over 2 days, 180. Over 10 days, 132.
#
# if win rate is above 53%, take this part into account. Otherwise, it will be counted simply as .1 * 100.
#
# .45 * 130
#
# .25 * 120 * (1 + (1 / 3))
#
# .2 * 140
#
# .1 * 160
