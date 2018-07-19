class Person(object):
    def __init__(self, name='', age=20, sex='man'):
        self.setName(name)
        self.setAge(age)
        self.setSex(sex)

    def setName(self, name):
        if not isinstance(name, str):
            print('name must be string.')
            return
        self.__name = name

    def setAge(self, age):
        if not isinstance(age, int):
            print('age must be integer.')
            return
        self.__age = age

    def setSex(self, sex):
        if sex != 'man' and sex != 'woman':
            print('sex must be "man" or "woman"')
            return
        self.__sex = sex

    def show(self):
        print('Name:', self.__name)
        print('Age:', self.__age)
        print('Sex:', self.__sex)


class Teacher(Person):
    def __init__(self, name='', age=30, sex='man', department='Computer'):
        super(Teacher, self).__init__(name, age, sex)
        ## or, use another method like below:
        # Person.__init__(self, name, age, sex)
        self.setDepartment(department)

    def setDepartment(self, department):
        if not isinstance(department, str):
            print('department must be a string.')
            return
        self.__department = department

    def show(self):
        super(Teacher, self).show()
        print('Department:', self.__department)


if __name__ == '__main__':
    zhangsan = Person('Zhang San', 19, 'man')
    zhangsan.show()

    lisi = Teacher('Li Si', 32, 'man', 'Math')
    lisi.show()
    lisi.setAge(40)
    lisi.show()