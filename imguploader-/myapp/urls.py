from django.urls import path  
from myapp import views 

app_name = "myapp"

urlpatterns = [
    path('', views.home, name = "home"),
    path('addimage', views.AddImage, name = "addimage"),
    path('deleteimage/<int:idphoto>/', views.DeleteImage, name = "deleteimage"),
    path('addfile', views.AddFile, name = "addfile"),
    path('downloadfile/<int:file_id>/', views.downloadFile, name = "downloadFile"),
]
