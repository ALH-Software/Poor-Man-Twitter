from django.db import models

# Create your models here.
class Tweet(models.Model):
    tweet_id = models.AutoField(primary_key=True)
    tweet_name = models.CharField(max_length=25)
    tweet_body = models.CharField(max_length=50)
    tweet_crated_at = models.DateTimeField(auto_now_add=True)
    