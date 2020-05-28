from django.urls import path

from . import views

urlpatterns = [
    path('', views.CarList.as_view(), name='car_list'),
    path('Cars/', views.CarList.as_view(), name='car_list'),
    path('view/<int:pk>', views.CarView.as_view(), name='car_view'),
    path('new', views.CarCreate.as_view(), name='car_new'),
    path('view/<int:pk>', views.CarView.as_view(), name='car_view'),
    path('edit/<int:pk>', views.CarUpdate.as_view(), name='car_edit'),
    path('delete/<int:pk>', views.CarDelete.as_view(), name='car_delete'),
]