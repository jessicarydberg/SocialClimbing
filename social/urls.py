from . import views
from django.urls import path


urlpatterns = [
    path('', views.EventList.as_view(), name='home'),
    path('add_event/', views.AddEvent.as_view(), name='add_event'),
    path('delete_event/<slug:slug>', views.DeleteEvent.as_view(), name='delete_event'),
    path('event_edit/<slug:slug>', views.EditEvent.as_view(), name='event_edit'),
    path('<slug:slug>/', views.EventDetail.as_view(), name='event_detail'),
    path('attend/<slug:slug>/', views.PostAttend.as_view(), name='event_attendees'),
]
