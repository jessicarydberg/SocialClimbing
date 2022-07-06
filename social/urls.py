from . import views
from django.urls import path


urlpatterns = [
    path('', views.EventList.as_view(), name='home'),
    path('add_event/', views.AddEvent.as_view(), name='add_event'),
    path('<slug:slug>/', views.EventDetail.as_view(), name='event_detail'),
    path('attend/<slug:slug>/', views.PostAttend.as_view(), name='event_attendees'),
]
