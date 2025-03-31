from rest_framework import serializers
from ..models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'user', 'course', 'amount', 'payment_method', 'status', 'created_at', 'updated_at']