from rest_framework import viewsets
from .serializers import CustomerSerializer, CustomerMiniSerializer
from .models import Customer
from rest_framework.response import Response


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def list(self, request, *args, **kwargs):
        customers = Customer.objects.all()
        serializer = CustomerMiniSerializer(customers, many=True)
        return Response(serializer.data)