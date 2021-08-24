from django.db import models


class UserTweets(models.Model):
    """
    UserTweets: Model to store user tweets.
    """

    username = models.CharField(max_length=30)
    tweet_message = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "user_tweets"

    def __str__(self):
        return "{}".format(self.username)
