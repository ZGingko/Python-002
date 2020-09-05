from Animal import Cat
from Animal import Dog


class Zoo(object):
    def __init__(self, name):
        self.name = name
        self.__animals = set()

    def add_animal(self, ani):
        if hasattr(self, ani.__class__.__name__):
            print(f"the zoo {self.name} has {ani.__class__.__name__} already.")
        else:
            setattr(self, ani.__class__.__name__, True)
            self.__animals.add(ani)           


if __name__ == '__main__':
    z = Zoo('小嘿动物园')
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    z.add_animal(cat1)
    have_cat = hasattr(z, 'Cat')
    print(f"the zoo {z.name} has a Cat:{have_cat}")
    print(f"{cat1.name} is ferocious? {cat1.is_ferocious}")
    print(f"{cat1.name} is ok as a pet? {cat1.is_ok_pet}")

    dog1 = Dog('阿黄', '食肉', '中等', '温顺的')
    z.add_animal(dog1)
    print(hasattr(z, "Dog"))
    print(f"the zoo {z.name} has a Dog:{have_cat}")

    dog2 = Dog('大黄', '食肉', '中等', '凶猛')
    z.add_animal(dog2)
