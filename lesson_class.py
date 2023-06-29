import abc

class Poultry(abc.ABC):
    def __init__(self, color, sound, specy):
        self.color = color
        self.sound = sound
        self.specy = specy

    def make_some_noise(self):
        print(f"{self.specy} is making some noise !! {self.sound * 3}")

    def move(self):
        print(f"{self.specy}  move.")

    @abc.abstractmethod
    def eat(self):
        pass

    def hatch(self):
        print(f"{self.specy}  hatch zzz.")

class Duck(Poultry):
    def __init__(self, color, sound):
        super().__init__(color, sound, 'Duck')

    def eat(self):
        print(f"{self.specy} eat vegetable")

    def swim(self):
        print(f"{self.specy}  swim ~")

    def move(self):
        print(f"{self.specy} don't want to move......")

class Chicken(Poultry):
    def __init__(self, color, sound):
        super().__init__(color, sound, "Chicken")

    def eat(self):
        print(f"{self.specy} eat bugs ")

    def moring_call(self, time):
        print(f"{self.sound *3}, It's {time} a.m. now.......")

if __name__ == '__main__':
    duck_1 = Duck('yellow', "ba")
    duck_2 = Duck('black', "ga")
    duck_3 = Duck("White", "gua")
    duck_2.move()

    chicken_1 = Chicken("Brown", "gu")
    chicken_1.move()

