from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('demo/', views.demo),
    path('index/', views.index),
    path('insert/', views.insert),
    path('show/',views.show),
    path('update/',views.update),
    path('delete/', views.delete),
    path('completeupdate/',views.completeupdate)

]