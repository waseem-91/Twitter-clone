from email.mime import image
from django.db import models
from cloudinary.models import CloudinaryField 

# Create your models here.
class Post(models.Model):
    class Meta(object):
        db_table ='post'

    name = models.CharField(
        'Name', blank=False, null=False, max_length=14, db_index=True, default='Anonymous'
    ) 
    body = models.CharField(
        'Body', blank=False, null=True, max_length=140, db_index=True
    ) 
    created_at = models.DateTimeField(
        'Created DateTime', blank=True, auto_now_add=True
    )
    image = CloudinaryField(
        'image', blank = True, db_index = True 
    )
    likecount = models.IntegerField(
        'like_count', default= 0, blank=True
    )
      