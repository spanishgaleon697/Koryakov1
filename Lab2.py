class Discipline:
    def __init__(self, name, department, specialties):
        self.name = name
        self.department = department
        self.specialties = specialties
        self.students = []

class Department:
    def __init__(self, name):
        self.name = name
        self.disciplines = []

class Student:
    def __init__(self, id, name, speciality):
        self.id = id
        self.name = name
        self.speciality = speciality
        self.semester = 1
        self.courses = []
        self.grades = {}

class Faculty:
    def __init__(self):
        self.students = []
        self.departments = []
        self.specialties = [
            "прикладная информатика",
            "кибербезопасность"
        ]
    def find_student(self, id):
        for student in self.students:
            if student.id == id:
                return student
        raise ValueError("Студент не найден")
    def find_discipline(self, name):
        for department in self.departments:
            for course in department.disciplines:
                if course.name == name:
                    return course
        raise ValueError("Дисциплина не найдена")
    def add_student(self, id, name, speciality):
        for student in self.students:
            if student.id == id:
                raise ValueError("Такой ID уже существует")
        if speciality not in self.specialties:
            raise ValueError("Такой специальности нет")
        student = Student(id, name, speciality)
        self.students.append(student)
        print("Студент зачислен")
    def remove_student(self, id):
        student = self.find_student(id)
        for course in student.courses:
            course.students.remove(student)
        self.students.remove(student)
        print("Студент отчислен")
    def add_course(self, id, name):
        student = self.find_student(id)
        course = self.find_discipline(name)
        if student.speciality not in course.specialties:
            raise ValueError("Дисциплина не подходит специальности")
        if course in student.courses:
            raise ValueError("Студент уже записан на эту дисциплину")
        student.courses.append(course)
        course.students.append(student)
        print("Студент записан на дисциплину")
    def remove_course(self, id, name):
        student = self.find_student(id)
        course = self.find_discipline(name)
        if course not in student.courses:
            raise ValueError("Студент не записан на эту дисциплину")
        student.courses.remove(course)
        course.students.remove(student)
        student.grades.pop(name, None)
        print("Студент удален с дисциплины")
    def set_grade(self, id, name, grade):
        student = self.find_student(id)
        course = self.find_discipline(name)
        if course not in student.courses:
            raise ValueError("Студент не записан на эту дисциплину")
        if grade < 1 or grade > 10:
            raise ValueError("Оценка должна быть от 1 до 10")
        student.grades[name] = grade
        print("Оценка выставлена")
    def next_semester(self, id):
        student = self.find_student(id)
        if len(student.courses) == 0:
            raise ValueError("Нет изученных дисциплин")
        for course in student.courses:
            if course.name not in student.grades:
                raise ValueError("Не все оценки выставлены")
            if student.grades[course.name] < 4:
                raise ValueError("Есть неудовлетворительные оценки")
        student.semester += 1
        student.courses = []
        student.grades = {}
        print("Студент переведен на следующий семестр")
    def student_report(self, id):
        student = self.find_student(id)
        file = open("student_" + id + ".txt", "w", encoding="utf-8")
        file.write("Студент: " + student.name + "\n")
        file.write("ID: " + student.id + "\n")
        file.write("Специальность: " + student.speciality + "\n")
        file.write("Семестр: " + str(student.semester) + "\n\n")
        total = 0
        count = 0
        for course in student.courses:
            file.write("Дисциплина: " + course.name + "\n")
            file.write("Кафедра: " + course.department.name + "\n")
            if course.name in student.grades:
                grade = student.grades[course.name]
                file.write("Оценка: " + str(grade) + "\n")
                total += grade
                count += 1
            else:
                file.write("Оценка: нет\n")
            file.write("\n")
        if count > 0:
            average = total / count
        else:
            average = 0
        file.write("Средний балл: " + str(average))
        file.close()
        print("Ведомость сохранена")
    def course_report(self, name):
        course = self.find_discipline(name)
        file = open("course_" + name + ".txt", "w", encoding="utf-8")
        file.write("Дисциплина: " + course.name + "\n")
        file.write("Кафедра: " + course.department.name + "\n\n")
        file.write("Студенты, изучившие дисциплину:\n")
        total = 0
        count = 0
        for student in course.students:
            if course.name in student.grades:
                grade = student.grades[course.name]
                file.write(student.name + " — " + str(grade) + "\n")
                total += grade
                count += 1
        if count > 0:
            average = total / count
        else:
            average = 0
        file.write("\nСредний балл: " + str(average))
        file.close()
        print("Ведомость сохранена")
faculty = Faculty()
dep1 = Department("Кафедра информатики")
dep2 = Department("Кафедра компьютерной безопасности")
faculty.departments.append(dep1)
faculty.departments.append(dep2)
course1 = Discipline("Python", dep1, ["прикладная информатика"])
course2 = Discipline("Базы данных", dep1, ["прикладная информатика"])
course3 = Discipline("Сети", dep2, ["кибербезопасность"])
course4 = Discipline("Java", dep2, ["кибербезопасность"])
dep1.disciplines.append(course1)
dep1.disciplines.append(course2)
dep2.disciplines.append(course3)
dep2.disciplines.append(course4)
while True:
    print("\n1. Зачислить студента")
    print("2. Отчислить студента")
    print("3. Записать на дисциплину")
    print("4. Удалить с дисциплины")
    print("5. Выставить оценку")
    print("6. Перевести на следующий семестр")
    print("7. Ведомость студента")
    print("8. Ведомость дисциплины")
    print("0. Выход")
    choice = input("\nВыберите действие: ")
    if choice == "0":
        break
    try:
        if choice == "1":
            id = input("ID студента: ")
            name = input("Имя студента: ")
            speciality = input("Специальность: ")
            faculty.add_student(id, name, speciality)
        elif choice == "2":
            id = input("ID студента: ")
            faculty.remove_student(id)
        elif choice == "3":
            id = input("ID студента: ")
            name = input("Название дисциплины: ")
            faculty.add_course(id, name)
        elif choice == "4":
            id = input("ID студента: ")
            name = input("Название дисциплины: ")
            faculty.remove_course(id, name)
        elif choice == "5":
            id = input("ID студента: ")
            name = input("Название дисциплины: ")
            grade = int(input("Оценка: "))
            faculty.set_grade(id, name, grade)
        elif choice == "6":
            id = input("ID студента: ")
            faculty.next_semester(id)
        elif choice == "7":
            id = input("ID студента: ")
            faculty.student_report(id)
        elif choice == "8":
            name = input("Название дисциплины: ")
            faculty.course_report(name)
        else:
            print("Неверный пункт меню")
    except ValueError as error:
        print("Ошибка:", error)
    except Exception as error:
        print("Ошибка:", error)