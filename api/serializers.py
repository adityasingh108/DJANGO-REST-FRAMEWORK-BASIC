from rest_framework import serializers


class Studentserializers(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    city = serializers.CharField(max_length=100)
    RollNo = serializers.IntegerField()