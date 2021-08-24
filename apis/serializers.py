from rest_framework import serializers
from apis.models import UserTweets


class TweetPostSerializer(serializers.ModelSerializer):
    """
    TweetPostSerializer: Serializer for validate name and tweet fields and create tweets.
    """

    def create(self, data):
        instance = super().create(data)
        return instance

    class Meta:
        model = UserTweets
        exclude = ("created_at",)


class TweetGetSerializer(serializers.ModelSerializer):
    """
    TweetGetSerializer: Serializer to fetch all tweets.
    """
    class Meta:
        model = UserTweets
        fields = "__all__"
