from django.urls import path
from .views import UpdateTable


urlpatterns = [
    path('match/tables/',UpdateTable.as_view(),name='update-table'),
]
