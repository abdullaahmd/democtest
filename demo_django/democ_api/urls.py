from django.urls import path
from .views import CustomerViews
from .views import PolicyViews


urlpatterns = [
    path('create_customer/', CustomerViews.as_view()),
    path('customer/name/<str:name>/', CustomerViews.as_view()),
    path('customer/dob/<str:dob>/', CustomerViews.as_view()),
    path('create_quote/', PolicyViews.as_view()),
    path('policies/policy/<int:policy>', PolicyViews.as_view()),
    path('policies/customer/<int:customer>', PolicyViews.as_view())
]