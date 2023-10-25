from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from rest_framework.views import APIView

class SignIn(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'sign_in.html')

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/sign_in/')
