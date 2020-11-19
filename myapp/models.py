from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class BlogPost(models.Model):
    post_title = models.CharField(max_length=50)
    post_content = models.CharField(max_length=512)
    post_author = models.ForeignKey(User,on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.post_title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})














    #
    #
    #
    # def get_absolute_url(self):
    #     return redirect('post-detail', kwargs={'pk':self.pk})
