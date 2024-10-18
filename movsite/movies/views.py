from .serializers import MovieSerializer
from .models import MovieData
from rest_framework import viewsets


# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer
