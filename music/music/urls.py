
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('genre/', views.genre),
    path('add_genre/', views.add_genre),
    path('editgenre/<int:id_genre>', views.edit_genre),
    path('deletegenre/<int:id_genre>', views.deleteGenre),
    path('track/', views.track),
    path('add_track/', views.add_track),
    path('edittrack/<int:id_track>', views.edit_track),
    path('deletetrack/<int:id_track>', views.deleteTrack),
]
