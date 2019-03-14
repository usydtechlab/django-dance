from django.urls import path
from . import views
from .views import ListSongsView


urlpatterns = [
    #path('', views.index, name='index'),
    path('', ListSongsView.as_view(), name="songs-all"),
    path('songs/', ListSongsView.as_view(), name="songs-all")
]