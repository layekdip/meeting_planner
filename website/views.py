from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from meetings.models import Meeting


def welcome(request):
    # return HttpResponse("Welcome Dip!!!")
    return render(request, "website/welcome.html",
                  {"message": "Hi Dip, wab page is working!!!", "meetings": Meeting.objects.all()})


def date(request):
    return HttpResponse("Current time : {}".format(str(datetime.now())))


def about(request):
    return HttpResponse("Welcome Dip - lets have magic!!!")
