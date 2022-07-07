from django.test import TestCase
from .models import Event
from django.contrib.auth import get_user_model


class TestViews(TestCase):

    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_event_detail_page(self):
        event = Event.objects.create(
            title='Climbing',
            date='2022-03-07 18:00:00',
            location='home',
            content='whatever'
        )
        response = self.client.get(f'/{event.slug}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'event.html')

    def test_get_add_event_page(self):
        
        event = Event.objects.create(
            title='Climbing',
            date='2022-03-07 18:00:00',
            location='home',
            content='whatever'
        )
        response = self.client.get(f'/event_edit/{event.slug}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'event_edit_form')
    
    # def test_add_comment(self):

    # def test_toggle_attend(self):

    # def test_add_event(self):
    
    # def test_edit_event(self):

    # def test_delete_event(self):
