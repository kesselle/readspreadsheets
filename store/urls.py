from django.urls import path
from readspreadsheets import settings
from store import views
from django.conf.urls.static import static


urlpatterns =[
    
    path('import_excel/', views.importExcel, name='import_excel'),
    path('tablelist/', views.displayTable, name='table_list'),
    path('delete/<int:id>/', views.Delete_table, name='delete_table'),
    path('edit/<int:id>/', views.edit_table, name='edit_table'),
    path('retrievedata/', views.retrieve_data, name='get_data')

]
if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)