from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    text = models.TextField(max_length=500)
    publisher = models.CharField(max_length=100)
    bookimage = models.ImageField(upload_to='images/',default='images/none.jpg')

    def __str__(self):
        return self.title