from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime
import pytz

from .serializers import BookingSerializer
from .utils import load_bookings, save_booking
from apps.classes.utils import load_classes, save_classes


class BookingAPIView(APIView):
    def post(self, request):
        data = request.data
        class_id = data.get("class_id")
        name = data.get("client_name")
        email = data.get("client_email")

        if not (class_id and name and email):
            return Response({"error": "Missing required fields."}, status=400)

        try:
            classes = load_classes()
        except Exception as e:
            return Response({"error": f"Error loading classes: {str(e)}"}, status=500)

        target_class = next((c for c in classes if c["id"] == class_id), None)

        if not target_class:
            return Response({"error": "Class not found."}, status=404)

        if target_class["available_slots"] <= 0:
            return Response({"error": "No slots available."}, status=400)

        try:
            all_bookings = load_bookings()
        except Exception as e:
            return Response({"error": f"Error loading bookings: {str(e)}"}, status=500)

        # Check for duplicate booking
        already_booked = any(
            b["class_id"] == class_id and b["client_email"] == email
            for b in all_bookings
        )
        if already_booked:
            return Response({"error": "You have already booked this class."}, status=400)

        try:
            # Save booking
            save_booking({
                "class_id": class_id,
                "client_name": name,
                "client_email": email,
                "timestamp": datetime.now(pytz.UTC).isoformat()
            })

            # Update available slots
            target_class["available_slots"] -= 1
            save_classes(classes)

        except Exception as e:
            return Response({"error": f"Booking failed: {str(e)}"}, status=500)

        return Response({"message": "Booking successful."}, status=201)


class BookingListAPIView(APIView):
    def get(self, request):
        email = request.query_params.get("email")
        if not email:
            return Response({"error": "Email is required."}, status=400)

        try:
            all_bookings = load_bookings()
        except Exception as e:
            return Response({"error": f"Error loading bookings: {str(e)}"}, status=500)

        user_bookings = [b for b in all_bookings if b["client_email"] == email]

        try:
            serializer = BookingSerializer(user_bookings, many=True)
        except Exception as e:
            return Response({"error": f"Error serializing data: {str(e)}"}, status=500)

        return Response(serializer.data, status=200)