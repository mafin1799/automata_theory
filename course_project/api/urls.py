from django.urls import path
from . import views
from .views import StudentOnlyAPIView, TeacherOnlyAPIView, AdminOnlyAPIView, UserProfileView

urlpatterns = [
    # ... другие маршруты ...
    path('test/', views.TestView.as_view(), name='test'),
    path('student/', StudentOnlyAPIView.as_view(), name='student-api'),
    path('teacher/', TeacherOnlyAPIView.as_view(), name='teacher-api'),
    path('admin/', AdminOnlyAPIView.as_view(), name='admin-api'),

    path('user/profile/', UserProfileView.as_view(), name='user_profile'),
]