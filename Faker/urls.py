from os import name
from django.urls import path
from .views import Paginationshowview, Populate



urlpatterns=[
    path('polu/',Populate,name='populate'),
    path('page/',Paginationshowview,name='pagination')
]