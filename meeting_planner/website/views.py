from datetime import datetime
from django.shortcuts import render
from meetings.models import Meeting, Room
from django.http import HttpResponse


def welcome(request):
    return render(request, "website/welcome.html",
                  {
                      "meetings": Meeting.objects.all()
                  })


def date(request):
    return HttpResponse(f"Now is: {datetime.now()}")


def about(request):
    return HttpResponse(f"Hello, my name is Ciprian and I'm glad to meet you!")
