class Goose:

    def __init__(self, name, weight, speech='Га-Га-Га'):
        self.name = name
        self.weight = weight
        self.speech = speech

    def eat(self, food):
        self.weight += food
        print(f'Гусь {self.name} был покормлен {food} кг корма')

    def gather_eggs(self, eggs_count):
        eggs_gathered_count = 0
        eggs_gathered_count += eggs_count
        print(f'У гуся {self.name} собрали {eggs_gathered_count} яиц')

    def voice_definition(self, speech):
        if speech == 'Га-Га-Га':
            print('Это гусь')
        else:
            print('Это не гусь')


goose_grey = Goose('Серый', 12)
# print(goose_grey.name)
# print(goose_grey.weight)
# print(goose_grey.speech)

goose_white = Goose('Белый', 11)


# print(goose_white.name)
# print(goose_white.weight)
# print(goose_white.speech)

class Cow:

    def __init__(self, name, weight, speech='Мууу'):
        self.name = name
        self.weight = weight
        self.speech = speech

    def eat(self, food):
        self.weight += food
        print(f'Корова {self.name} была покормлена {food} кг корма')

    def milk(self):
        print(f'Корова {self.name} подоена')

    def voice_definition(self, speech):
        if speech == 'Мууу':
            print('Это корова')
        else:
            print('Это не корова')


cow_manka = Cow('Манька', 270)


class Sheep:

    def __init__(self, name, weight, speech='Беее'):
        self.name = name
        self.weight = weight
        self.speech = speech

    def eat(self, food):
        self.weight += food
        print(f'Овца {self.name} была покормлена {food} кг корма')

    def cut(self):
        print(f'Овца {self.name} была подстрижена')

    def voice_definition(self, speech):
        if speech == 'Беее':
            print('Это овца')
        else:
            print('Это не овца')


sheep_barash = Sheep('Барашек', 150)
sheep_curly = Sheep('Кудрявый', 135)


class Chicken:

    def __init__(self, name, weight, speech='Ко-Ко-Ко'):
        self.name = name
        self.weight = weight
        self.speech = speech

    def eat(self, food):
        self.weight += food
        print(f'Курица {self.name} была покормлена {food} кг корма')

    def gather_eggs(self, eggs_count):
        eggs_gathered_count = 0
        eggs_gathered_count += eggs_count
        print(f'У курицы {self.name} собрали {eggs_gathered_count} яиц')

    def voice_definition(self, speech):
        if speech == 'Ко-Ко-Ко':
            print('Это курица')
        else:
            print('Это не курица')


chicken_koko = Chicken('Ко-Ко', 4)
chicken_kykareky = Chicken('Кукареку', 3)


class Goat:

    def __init__(self, name, weight, speech='Меее'):
        self.name = name
        self.weight = weight
        self.speech = speech

    def eat(self, food):
        self.weight += food
        print(f'Коза {self.name} была покормлена {food} кг корма')

    def milk(self):
        print(f'Коза {self.name} подоена')

    def voice_definition(self, speech):
        if speech == 'Меее':
            print('Это коза')
        else:
            print('Это не коза')


goat_roga = Goat('Рога', 70)
goat_kopyta = Goat('Копыта', 65)


class Duck:

    def __init__(self, name, weight, speech='Кря'):
        self.name = name
        self.weight = weight
        self.speech = speech

    def eat(self, food):
        self.weight += food
        print(f'Утка {self.name} была покормлена {food} кг корма')

    def gather_eggs(self, eggs_count):
        eggs_gathered_count = 0
        eggs_gathered_count += eggs_count
        print(f'У утки {self.name} собрали {eggs_gathered_count} яиц')

    def voice_definition(self, speech):
        if speech == 'Кря':
            print('Это утка')
        else:
            print('Это не утка')


duck_kryakva = Duck('Кряква', 9)

general_weight = duck_kryakva.weight + goat_kopyta.weight + goat_roga.weight + chicken_kykareky.weight + chicken_koko.weight + sheep_curly.weight\
                 + sheep_barash.weight + cow_manka.weight + goose_grey.weight + goose_white.weight

print(f'Суммарный вес животных = {general_weight}')

max_weight_dict = {duck_kryakva.name: duck_kryakva.weight, goat_kopyta.name: goat_kopyta.weight, goat_roga.name: goat_roga.weight, chicken_kykareky.name: chicken_kykareky.weight, chicken_koko.name: chicken_koko.weight,\
                   sheep_curly.name: sheep_curly.weight, sheep_barash.name: sheep_barash.weight, cow_manka.name: cow_manka.weight, goose_grey.name: goose_grey.weight, goose_white.name: goose_white.weight}

# print(max_weight_dict)

max_weight = 0
for name_dict, weight_dict in max_weight_dict.items():
    if weight_dict > max_weight:
        max_weight = weight_dict
        name_of_max_weight = name_dict

# print(max_weight)
print(f'Самое тяжёлое животное на ферме - {name_of_max_weight}')

max_weight_list = [duck_kryakva.weight, goat_kopyta.weight, goat_roga.weight, chicken_kykareky.weight, chicken_koko.weight, sheep_curly.weight, sheep_barash.weight, cow_manka.weight, goose_grey.weight, goose_white.weight]







