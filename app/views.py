from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import viewsets

from app.models import Job
from app.serializers import JobSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = []


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
