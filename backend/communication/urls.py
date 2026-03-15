from django.urls import path
from .views import ApiKeyCreation

urlpatterns = [
    path('' , ApiKeyCreation.as_view())
]
