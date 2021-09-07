  
from rest_framework import serializers
from .models import App

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ('id','title','body','author', 'created_at', 'updated_at')