from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from apis.models import UserTweets
from apis.constant import MESSAGE, CREATE_TWEET
from apis.serializers import TweetGetSerializer, TweetPostSerializer


class TweetView(APIView):
    """
    Create and featch all tweets.
    """

    def post(self, request):
        serializer = TweetPostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response_data = {MESSAGE: CREATE_TWEET}
            return Response(response_data, status.HTTP_201_CREATED)

    def get(self, request):
        tweets = UserTweets.objects.order_by("-created_at", "username")
        serializer = TweetGetSerializer(tweets, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
