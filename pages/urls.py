from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('api/chart/data/', views.ChartData.as_view()),
]