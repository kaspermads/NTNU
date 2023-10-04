from django.urls import path
from api.views import RoomView

urlpatterns = [
    path('home', RoomView.as_view()),
    
]
