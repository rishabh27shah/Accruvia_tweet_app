from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import UserTweets
from api.serializers import TweetGetSerializer


class APITest(APITestCase):
    """
        APITest : for testing API endpoints
    """

    def test_tweet_post(self):
        """
        test_tweet_post : test /tweet/ endpoint for post request
        """
        url = reverse('tweet')
        data = {'name': 'Test Name', 'tweet': 'Test Tweet Message'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_tweet_get(self):
        """
        test_tweet_get : test /tweet/ endpoint for get request
        """
        url = reverse('tweet')
        response = self.client.get(url)
        tweets = UserTweets.objects.all()
        serialised_tweets = TweetGetSerializer(tweets, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serialised_tweets.data)