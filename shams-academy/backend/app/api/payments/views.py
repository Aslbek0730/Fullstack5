from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import PaymentSerializer
from .models import Payment
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        payment = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        payment = self.get_object()
        serializer = self.get_serializer(payment)
        return Response(serializer.data)

    def update(self, request, pk=None):
        payment = self.get_object()
        serializer = self.get_serializer(payment, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        payment = serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        payment = self.get_object()
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)