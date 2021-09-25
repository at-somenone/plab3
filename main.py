# артикул, фирма-производитель, название, количество ядер, тактовая частота, стоимость
class CPU:
    def __init__(self, article, maker, name, cores, freq, price):
        self.article = article
        self.maker = maker
        self.name = name
        self.cores = cores
        self.freq = freq
        self.price = price

    def __str__(self):
        return f"{self.article}: {self.maker} {self.name}, {self.cores}x {self.freq} GHz, {self.price}Ω"


def try_input_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            pass


def add():
    article = input("Введите артикул: ")
    maker = input("Введите производителя: ")
    name = input("Введите название: ")
    cores = try_input_number("Введите кол-во ядер: ")
    freq = try_input_number("Введите частоту: ")
    price = try_input_number("Введите стоимость: ")
    cpus.append(CPU(article, maker, name, cores, freq, price))


def delete():
    index = try_input_number("Введите артикул: ")
    if index < len(cpus):
        cpus.pop(index)
    else:
        print('Данного элемента не существует')


def show():
    print(*cpus, sep='\n')


def search():
    maker = input('Введите производителя')
    found = filter(lambda cpu: cpu.maker == maker, cpus)
    print(*found)


done = False

cpus = []

while not done:
    print("""1. Добавить
2. Удалить
3. Отобразить
4. Поиск
""")
    commands = {
        "1": add,
        "2": delete,
        "3": show,
        "4": search,
    }
    cmd = input()
    if cmd in commands:
        commands[cmd]()
    else:
        done = True
