  
from rest_framework import generics
from .models import App
from .serializers import AppSerializer
from .permissions import IsOwnerOrReadOnly

# Create your views here.

class AppList(generics.ListCreateAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer

class AppDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    permission_classes = (IsOwnerOrReadOnly,)