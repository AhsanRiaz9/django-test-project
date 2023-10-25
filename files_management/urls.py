from django.urls import path
from files_management.views import FilesView, FileUploadView, FileDetailView

urlpatterns = [
    path('', FilesView.as_view()),
    path('upload_file/', FileUploadView.as_view()),
    path('file/<int:id>/', FileDetailView.as_view()),

]


