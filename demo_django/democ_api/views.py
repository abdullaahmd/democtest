from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomerSerializer
from .serializers import PolicySerializer
from .models import Customer
from .models import Policy
from django.db.models import Value as V
from django.db.models.functions import Concat

class CustomerViews(APIView):
    """
    create_customer hit this function
    """
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, name=None,dob=None):
        """
        search by dob and name can be obtained using this function
        tried to concatenate to enable search of partial names
        """
        if name:
            item = Customer.objects.annotate(full_name=Concat('first_name', V(' '), 'last_name')). \
                filter(full_name__icontains=name)
            serializer = CustomerSerializer(item, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        elif dob:
            item = Customer.objects.filter(dob__icontains=dob)
            serializer = CustomerSerializer(item, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Customer.objects.all()
        serializer = CustomerSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


class PolicyViews(APIView):
    def post(self, request):
        serializer = PolicySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, policy=None,customer=None):
        """
        search policy unique quote id
        search all policies associated with customer using unique customer id
        """
        if policy:
            item = Policy.objects.get(quote_id = policy)
            serializer = PolicySerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        elif customer:
            item = Policy.objects.filter(customer_id = customer)
            serializer = PolicySerializer(item, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Policy.objects.all()
        serializer = PolicySerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request):
        """
        enable to change the status of the quote like new, accepted or active
        :param request:
        :return:
        """
        item = Policy.objects.get(quote_id = request.data['quote_id'])
        serializer = PolicySerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)