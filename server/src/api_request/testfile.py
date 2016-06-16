import unittest
import time
from riot_api_fetcher import *

#To run the tests, put your API Key in the places where they are commented out
class TestRiotApi(unittest.TestCase):

    def setUp(self):
        self.test_thread = RequestThread("NA", "NA", MatchFetcher.SUMMONERS_BY_REGION["NA"], int((time.time() * 1000) - 1209600000), 10, #API Key)
        self.test_fetcher = MatchFetcher(#API Key)

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

    def test_fetcher_bad_input(self):
        bad_thread = RequestThread("NA", "NA", MatchFetcher.SUMMONERS_BY_REGION["NA"] + "00", int((time.time() * 1000) - 1209600000), 1, #API Key)
        bad_thread.start()
        bad_thread.join()
        results = bad_thread.total_matches
        self.assertEqual(len(results), 0)



if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(BasicApiTest)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(BasicFetcherTest)
    alltests = unittest.TestSuite([suite1, suite2])
    unittest.TextTestRunner(verbosity=2).run(alltests)
