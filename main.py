from pprint import pprint

class BaseMetaClass(type):
    def __new__(cls, name, bases, dct):
        print(' --- Create Class')
        print()
        print('Meta __new__')
        print('Class', cls)
        print('name', name)
        print('bases', bases)
        print('dict', end=' ')
        pprint(dct)
        print()
        return super().__new__(cls, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print(' --- Inicialize/Update Class')
        print()
        print('Meta __init__')
        print('Class', cls)
        print('name', name)
        print('bases', bases)
        print('dict', end=' ')
        pprint(dct)
        print()
        return super().__init__(name, bases, dct)

class Example(object, metaclass=BaseMetaClass):
    def __new__(cls, *args, **kwargs):
        print(' --- Create Instance')
        print()
        print('__new__')
        print('args', args)
        print('kwargs', kwargs)
        print()
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        print(' --- Inicialize/Update Instance')
        print()
        print('__init__')
        print('args', args)
        print('kwargs', kwargs)
        print()
        return super().__init__()


Example(
    1, 2, 3, 4, 5,
    name='Vinicio',
    last_name='Valbuena',
)
