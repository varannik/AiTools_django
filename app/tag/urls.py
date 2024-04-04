from django.urls import path
from . import views

urlpatterns = [
    path('tags/getms', views.RetrieveMainSub.as_view()),
    path('tags/getca', views.RetrieveCareer.as_view()),
    path('tags/lct', views.Tagging.as_view()),

]