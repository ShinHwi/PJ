from django.urls import include, path
from blog import views

urlpatterns = [
    path("", views.index, name="index"),
    path("english/", views.english, name="english"),
    path("japanese/", views.japanese, name="japanese"),
    path("chinese/", views.chinese, name="chinese"),

]