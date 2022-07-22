import datetime
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    PRDImage = models.ImageField(upload_to="media", blank=True, null=True, verbose_name='صور المنتج')

    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=158)
    lname = models.CharField(max_length=158 , null=True)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name   