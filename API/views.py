from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework import viewsets
from API .models import Company
from API .serializers import CompanySerilizers
# Create your views here.

def index(request):
    friends = [
        "jagu","foodie","ishu",
    ]
    return JsonResponse(friends,safe=False)


class CompanyViewSet(viewsets.ModelViewSet):
    quesryset=Company.objects.all()
    serializer_class=CompanySerilizers