class Student(object):
    """Main class of students"""
    def __init__(self, last_name, group_number, progress):
        self.last_name = last_name
        self.group_number = Group(group_number)
        self.progress = progress


class Group(object):
    """Class of groups in university"""
    def __init__(self, name):
        self.name = name


class UserInfoAggregator(object):
    """Class for working with students data base"""
    data_context = [
        ('Vasiliev A.A.', 5, {'math': 4, 'literature': 3, 'physics': 3}),
        ('Khorotnev D.M.', 5, {'math': 3, 'literature': 5, 'physics': 2}),
        ('Murashko I.A.', 3, {'math': 4, 'literature': 5, 'physics': 5}),
        ('Sinitsina A.O.', 1, {'math': 3, 'literature': 2, 'physics': 3}),
        ('Jejelenko M.D.', 3, {'math': 2, 'literature': 3, 'physics': 3})
    ]
    __student_db = []

    def _make_student_db(self):
        """Method for recording Class Student examples to db from data_context"""
        for student in self.data_context:
            last_name, group_number, progress = student[0], student[1], student[2]
            self.__student_db.append(Student(last_name, group_number, progress))
        return self.__student_db

    def get_students_with_good_marks(self):
        """Method shows us only students with marks 4 or 5"""
        students_with_good_marks = []
        self._make_student_db()
        for elem in self.__student_db:
            if 4 in elem.progress.values():
                students_with_good_marks.append((elem.last_name, elem.group_number.name))
            elif 5 in elem.progress.values():
                students_with_good_marks.append((elem.last_name, elem.group_number.name))
        return students_with_good_marks


task1 = UserInfoAggregator()
print(task1.get_students_with_good_marks())
