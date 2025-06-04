from rest_framework import serializers

class FitnessClassSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    instructor = serializers.CharField()
    datetime = serializers.DateTimeField()
    available_slots = serializers.IntegerField()
