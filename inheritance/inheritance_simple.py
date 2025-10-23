class BaseClass(object):
    def __init__(self,  property):
        self.property = property

    def message(self):
        print('Welcome to Base Class')

    def message_base_class(self):
        print('This is a message from Base Class')

class ChildClass(BaseClass):
    def __init__(self, property):
        BaseClass.__init__(self, property)

    def message(self):
        print('Welcome to Child Class')
        print('This is inherited from BaseClass')

    # def message_base_class(self):
    #     print('This is a message from inherited from BaseClass')


if __name__ == '__main__':
 base_obj = BaseClass('property')
 base_obj.message()
 child_obj = ChildClass('property')
 child_obj.message()
 child_obj.message_base_class()