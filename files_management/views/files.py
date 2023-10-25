from django.shortcuts import render, redirect
from rest_framework import status

from files_management.models import File
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class FilesView(APIView):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/sign_in/')
        search = request.GET.get('search', '')
        queryset = File.objects.all()
        if search:
            queryset = queryset.filter(title__contains=search.lower())
        context = {'files': queryset}
        return render(request, 'index.html', context)


class FileUploadView(APIView):

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/sign_in/')

        title = request.data.get('title')
        description = request.data.get('description')
        attachement = request.data.get('attachement')

        if title and description and attachement:
            # Create a new File object and save it to the database
            new_file = File(title=title, description=description, attachement=attachement)
            new_file.save()

            return redirect('/')
        else:
            return Response({'error': 'Invalid data provided'}, status=400)


class FileDetailView(APIView):
    def get(self, request, id):
        try:
            File.objects.get(pk=id).delete()
            return redirect('/')
        except Exception as e:
            msg = f'File is not available against id {id}'
            return redirect('/')

