from rest_framework import serializers

class BookingSerializer(serializers.Serializer):
    class_id = serializers.IntegerField()
    client_name = serializers.CharField()
    client_email = serializers.EmailField()
    timestamp = serializers.DateTimeField()
