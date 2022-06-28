from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Event(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
    date = models.DateTimeField('Event Date')
    content = models.TextField()
    location = models.CharField(max_length=120)
    attendees = models.CharField(User, related_name='event_attendees', blank=True)
    image = models.CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.title

    def number_of_attendees(self):
        return self.attendees.count()
