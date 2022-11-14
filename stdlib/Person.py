class Person:
    name = []

    def set_name(self, user_name):
        self.name.append(user_name)
        return len(self.name) - 1

    def get_name(self, user_id):
        if user_id >= len(self.name):
            return 'There is no such user'
        else:
            return self.name[user_id]


# __name__ 是个特殊的变量，Python会为他自动赋值为当前的模块名称， 如果被直接运行的话，它的名 字就是 __main__ ;
# 这句话的意思就是:当模块直接被运行时，下面的代码块将被运行，如果这个文件被当做模块导入，就不会运行。
if __name__ == '__main__':
    person = Person()
    print('User Abbas has been added with id ', person.set_name('Abbas'))
    print('User associated with id 0 is ', person.get_name(0))
