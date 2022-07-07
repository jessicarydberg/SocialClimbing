from django.test import TestCase
from .forms import CommentForm, EventForm


class TestEventForm(TestCase):

    def test_event_title_is_required(self):
        form = EventForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_event_date_is_required(self):
        form = EventForm({'date': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('date', form.errors.keys())
        self.assertEqual(form.errors['date'][0], 'This field is required.')

    def test_event_location_is_required(self):
        form = EventForm({'location': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('location', form.errors.keys())
        self.assertEqual(form.errors['location'][0], 'This field is required.')

    def test_event_content_is_required(self):
        form = EventForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')
    
    def test_image_field_is_not_required(self):
        form = EventForm({
            'title': 'Climbing',
            'date': '2022-03-07 18:00:00',
            'location': 'home',
            'content': 'whatever'
            })
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = EventForm()
        self.assertEqual(form.Meta.fields, ('title', 'date', 'location', 'content', 'image'))


class TestCommentForm(TestCase):

    def test_comment_body_is_required(self):
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('body',))
