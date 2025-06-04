from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import load_classes
from .serializers import FitnessClassSerializer

class ClassListAPIView(APIView):
    def get(self, request):
        try:
            classes = load_classes()
        except FileNotFoundError:
            return Response(
                {"error": "Classes file not found."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        except Exception as e:
            return Response(
                {"error": f"Error loading classes: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        try:
            serializer = FitnessClassSerializer(classes, many=True)
        except Exception as e:
            return Response(
                {"error": f"Error serializing classes: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response(serializer.data, status=status.HTTP_200_OK)