from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo  # Corrected the assignment operator here
        fields = ('id', 'title', 'description', 'completed')
