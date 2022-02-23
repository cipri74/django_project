from django.shortcuts import render, get_object_or_404, redirect
from meetings.models import Meeting, Room
from django.forms import modelform_factory


def detail(request, id):

    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {
        "meeting": meeting
    })


def rooms(request):
    return render(request, "meetings/rooms.html", {
        "rooms": Room.objects.all()
    })


def room(request, id):

    _room = get_object_or_404(Room, pk=id)
    return render(request, "meetings/room.html", {
        "room": _room
    })


MeetingForm = modelform_factory(Meeting, exclude=[])


def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    form = MeetingForm()
    return render(request, "meetings/new.html",
                  {"form": form})
