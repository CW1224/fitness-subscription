from django.db import models

# Create your models here.

class Event(models.Model):
    event_title = models.CharField(max_length=50)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    event_on = models.DateTimeField()
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.event_title} added on {self.created_on}'