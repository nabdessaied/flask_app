import unittest
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer


class TestSentimentAnalyzer(unittest.TestCase):
    def test_positive_sentiment_analyzer (self):
        actual_response = sentiment_analyzer("I love this new technology")
        expected_response_sent = 'SENT_POSITIVE'
        assert expected_response_sent == actual_response['label']

    def test_negative_sentiment_analyzer (self):
        actual_response = sentiment_analyzer("I hate this new technology")
        expected_response_sent = 'SENT_NEGATIVE'
        assert expected_response_sent == actual_response['label']
    
    def test_neutral_sentiment_analyzer (self):
        actual_response = sentiment_analyzer("I use this new technology")
        expected_response_sent =  'SENT_NEUTRAL'
        assert expected_response_sent == actual_response['label']

unittest.main()
