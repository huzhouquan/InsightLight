# api/urls.py
from django.urls import path
from .views import ResultCreateView, ResultRetrieveView

urlpatterns = [
    path('results/', ResultCreateView.as_view(), name='result-create'),
    path('results/<uuid:id>/', ResultRetrieveView.as_view(), name='result-retrieve'),
]