import unittest
import time
from riot_api_fetcher import *

class TestRiotApi(unittest.TestCase):

    def setUp(self):
        self.test_thread = RequestThread("NA", "NA", MatchFetcher.SUMMONERS_BY_REGION["NA"], int((time.time() * 1000) - 1209600000), 10)
        self.test_fetcher = MatchFetcher()

class BasicApiTest(TestRiotApi):
    def test_thread_init_region(self):
        self.assertEqual(self.test_thread.region, "NA")

    def test_thread_init_name(self):
        self.assertEqual(self.test_thread.name, "NA")

    def test_thread_init_starting_summoner(self):
        self.assertEqual(self.test_thread.starting_summoner, MatchFetcher.SUMMONERS_BY_REGION["NA"])

    def test_thread_init_query_distance(self):
        self.assertEqual(self.test_thread.query_distance, int((time.time() * 1000) - 1209600000))

    def test_thread_init_match_request_number(self):
        self.assertEqual(self.test_thread.matches_requested, 10)

class BasicFetcherTest(TestRiotApi):
    def test_fetcher_init(self):
        self.assertEqual(self.test_fetcher.total_matches, {})

    def test_fetcher_run(self):
        results = self.test_fetcher.fetch_matches(int((time.time() * 1000) - 1209600000), 1)
        self.assertEqual(len(results), 11)

        

if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(BasicApiTest)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(BasicFetcherTest)
    alltests = unittest.TestSuite([suite1, suite2])
    unittest.TextTestRunner(verbosity=2).run(alltests)
