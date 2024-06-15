from django.core.management.base import BaseCommand
from users.models import UserModel
from boards.models import BoardModel
from participation.models import ParticipationModel
from tasks.models import TaskModel
from datetime import date, timedelta


class Command(BaseCommand):
    help = 'Заполнить базу данных тестовыми данными'

    def handle(self, *args, **kwargs):
        users = [
            UserModel(
                username='ivanov',
                email='ivanov@example.com',
                first_name='Иван',
                last_name='Иванов'
            ),
            UserModel(
                username='petrov',
                email='petrov@example.com',
                first_name='Петр',
                last_name='Петров'
            ),
            UserModel(
                username='sidorov',
                email='sidorov@example.com',
                first_name='Сидор',
                last_name='Сидоров'
            ),
            UserModel(
                username='smirnova',
                email='smirnova@example.com',
                first_name='Анна',
                last_name='Смирнова'
            ),
        ]

        for user in users:
            user.set_password('password123')
            user.save()

        boards = [
            BoardModel(
                title='Проект Альфа',
                author=UserModel.objects.get(username='ivanov'),
                description='Описание проекта Альфа'
            ),
            BoardModel(
                title='Проект Бета',
                author=UserModel.objects.get(username='petrov'),
                description='Описание проекта Бета'
            ),
            BoardModel(
                title='Проект Гамма',
                author=UserModel.objects.get(username='smirnova'),
                description='Описание проекта Гамма'
            ),
        ]

        for board in boards:
            board.save()

        participations = [
            ParticipationModel(
                participant=UserModel.objects.get(username='ivanov'),
                board=BoardModel.objects.get(title='Проект Альфа'),
                can_edit=True
            ),
            ParticipationModel(
                participant=UserModel.objects.get(username='petrov'),
                board=BoardModel.objects.get(title='Проект Альфа'),
                can_edit=False
            ),
            ParticipationModel(
                participant=UserModel.objects.get(username='sidorov'),
                board=BoardModel.objects.get(title='Проект Бета'),
                can_edit=True
            ),
            ParticipationModel(
                participant=UserModel.objects.get(username='smirnova'),
                board=BoardModel.objects.get(title='Проект Гамма'),
                can_edit=True
            ),
        ]

        for participation in participations:
            participation.save()

        tasks = [
            TaskModel(
                title='Задача 1 по проекту Альфа',
                description='Описание задачи 1',
                created_at=date.today(),
                deadline=date.today() + timedelta(days=10),
                status='to-do',
                priority='high',
                on_board=BoardModel.objects.get(title='Проект Альфа'),
                assignee=UserModel.objects.get(username='ivanov')
            ),
            TaskModel(
                title='Задача 2 по проекту Альфа',
                description='Описание задачи 2',
                created_at=date.today(),
                deadline=date.today() + timedelta(days=5),
                status='in-progress',
                priority='medium',
                on_board=BoardModel.objects.get(title='Проект Альфа'),
                assignee=UserModel.objects.get(username='petrov')
            ),
            TaskModel(
                title='Задача 1 по проекту Бета',
                description='Описание задачи 1',
                created_at=date.today(),
                deadline=date.today() + timedelta(days=20),
                status='to-do',
                priority='low',
                on_board=BoardModel.objects.get(title='Проект Бета'),
                assignee=UserModel.objects.get(username='sidorov')
            ),
            TaskModel(
                title='Задача 1 по проекту Гамма',
                description='Описание задачи 1',
                created_at=date.today(),
                deadline=date.today() + timedelta(days=15),
                status='completed',
                priority='high',
                on_board=BoardModel.objects.get(title='Проект Гамма'),
                assignee=UserModel.objects.get(username='smirnova')
            ),
        ]

        for task in tasks:
            task.save()

        self.stdout.write(
            self.style.SUCCESS(
                'База данных успешно заполнена тестовыми данными'
            )
        )
