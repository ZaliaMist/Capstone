# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from authuser.models import Profile


class Community(models.Model):
    comm_name = models.CharField(max_length=60)
    comm_about = models.TextField(max_length=2000, default="Welcome to the Community")
    comm_creator = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    created_on = models.DateField(auto_now_add=True)
    comm_url = models.URLField(max_length=200, blank=True)
    # comm_members = models.ManyToManyField(Profile, blank=True)

    def __str__(self):
        return self.comm_name
        # return str(self.comm_name)

class Post(models.Model):
    post_name = models.CharField(max_length=60)
    post_text = models.TextField()
    post_creator = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
    created_on = models.DateField(auto_now_add=True)
    post_on_comm = models.ForeignKey(Community, on_delete=models.CASCADE)

    credit = models.IntegerField(default=0)

    def vote_total(self):
        return self.credit

    def __str__(self):
        return self.post_name
        
    

class Comment(models.Model):
    on_post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    comment_text = models.TextField()
    credit = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text
        

