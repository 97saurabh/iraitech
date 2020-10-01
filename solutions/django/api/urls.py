from django.urls import path
from . import views
app_name = 'api'

urlpatterns = [
    path('v1/',views.solution,name = "v1"),
    ]