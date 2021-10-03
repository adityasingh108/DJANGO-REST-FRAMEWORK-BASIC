from rest_framework import serializers
from .models import Student


class Studentserializers(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    city = serializers.CharField(max_length=100)
    RollNo = serializers.IntegerField()
    
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.city = validated_data.get('city', instance.city)
        instance.RollNo = validated_data.get('RollNo', instance.RollNo)
        instance.save()
        return instance