class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        print("name is: %s" %(self.__name))

    def get_score(self):
        print("score is: %s" %(self.__score))


stu = Student('wangliang', 90)
stu.get_name()
stu.get_score()