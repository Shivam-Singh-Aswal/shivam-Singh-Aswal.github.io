from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("schedule/", views.schedule, name="schedule"),
    path("register/", views.registerEdLecture, name="register"),
    # path("teaminfo/", views.theTeam, name="teaminfo"),
    path("attendees/", views.attendees, name="attendees"),
    # path("registration/success/", views.)
]