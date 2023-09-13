from django.urls import path
from readspreadsheets import settings
from store import views
from django.conf.urls.static import static


urlpatterns =[
    
    path('import_excel/', views.importExcel, name='import_excel')
]
if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)