Speech_dict = {'Гусь': 'Га-Га-Га', 'Корова': 'Мууу', 'Овца': 'Беее',\
               'Курица': 'Ко-Ко-Ко', 'Коза': 'Меее', 'Утка': 'Кря'}

# Speech_dict = {Goose.animal_type: Goose.speech, ...}


def voice_definition(who_speech):
    for pet, language in Speech_dict.items():
        counter = 0
        if who_speech in language:
            print(f'Это {pet}')
            counter += 1
    if counter == 0:
        print('Такого животного на ферме нет')


voice_definition('Кря')
print()


class Animal:

    def __init__(self, name, weight, speech):
        self.name = name
        self.weight = weight
        self.speech = speech

    def eat(self, food):
        self.weight += food
        print(f'Животному {self.name} дано {food} кг корма')


class Poultry(Animal):

    def __init__(self, name, weight, speech):
        super().__init__(name, weight, speech)

    def gather_eggs(self, eggs_count):
        eggs_gathered_count = 0
        eggs_gathered_count += eggs_count
        print(f'У животного {self.name} собрали {eggs_gathered_count} яиц')


class Chicken(Poultry):

    def __init__(self, name, weight, speech='Ко-Ко-Ко', animal_type='Курица'):
        super().__init__(name, weight, speech)
        self.animal_type = animal_type

    def gather_eggs(self, eggs_count):
        eggs_gathered_count = 0
        eggs_gathered_count += eggs_count
        print(f'У курицы {self.name} собрали {eggs_gathered_count} яиц')

    def eat(self, food):
        self.weight += food
        print(f'Курице {self.name} дано {food} кг корма')


class Duck(Poultry):

    def __init__(self, name, weight, speech='Кря', animal_type='Утка'):
        super().__init__(name, weight, speech)
        self.animal_type = animal_type


class Goose(Poultry):

    def __init__(self, name, weight, speech='Га-Га-Га', animal_type='Гусь'):
        super().__init__(name, weight, speech)
        self.animal_type = animal_type


class MilkGivers(Animal):

    def __init__(self, name, weight, speech):
        super().__init__(name, weight, speech)

    def milk(self):
        print(f'Животное {self.name} подоено')


class Cow(MilkGivers):

    def __init__(self, name, weight, speech='Мууу', animal_type='Корова'):
        super().__init__(name, weight, speech)
        self.animal_type = animal_type


class Goat(MilkGivers):

    def __init__(self, name, weight, speech='Меее', animal_type='Коза'):
        super().__init__(name, weight, speech)
        self.animal_type = animal_type


class Sheep(Animal):

    def __init__(self, name, weight, speech='Беее', animal_type='Овца'):
        super().__init__(name, weight, speech)
        self.animal_type = animal_type

    def cut(self):
        print(f'Овца {self.name} была подстрижена')


goose_grey = Goose('Серый', 12)
goose_white = Goose('Белый', 11)
cow_manka = Cow('Манька', 270)
sheep_barash = Sheep('Барашек', 150)
sheep_curly = Sheep('Кудрявый', 135)
chicken_koko = Chicken('Ко-Ко', 4)
chicken_kykareky = Chicken('Кукареку', 3)
goat_roga = Goat('Рога', 70)
goat_kopyta = Goat('Копыта', 65)
duck_kryakva = Duck('Кряква', 9)

Animal_list = [goose_grey, goose_white, cow_manka, sheep_barash, sheep_curly, chicken_koko, chicken_kykareky, goat_roga, goat_kopyta, duck_kryakva]

for element in Animal_list:
    element.eat(2)
