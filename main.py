class Mentor:
    def __init__(self, name, surname, courses=[]):
        self.name = name
        self.surname = surname
        self.courses = courses

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

class Lecturer(Mentor):
    def __init__(self, name, surname, courses=[]):
        super().__init__(name, surname, courses)
        self.grades = {}

    def __str__(self):
        avg_grade = sum([sum(grades) / len(grades) for grades in self.grades.values()]) / len(self.grades) if self.grades else 0
        return super().__str__() + f'\nСредняя оценка за лекции: {avg_grade:.1f}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        avg_self_grade = sum([sum(grades) / len(grades) for grades in self.grades.values()]) / len(self.grades) if self.grades else 0
        avg_other_grade = sum([sum(grades) / len(grades) for grades in other.grades.values()]) / len(other.grades) if other.grades else 0
        return avg_self_grade < avg_other_grade

class Reviewer(Mentor):
    def review_homework(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses and course in self.courses:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]

class Student:
    def __init__(self, name, surname, courses=[]):
        self.name = name
        self.surname = surname
        self.courses = courses
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses and course in self.courses:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]

    def __str__(self):
        avg_grade = sum([sum(grades) / len(grades) for grades in self.grades.values()]) / len(self.grades) if self.grades else 0
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_grade:.1f}\nКурсы в процессе изучения: {", ".join(self.courses)}\nЗавершенные курсы: Введение в программирование'

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        avg_self_grade = sum([sum(grades) / len(grades) for grades in self.grades.values()]) / len(self.grades) if self.grades else 0
        avg_other_grade = sum([sum(grades) / len(grades) for grades in other.grades.values()]) / len(other.grades) if other.grades else 0
        return avg_self_grade < avg_other_grade

def avg_homework_grade(students, course):
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])
    return sum(total_grades) / len(total_grades) if total_grades else 'Нет оценок по данному курсу'

def avg_lecture_grade(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])
    return sum(total_grades) / len(total_grades) if total_grades else 'Нет оценок по данному курсу'

# Создание экземпляров классов
student1 = Student('Иван', 'Иванов', ['Python'])
student2 = Student('Петр', 'Петров', ['Python'])
lecturer1 = Lecturer('Алексей', 'Алексеев', ['Python'])
lecturer2 = Lecturer('Сергей', 'Сергеев', ['Python'])
reviewer1 = Reviewer('Василий', 'Васильев', ['Python'])
reviewer2 = Reviewer('Николай', 'Николаев', ['Python'])

# Вызов методов
reviewer1.review_homework(student1, 'Python', 8)
reviewer2.review_homework(student2, 'Python', 9)
student1.rate_lecturer(lecturer1, 'Python', 10)
student2.rate_lecturer(lecturer2, 'Python', 9)

# Подсчет средней оценки
print(f'Средняя оценка за домашние задания по курсу Python: {avg_homework_grade([student1, student2], "Python")}')
print(f'Средняя оценка за лекции по курсу Python: {avg_lecture_grade([lecturer1, lecturer2], "Python")}')

# Вывод информации о студентах, лекторах и проверяющих
print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)