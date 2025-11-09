from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class categories(models.Model):
    category=models.CharField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.category
    
status_choices=[
    ('published','published'),
    ('draft','draft')
]

class articles(models.Model):
    title=models.CharField(max_length=1000)
    slug=models.SlugField(max_length=500)
    image=models.ImageField(upload_to='media')
    category=models.ForeignKey(categories,on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    short_description=models.TextField()
    detail_description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    status=models.CharField(choices=status_choices)
    is_trending=models.BooleanField(default=False)