from django.contrib.auth import views as auth_views, logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from rest_framework.views import APIView


class LogoutView(APIView):
    def get(self, request):
        logout(request)
        return redirect('/')
