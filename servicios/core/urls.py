from django.urls import path
from . import views

urlpatterns = [
    path('api/ListAll_Customer', views.CustomerAllViewSet.as_view()), #http://127.0.0.1:8000/api/ListAll_Customer
    path('Create_Customer', views.CustomerCreate.as_view()), #http://127.0.0.1:8000/api/Create_Customer
    path('Delete_Customer/<customer_id>', views.CustomerDelete.as_view()), #http://127.0.0.1:8000/api/Delete_Customer
    path('Update_Customer/<customer_id>', views.CustomerUpdate.as_view()), #http://127.0.0.1:8000/api/Update_Customer
]
