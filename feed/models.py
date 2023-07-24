from django.db import models
from sorl.thumbnail import ImageField

class Post(models.Model):
    text = models.CharField(max_length=40, blank=True, null=False)
    image = ImageField()
    description = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.text

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=40)
    country = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']
    def __str__(self):
        return "Comment {} by {} ".format(self.body,self.name)


    