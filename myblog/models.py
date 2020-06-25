from django.db import models

# Create your models here.
# 1) User Credentials model - extend Django user
from django.contrib.auth.models import User
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=30, blank=True)
    dob = models.DateField(null=True, blank=True) #date of birth
    
# 2) Post model - where I can save it, distinguish who is a owner of this post
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    reporter = models.ForeignKey(Profile, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='.\pic', blank=True, null=True)

# 3) Model for Facebook and Insta - likes, comments (real time) for real time I will need just Ids
class Comment(models.Model):
    author = models.CharField(max_length=55)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    NETWORK_TYPES = (
            ('Inst', 'Instagram'),
            ('FB', 'FACEBOOK'),
        )
    network_type = models.CharField(max_length=4, choices=NETWORK_TYPES)


class Like(models.Model):
     post = models.ForeignKey(Post, on_delete=models.CASCADE)
     author = models.CharField(max_length=55)
