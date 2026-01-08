from django.shortcuts import render
from rest_framework import generics
from .models import Organizations,Subscriptions,Branch
from .serializers import OrganizationsSerializer,SubscriptionsSerializer,BranchSerializer
# Create your views here.

class OrganizationsListCreate(generics.ListCreateAPIView):
    queryset = Organizations.objects.all()
    serializer_class = OrganizationsSerializer


class OrganizationsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organizations.objects.all()
    serializer_class = OrganizationsSerializer


class SubscriptionsListCreate(generics.ListCreateAPIView):
    queryset = Subscriptions.objects.all()
    serializer_class = SubscriptionsSerializer


class SubscriptionsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscriptions.objects.all()
    serializer_class = SubscriptionsSerializer


class BranchListCreate(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class BranchRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


