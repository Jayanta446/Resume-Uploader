from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
   path('resume-form/', views.resume_form),
   path('resume-details/<int:id>/', views.resume_details, name = 'details'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
