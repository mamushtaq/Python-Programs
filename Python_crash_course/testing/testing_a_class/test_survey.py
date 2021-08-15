import unittest
from survey import AnonymousSurvey

class TestingAnonymousSurvey(unittest.TestCase):
    """It tests the survey.py"""

    def setUp(self):
        """Creates sets of responses to be tested"""
        question = "Which language did you learn to speak first"
        self.mysurvey = AnonymousSurvey(question)
        self.responses = ['English','Urdu', 'Spanish','Japanese','German']

    def test_store_single_response(self):
        """Tests if single response is stored in the list"""
        
        self.mysurvey.store_response(self.responses[0])

        self.assertIn(self.responses[0], self.mysurvey.response)

    def test_store_three_responses(self):
        """Tests if three responses are stored in the list"""
        for response in self.responses[1:4]:
            self.mysurvey.store_response(response)
        for response in self.responses[1:4]:
            self.assertIn(response, self.mysurvey.response)


unittest.main()