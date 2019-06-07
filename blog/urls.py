from django.urls import path
from . import views
urlpatterns = [
    path('1/',views.f1,name="1"),
    path('2/',views.f2,name="2"),
]