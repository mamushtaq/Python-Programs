import unittest
from survey import AnonymousSurvey

class TestingAnonymousSurvey(unittest.TestCase):
    """It tests the survey.py"""

    def test_store_single_response(self):
        """Tests if single response is stored in the list"""
        question = "Which language did you learn to speak first"
        mysurvey = AnonymousSurvey(question)
        mysurvey.store_response('English')

        self.assertIn('English', mysurvey.response)

    def test_store_three_responses(self):
        """Tests if three responses are stored in the list"""
        question = "Which language did you learn to speak first"
        mysurvey = AnonymousSurvey(question)
        responses = ['Urdu', 'Spanish','Japanese','German']
        for response in responses:
            mysurvey.store_response(response)
        for response in responses:
            self.assertIn(response, mysurvey.response)


unittest.main()