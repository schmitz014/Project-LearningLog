from django.db import models

class Topic(models.Model):
    """An topic that is about what user is learning"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns a string representation of model"""
        return self.text