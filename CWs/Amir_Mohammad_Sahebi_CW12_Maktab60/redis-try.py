import redis

DB = redis.Redis(charset="utf-8", decode_responses=True)


class Student:

    def __init__(self, name, age) -> None:
        self.student_number = Student.stu_number()
        self.name = name
        self.age = age
        DB.hmset(
            f'student:{self.student_number}:info',
            {
                "name": self.name,
                "age": self.age,
                "student_number": self.student_number
            })

    @classmethod
    def stu_number(cls):
        DB.incr('student_number')
        student_number = DB.get('student_number')
        return student_number

    def add_point(self, grade):
        DB.rpush(f"student:{self.student_number}:grade", grade)
        return f'the {grade} successfully added to {self.name}'

    def gpa(self):
        key = f"student:{self.student_number}:grade"
        print(f'the average point for {self.name} is {sum(list(map(int, DB.lrange(key, 0, -1)))) / DB.llen(key)} ')

    def add_course(self, course):
        DB.rpush(f"student:{self.student_number}:courses", course)

    def show_course(self):
        key = f"student:{self.student_number}:courses"
        for i in DB.lrange(key, 0, -1):
            print(i)

    @staticmethod
    def get_all_students():
        for i in DB.scan_iter(match="student*", _type="HASH"):
            print(f'{DB.hget(i, "student_number")}->{DB.hget(i, "name")}')


class Course:

    def __init__(self, name, term) -> None:
        self.id = Course.course_id()
        self.name = name
        self.term = term
        DB.hmset(
            f'course:{self.id}:info',
            {
                "course_id": self.id,
                "name": self.name,
                "term": self.term

            })
        DB.rpush(f"term:{self.term}", f"{self.id}->{self.name}")

    @classmethod
    def course_id(cls):
        DB.incr('course_number')
        student_number = DB.get('course_number')
        return student_number

    @staticmethod
    def get_all_courses():
        for i in DB.scan_iter(match="course*", _type="HASH"):
            print(f'{DB.hget(i, "course_id")}->{DB.hget(i, "name")}')

    @staticmethod
    def get_all_courses_by_term(term):
        for lis in DB.scan_iter(match=f"term:{term}*", _type="LIST"):
            for lesson in DB.lrange(lis, 0, -1):
                print(lesson)
