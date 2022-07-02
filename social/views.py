from django.shortcuts import render
from django.db import models
from django.views import generic
from .models import Event


class EventList(generic.ListView):
    today = models.DateTimeField(auto_now=True)
    if Event.date > today:
        model = Event
        queryset = Event.objects.filter(status=1).order_by('date')
        template_name = 'index.html'
        paginate_by = 6

