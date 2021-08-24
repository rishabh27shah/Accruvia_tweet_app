from django.urls import path
from apis import views

urlpatterns = [
    path("tweet/", views.TweetView.as_view(), name="user_tweet"),
]
