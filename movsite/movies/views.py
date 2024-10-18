from .serializers import MovieSerializer
from .models import MovieData
from rest_framework import viewsets


# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer


class ComedyViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genre="Comedy")
    serializer_class = MovieSerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genre="Action")
    serializer_class = MovieSerializer
