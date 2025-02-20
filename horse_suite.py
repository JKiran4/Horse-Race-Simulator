import unittest
from horse_race_simulator_test.test_horse_stats import TestHorse
from horse_race_simulator_test.test_betting import TestUser
from horse_race_simulator_test.test_track_data import TestTrack
from horse_race_simulator_test.test_race_simulator import TestRaceSimulation
from horse_race_simulator_test.test_race_details import TestRace
from horse_race_simulator_test.test_race_results import TestRaceResults

def horse_suite(): # temporary name, please feel free to change if you have a preference
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(TestHorse('test_horse_creation'))
    suite.addTest(TestHorse('test_update_horse_stats'))
    suite.addTest(TestUser('test_balance_horse_id'))
    suite.addTest(TestUser('test_take_bet'))
    suite.addTest(TestTrack('test_create_track'))
    suite.addTest(TestTrack('test_weather_factor'))
    suite.addTest(TestTrack('test_get_track_info'))
    suite.addTest(TestRaceSimulation('test_start_race'))
    suite.addTest(TestRaceSimulation('test_get_times'))
    suite.addTest(TestRaceSimulation('test_get_winning_horse_id'))
    suite.addTest(TestRace('test_constructor'))
    suite.addTest(TestRace('test_set_delayed_date'))
    suite.addTest(TestRace('test_set_date'))
    suite.addTest(TestRace('test_get_race_info'))
    suite.addTest(TestRaceResults('test_constructor'))
    suite.addTest(TestRaceResults('test_get_horse_position'))
    suite.addTest(TestRaceResults('test_display_options_and_getters'))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))

horse_suite()
