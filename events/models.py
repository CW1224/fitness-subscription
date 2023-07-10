from django.db import models

# Create your models here.


class Event(models.Model):
    event_title = models.CharField(max_length=50)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    event_on = models.DateTimeField()
    location = models.CharField(max_length=80, null=False, blank=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.event_title} added on {self.created_on}'
