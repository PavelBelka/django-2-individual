from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('register/', views.register, name = 'register'),
    path('mypurchase/', views.my_purchase, name = 'mypurchase'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('configurator/<int:ids>/<int:step>/<int:complid>', views.configurator, name='configurator'),
    path('buy/<int:car_id>/<int:costs>', views.PurchaseCreate, name='buy')
]