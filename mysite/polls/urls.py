from django.urls import path
from .import views

urlpatterns = [
    # creating a path for the 'index' view (127.0.0.1/polls/)
    path('', views.index, name="index")
]