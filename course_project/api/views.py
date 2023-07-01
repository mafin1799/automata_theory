from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer


def group_required(group_name):
    def decorator(view_func):
        # Функция для проверки принадлежности пользователя к группе
        def test_func(user):
            return user.groups.filter(name=group_name).exists()

        # Оберните представление в декоратор user_passes_test
        decorated_view_func = user_passes_test(test_func)(view_func)
        return decorated_view_func

    return decorator


class StudentOnlyAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Требуется аутентификация

    @group_required('Студенты')  # Декоратор для проверки принадлежности к группе 'Студенты'
    def get(self, request):
        # Ваш код для обработки GET-запроса
        return Response('Привет, Студент!')


# Пример API-представления, доступного только учителям
class TeacherOnlyAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Требуется аутентификация

    @group_required('Учителя')  # Декоратор для проверки принадлежности к группе 'Учителя'
    def get(self, request):
        # Ваш код для обработки GET-запроса
        return Response('Привет, Преподаватель!')


# Пример API-представления, доступного только администраторам
class AdminOnlyAPIView(APIView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.groups.filter(name='Администраторы').exists():
            # Ваш код представления для администраторов
            return Response('Привет, Администратор!')
        else:
            return Response('Доступ запрещен', status=403)


class TestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({'message': f'Hello, {user.username}!'})


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)