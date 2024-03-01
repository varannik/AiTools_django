from django.urls import path
from . import views

urlpatterns = [
    path('submited/', views.SubmitedToolView.as_view()),

]
