def introspection_info(obj):
    obj_type = type(obj).__name__
    print(f'Type: {obj_type}')
    # attributes_obj = dir(obj)
    attributes_obj = [attribute for attribute in dir(obj) if not callable(getattr(obj, attribute))]
    print(f'Attributes: {attributes_obj}')
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    print(f'Methods: {methods}')
    module = obj.__class__.__module__
    return f'Module: {module}'


number_info = introspection_info(42)
print(number_info)

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


h1 = introspection_info(House('ЖК Эльбрус', 10))
print(h1)
