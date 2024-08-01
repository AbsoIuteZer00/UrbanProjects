import inspect


def object_info(obj):
    my_dict_ = {}
    my_list_1 = []
    my_list_2 = []
    for attributes in dir(obj):
        if callable(attributes):
            my_list_2.append(attributes)
        else:
            my_list_1.append(attributes)
    my_dict_.update(type=type(obj), attributes=my_list_1, method=my_list_2, module=inspect.getmodule(obj))
    return my_dict_


class Object:
    def __init__(self, obj_1, obj_2):
        self.obj_1 = obj_1
        self.obj_2 = obj_2

    def multiplication(self):
        return self.obj_1 * self.obj_2


my_object = Object(5, 8)
print(object_info(my_object))
