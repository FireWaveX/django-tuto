from django.urls import path
from . import views

app_name = 'customer'
urlpatterns = [
    path('', views.CustomerList.as_view()),
    path(r'<int:pk>', views.CustomerList.as_view()),
]