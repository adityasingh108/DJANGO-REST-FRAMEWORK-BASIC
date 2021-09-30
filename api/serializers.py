from rest_framework import serializers
from .models import Student


class Studentserializers(serializers.Serializer):
    # id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    city = serializers.CharField(max_length=100)
    RollNo = serializers.IntegerField()
    
    def create(self, validated_data):
        return Student.objects.create(**validated_data)