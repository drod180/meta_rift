import time

class MetaScoreCalculator:

    def __init__(self, champion):
        self.champion = champion



    def find_rising_trend(self, champion, query_distance):
        if query_distance == time.time() * 1000 - 1209600000:
            return None

        elif abs(champion_win_rate(time.time()) - champion_win_rate(time.time() - query_distance)) > 2 / 100:
            return champion_win_rate(time.time()) - champion_win_rate(time.time() - query_distance) / query_distance

        else:
            trend = find_rising_trend(champion, query_distance - 86400000)

        return trend



        Important Features (for max being 1)
            win rate vs meta picks (.6)
            pick/ban rate difference (.2)
            win rate trend if there is one (.15)
            win rate, if above a certain cutoff (.05)
