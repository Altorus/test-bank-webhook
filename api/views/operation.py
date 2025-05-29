from rest_framework import status, views
from rest_framework.response import Response

from api import serializers, exceptions


class PaymentViewSet(views.APIView):
    def post(self, request, *args, **kwargs):
        try:
            serializer = serializers.PaymentSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except exceptions.PaymentDuplicationException:
            return Response(status=status.HTTP_200_OK)
