from django.db import models


class Message(models.Model):

    text = models.TextField()

    def __str__(self):
        return self.text