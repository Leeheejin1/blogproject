from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    def summary(self):
        return self.content

class Portfolio(models.Model):
    title = models.CharField(max_length = 255)
    image = models.ImageField(upload_to = 'image/')
    description = models.CharField(max_length=500)
    def __str__(self):
        return self.title