from django.contrib.auth.models import Group, User

# Получение существующей группы "Студенты" или создание новой группы, если она не существует
students_group, _ = Group.objects.get_or_create(name='Студенты')

# Создание группы "Учителя"
teachers_group, _ = Group.objects.get_or_create(name='Учителя')

# Создание группы "Администраторы"
admins_group, _ = Group.objects.get_or_create(name='Администраторы')