from rest_framework import viewsets, status
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework.views import APIView
from post import models
from .serializers import ProfileSerializer, PostSerializer


class CreateProfile(ListCreateAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = ProfileSerializer


class Editprofile(RetrieveUpdateDestroyAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileViewSet(ListAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = ProfileSerializer


class CreatePost(ListCreateAPIView):
    queryset = models.Post.objects.all()
    serializer_class = PostSerializer


class EditPost(RetrieveUpdateDestroyAPIView):
    queryset = models.Post.objects.all()
    serializer_class = PostSerializer


class AllPost(ListAPIView):
    queryset = models.Post.objects.all()
    serializer_class = PostSerializer