from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    ani_type_dict = {"食肉": 1, "食草": 2}
    body_type_dict = {"小": 1, "中等": 2, "大": 3}
    character_dict = {"温顺": 1, "凶猛": 2}

    def __init__(self, ani_type, body_type, character):
        if ani_type not in Animal.ani_type_dict:
            raise ValueError(f"{ani_type} is not a right ani_type")
        if body_type not in Animal.body_type_dict:
            raise ValueError(f"{body_type} is not a right body_type")
        if character not in Animal.character_dict:
            raise ValueError(f"{character} is not a right character")

        self.ani_type = ani_type
        self.body_type = body_type
        self.character = character

    @property
    def is_ferocious(self):
        return Animal.ani_type_dict[self.ani_type] == 1 and Animal.body_type_dict[self.body_type] > 1 and Animal.character_dict[self.character] == 2


class Cat(Animal):
    barking = "喵~~喵~~"

    def __init__(self, name, ani_type, body_type, character):
        super().__init__(ani_type, body_type, character)
        self.name = name

    @property
    def is_ok_pet(self):
        return not self.is_ferocious


class Dog(Animal):
    barking = "汪汪。。汪汪。。"

    def __init__(self, name, ani_type, body_type, character):
        super().__init__(ani_type, body_type, character)
        self.name = name

    @property
    def is_ok_pet(self):
        return not self.is_ferocious
