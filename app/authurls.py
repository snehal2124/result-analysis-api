from django.urls import path
from .authviews import LoginView, UserView

urlpatterns = [
    path('login', LoginView.as_view()),
    path('user', UserView.as_view())
]
