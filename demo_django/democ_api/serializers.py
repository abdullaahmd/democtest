from rest_framework import serializers
from .models import Customer
from .models import Policy

class CustomerSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    dob = serializers.DateField()

    class Meta:
        model = Customer
        fields = ('__all__')


class PolicySerializer(serializers.ModelSerializer):
    customer_id = serializers.IntegerField()
    type = serializers.CharField(max_length=50)
    premium = serializers.IntegerField()
    cover = serializers.IntegerField()
    duration = serializers.IntegerField()
    state = serializers.CharField(max_length=50)

    class Meta:
        model = Policy
        fields = ('__all__')