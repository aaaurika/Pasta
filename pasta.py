from abc import ABC, abstractmethod

class Pasta(ABC):
    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_sauce(self):
        pass

    @abstractmethod
    def get_filling(self):
        pass

    @abstractmethod
    def get_additives(self):
        pass

class Spaghetti(Pasta):
    def get_type(self):
        return "Спагетти"

    def get_sauce(self):
        return "Томатный соус"

    def get_filling(self):
        return "Курица"

    def get_additives(self):
        return ["Сыр", "Чеснок"]

class Capellini(Pasta):
    def get_type(self):
        return "Капеллини"

    def get_sauce(self):
        return "Томатный соус"

    def get_filling(self):
        return "Курица"

    def get_additives(self):
        return ["Пармезан", "Петрушка"]

class Bukatini(Pasta):
    def get_type(self):
        return "Букатини"

    def get_sauce(self):
        return "Песто соус"

    def get_filling(self):
        return "Мясо"

    def get_additives(self):
        return ["Анчоусы", "Томаты"]

class PastaBuilder(ABC):
    @abstractmethod
    def build_type(self):
        pass

    @abstractmethod
    def build_sauce(self):
        pass

    @abstractmethod
    def build_filling(self):
        pass

    @abstractmethod
    def build_additives(self):
        pass

    @abstractmethod
    def get_pasta(self):
        pass

class SpaghettiBuilder(PastaBuilder):
    def __init__(self):
        self.pasta = Spaghetti()

    def build_type(self):
        self.pasta.type = self.pasta.get_type()

    def build_sauce(self):
        self.pasta.sauce = self.pasta.get_sauce()

    def build_filling(self):
        self.pasta.filling = self.pasta.get_filling()

    def build_additives(self):
        self.pasta.additives = self.pasta.get_additives()

    def get_pasta(self):
        return self.pasta

class CapelliniBuilder(PastaBuilder):
    def __init__(self):
        self.pasta = Capellini()

    def build_type(self):
        self.pasta.type = self.pasta.get_type()

    def build_sauce(self):
        self.pasta.sauce = self.pasta.get_sauce()

    def build_filling(self):
        self.pasta.filling = self.pasta.get_filling()

    def build_additives(self):
        self.pasta.additives = self.pasta.get_additives()

    def get_pasta(self):
        return self.pasta

class BukatiniBuilder(PastaBuilder):
    def __init__(self):
        self.pasta = Bukatini()

    def build_type(self):
        self.pasta.type = self.pasta.get_type()

    def build_sauce(self):
        self.pasta.sauce = self.pasta.get_sauce()

    def build_filling(self):
        self.pasta.filling = self.pasta.get_filling()

    def build_additives(self):
        self.pasta.additives = self.pasta.get_additives()

    def get_pasta(self):
        return self.pasta

class PastaDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_pasta(self):
        self.builder.build_type()
        self.builder.build_sauce()
        self.builder.build_filling()
        self.builder.build_additives()
        return self.builder.get_pasta()

class PastaFactory(ABC):
    def create_builder(self):
        pass

    def create_pasta(self):
        builder = self.create_builder()
        director = PastaDirector(builder)
        return director.construct_pasta()

class SpaghettiFactory(PastaFactory):
    def create_builder(self):
        return SpaghettiBuilder()

class CapelliniFactory(PastaFactory):
    def create_builder(self):
        return CapelliniBuilder()

class BukatiniFactory(PastaFactory):
    def create_builder(self):
        return BukatiniBuilder()

class PastaClient:
    def __init__(self, factory):
        self.factory = factory

    def prepare_pasta(self):
        pasta = self.factory.create_pasta()
        print(f"Сейчас мы приготовим {pasta.get_type()} с {pasta.get_sauce()}")
        print(f"Добавим в нее {', '.join(pasta.get_additives())}")
        print(f"А в качестве начинки положим {pasta.get_filling()}")
        return pasta

if __name__ == "__main__":
    spaghetti_for_vasya = PastaClient(SpaghettiFactory())
    capellini_for_petya = PastaClient(CapelliniFactory())
    bukatini_for_vova = PastaClient(BukatiniFactory())

    print("ГОТОВИМ ДЛЯ ВАСИ")
    spaghetti_for_vasya.prepare_pasta()
    print("-----------------")
    print("ГОТОВИМ ДЛЯ ПЕТИ")
    capellini_for_petya.prepare_pasta()
    print("-----------------")
    print("ГОТОВИМ ДЛЯ ВОВЫ")
    bukatini_for_vova.prepare_pasta()
