from django.db import models


class Message(models.Model):

    time = models.DateTimeField(auto_now_add=True, blank=True)
    text = models.TextField()

    def __str__(self):
        return self.text