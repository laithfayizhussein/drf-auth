  
from django.urls import path
from .views import AppList, AppDetail

urlpatterns = [
    path('', AppList.as_view(), name='app_list'),
    path('<int:pk>/', AppDetail.as_view(), name='app_detail'),
]