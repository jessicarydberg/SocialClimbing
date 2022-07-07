from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView, DeleteView
from django.utils.text import slugify
from .models import Event
from .forms import CommentForm, EventForm


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(status=1).order_by("date")
    template_name = "index.html"
    paginate_by = 8


class EventDetail(View):

    def get(self, request, slug):
        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        comments = event.comments.order_by('created_on')
        attended = False
        if event.attendees.filter(id=self.request.user.id).exists():
            attended = True

        return render(
            request,
            "event.html",
            {
                "event": event,
                "comments": comments,
                "commented": False,
                "attended": attended,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug):
        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        comments = event.comments.order_by('created_on')
        attended = False
        if event.attendees.filter(id=self.request.user.id).exists():
            attended = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.event = event
            comment.save()
        else:
            comment_form = CommentForm()
        return render(
            request,
            "event.html",
            {
                "event": event,
                "comments": comments,
                "commented": True,
                "attended": attended,
                "comment_form": CommentForm()
            },
        )



class PostAttend(View):

    def post(self, request, slug):
        event = get_object_or_404(Event, slug=slug)

        if event.attendees.filter(id=request.user.id).exists():
            event.attendees.remove(request.user)
        else:
            event.attendees.add(request.user)

        return HttpResponseRedirect(reverse('event_detail', args=[slug]))


class AddEvent(View):

    def get(self, request):
        event_form = EventForm()
        return render(request, 'add_event.html', {
            'form': event_form
            })

    def post(self, request):
        submitted = False
        event_form = EventForm(request.POST, request.FILES)
        if event_form.is_valid():
            event_form.instance.author = User.objects.get(username=request.user.username)
            event_form.instance.slug = slugify(event_form.instance.title)
            event_form.instance.status = 1
            event_form.save()
            submitted = True

        return render(request, 'add_event.html', {
            'form': event_form, 'submitted': submitted
            })


class DeleteEvent(DeleteView):

    model = Event
    template_name = 'delete_event.html'
    deleted = True
    success_url = '/'


class EditEvent(UpdateView):
    
    model = Event
    form_class = EventForm
    template_name_suffix = '_edit_form'
    template_name = 'event_edit_form.html'
    edited = True
    success_url = '/'
