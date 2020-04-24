from django.urls import path
from main import views
appname='main'
urlpatterns = [

    path('',views.index,name='index'),
    path('delete/<city_name>/',views.delete_city,name='delete_city'),
]
