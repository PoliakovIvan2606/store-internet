from django.urls import path

from .views import OrderCreateView, CanceledTeamplateView, SuccesTemplateView

app_name = 'orders'

urlpatterns = [
    path('order-create', OrderCreateView.as_view(), name='order-create'),
    path('order-cancaled', CanceledTeamplateView.as_view(), name='order-cancaled'),
    path('order-succes', SuccesTemplateView.as_view(), name='order-succes'),
]