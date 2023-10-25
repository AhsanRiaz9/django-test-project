from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from rest_framework.views import APIView

from authentication.models import User


class SignUp(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'sign_up.html')

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        date_of_birth = request.POST.get('date_of_birth')
        user = User.objects.filter(email=email.lower()).first()
        if user:
            return render(request, 'sign_up.html')
        if password == confirm_password:
            user = User.objects.create_user(email=email, password=password, date_of_birth=date_of_birth)
            login(request, user)
        return redirect('/')

