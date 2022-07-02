from django.shortcuts import render, get_object_or_404
from django.views import generic, View
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
                "attended": attended,
                "comment_form": CommentForm()
            },
        )
