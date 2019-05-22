from django.shortcuts import render
from rest_framework import viewsets

from django.contrib.auth.models import User, Group
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer, UserSerializer, GroupSerializer
from rest_framework import mixins, generics

# Communication with external apps
# Customer.objects.all() = select * in customer
class CustomerList(mixins.ListModelMixin, 
    mixins.CreateModelMixin, 
    generics.GenericAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    # authentication_classes = ()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer