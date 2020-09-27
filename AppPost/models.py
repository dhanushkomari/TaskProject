from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=100,blank=False)
    #slug = models.SlugField(max_length=50,unique=True, blank=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'post'
        verbose_name_plural = 'posts'
    
    def __str__(self):
        return '{}'.format(self.title)