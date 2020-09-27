from django.db import models
from django.utils import timezone

class Comic(models.Model):
    title = models.CharField(max_length=100)
    aouthor = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Character(models.Model):
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    profile = models.TextField()
    # image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class Voting(models.Model):
    name = models.ForeignKey(Character, on_delete=models.CASCADE)
    point = models.IntegerField()
    created_at = models.DateTimeField(verbose_name='投票日時', default=timezone.now, editable=False)