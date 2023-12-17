from django.urls import path,include
from .views import front, note, note_detail
urlpatterns = [
    path("", front, name="front"),
    path("notes/", note, name="note"),
    path("notes/<int:pk>/", note_detail, name="detail"),
]
