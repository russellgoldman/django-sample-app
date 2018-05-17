from django.urls import path
from .import views

urlpatterns = [
    # creating a path for the 'index' view
    # e.g. 127.0.0.1/polls/
    path('', views.index, name='index'),

    # int specifies the parameter type and question_id is the parameter to show in PATH
    # e.g. 127.0.0.1/polls/1
    path('<int:question_id>/', views.detail, name='detail'),

    # question_id is the parameter to show in PATH, and 'results' is the hardcoded route after it
    # e.g. 127.0.0.1/polls/1/vote
    path('<int:question_id>/results/', views.results, name='results'),

    # e.g. 127.0.0.1/polls/1/results
    path('<int:question_id>/vote/', views.vote, name='vote'),
]