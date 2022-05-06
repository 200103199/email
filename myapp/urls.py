from django.urls import path
from .views import *
urlpatterns=[
    path('add_emp/', add_emp),
    path('send/', send_message)
    ]
