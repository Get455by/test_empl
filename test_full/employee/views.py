import random
from datetime import datetime, timedelta

from django.shortcuts import render
from .models import Department, Employee


def department_tree_view(request):
    # Department.objects.all().delete()
    # Employee.objects.all().delete()
    # # Создание 5 корневых подразделений
    # root_departments = [Department.objects.create(name=f'Department {i + 1}') for i in range(5)]
    #
    # # Функция для создания подуровней с уникальными именами
    # def create_sub_departments(parent, depth, max_depth):
    #     if depth < max_depth:
    #         num_sub_departments = 5 if depth == 1 else 4 if depth == 2 else 3 if depth == 3 else 2
    #         for i in range(num_sub_departments):
    #             sub_department = Department.objects.create(
    #                 name=f'{parent.name} - Level {depth + 1} - Sub {i + 1}',
    #                 parent=parent
    #             )
    #             # Рекурсивное создание подуровней
    #             create_sub_departments(sub_department, depth + 1, max_depth)
    #
    # # Создание иерархии до 5 уровней
    # for root in root_departments:
    #     create_sub_departments(root, 1, 5)
    #
    # # Проверка количества подразделений
    # print(f'Создано подразделений: {Department.objects.count()}')
    #
    # # Создание сотрудников и их распределение по подразделениям
    # departments = Department.objects.all()
    #
    # for i in range(50000):
    #     department = random.choice(departments)
    #     Employee.objects.create(
    #         full_name=f'Employee {i + 1}',
    #         position=random.choice(['Developer', 'Manager', 'Analyst', 'Tester']),
    #         hire_date=datetime.now() - timedelta(days=random.randint(1, 365 * 10)),
    #         salary=random.uniform(30000, 150000),
    #         department=department
    #     )
    #
    # print(f'Создано сотрудников: {Employee.objects.count()}')

    departments = Department.objects.filter(parent=None).prefetch_related('children__children__children__children__children', 'employees')
    return render(request, 'department_tree.html', {'departments': departments})
