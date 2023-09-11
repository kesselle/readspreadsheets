from django.urls import path
from . views import Exceluploadfile


urlpatterns =[
    path('upload-excel', Exceluploadfile.as_view(), name='upload-excel'),
]