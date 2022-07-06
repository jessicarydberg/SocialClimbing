from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Event
from .forms import CommentForm


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(status=1).order_by("date")
    template_name = "index.html"
    paginate_by = 8


class EventDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        comments = event.comments.filter(approved=True).order_by('created_on')
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

    def post(self, request, slug, *args, **kwargs):
        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        comments = event.comments.filter(approved=True).order_by('created_on')
        attended = False
        if event.attendees.filter(id=self.request.user.id).exists():
            attended = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
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
        return render(request, 'add_event.html')
