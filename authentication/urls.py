from django.urls import path
from authentication.views import SignUp, SignIn, LogoutView

urlpatterns = [
    path('sign_in/', SignIn.as_view()),
    path('sign_up/', SignUp.as_view()),
    path('logout/', LogoutView.as_view(), name='logout'),

]
