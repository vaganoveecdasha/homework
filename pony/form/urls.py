from django.urls import path
from .views import *

urlpatterns = [
    path('', form_page, name="form"),
]