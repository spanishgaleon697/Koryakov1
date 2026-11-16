class Course:
    def __init__(self, name, department, specialties):
        self.name = name
        self.department = department
        self.specialties = specialties
        self.students = []


class Department:
    def __init__(self, name):
        self.name = name
        self.courses = []


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

    def find_course(self, name):
        for department in self.departments:
            for course in department.courses:
                if course.name == name:
                    return course
        raise ValueError("Курс не найден")

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
        course = self.find_course(name)
        if student.speciality not in course.specialties:
            raise ValueError("Курс не подходит специальности")
        if course in student.courses:
            raise ValueError("Студент уже записан на этот курс")
        student.courses.append(course)
        course.students.append(student)
        print("Студент записан на курс")

    def remove_course(self, id, name):
        student = self.find_student(id)
        course = self.find_course(name)
        if course not in student.courses:
            raise ValueError("Студент не записан на этот курс")
        student.courses.remove(course)
        course.students.remove(student)
        student.grades.pop(name, None)
        print("Студент удален с курса")

    def set_grade(self, id, name, grade):
        student = self.find_student(id)
        course = self.find_course(name)
        if course not in student.courses:
            raise ValueError("Студент не записан на этот курс")
        if grade < 1 or grade > 10:
            raise ValueError("Оценка должна быть от 1 до 10")
        student.grades[name] = grade
        print("Оценка выставлена")

    def next_semester(self, id):
        student = self.find_student(id)
        if len(student.courses) == 0:
            raise ValueError("Нет изученных курсов")
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
        with open("student_" + id + ".txt", "w", encoding="utf-8") as file:
            file.write("Студент: " + student.name + "\n")
            file.write("ID: " + student.id + "\n")
            file.write("Специальность: " + student.speciality + "\n")
            file.write("Семестр: " + str(student.semester) + "\n\n")
            total = 0
            count = 0
            for course in student.courses:
                file.write("Курс: " + course.name + "\n")
                file.write("Кафедра: " + course.department.name + "\n")
                if course.name in student.grades:
                    grade = student.grades[course.name]
                    file.write("Оценка: " + str(grade) + "\n")
                    total += grade
                    count += 1
                else:
                    file.write("Оценка: нет\n")
                file.write("\n")
            average = total / count if count > 0 else 0
            file.write("Средний балл: " + str(average))
        print("Ведомость сохранена")

    def course_report(self, name):
        course = self.find_course(name)
        with open("course_" + name + ".txt", "w", encoding="utf-8") as file:
            file.write("Курс: " + course.name + "\n")
            file.write("Кафедра: " + course.department.name + "\n\n")
            file.write("Студенты, изучившие курс:\n")
            total = 0
            count = 0
            for student in course.students:
                if course.name in student.grades:
                    grade = student.grades[course.name]
                    file.write(student.name + " — " + str(grade) + "\n")
                    total += grade
                    count += 1
            average = total / count if count > 0 else 0
            file.write("\nСредний балл: " + str(average))
        print("Ведомость сохранена")


faculty = Faculty()
dep1 = Department("Кафедра информатики")
dep2 = Department("Кафедра компьютерной безопасности")
faculty.departments.append(dep1)
faculty.departments.append(dep2)

course1 = Course("Python", dep1, ["прикладная информатика"])
course2 = Course("Базы данных", dep1, ["прикладная информатика"])
course3 = Course("Сети", dep2, ["кибербезопасность"])
course4 = Course("Java", dep2, ["кибербезопасность"])
dep1.courses.extend([course1, course2])
dep2.courses.extend([course3, course4])

while True:
    print("\n1. Зачислить студента")
    print("2. Отчислить студента")
    print("3. Записать на курс")
    print("4. Удалить с курса")
    print("5. Выставить оценку")
    print("6. Перевести на следующий семестр")
    print("7. Ведомость студента")
    print("8. Ведомость курса")
    print("0. Выход")

    choice = input("\nВыберите действие: ")

    try:
        match choice:
            case "1":
                id = input("ID студента: ")
                name = input("Имя студента: ")
                speciality = input("Специальность: ")
                faculty.add_student(id, name, speciality)
            case "2":
                id = input("ID студента: ")
                faculty.remove_student(id)
            case "3":
                id = input("ID студента: ")
                name = input("Название курса: ")
                faculty.add_course(id, name)
            case "4":
                id = input("ID студента: ")
                name = input("Название курса: ")
                faculty.remove_course(id, name)
            case "5":
                id = input("ID студента: ")
                name = input("Название курса: ")
                grade = int(input("Оценка: "))
                faculty.set_grade(id, name, grade)
            case "6":
                id = input("ID студента: ")
                faculty.next_semester(id)
            case "7":
                id = input("ID студента: ")
                faculty.student_report(id)
            case "8":
                name = input("Название курса: ")
                faculty.course_report(name)
            case "0":
                break
            case _:
                print("Неверный пункт меню")
    except ValueError as error:
        print("Ошибка:", error)
    except Exception as error:
        print("Ошибка:", error)
