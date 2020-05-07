#2)	Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
#Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
#Реализовать общий подсчет расхода ткани. Проверить на практике полученные
# на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.
class Textil:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def fabric_coat_cost(self):
        return round(self.width / 6.5 + 0.5)

    def coat_tissue_consum (self):
        return round(self.height * 2 + 0.3)

    @property
    def fabric_area(self):
        return str(f'Площадь общая ткани: {round(self.width/ 6.5 + 0.5) + round(self.height * 2 + 0.3)}')

class Coat(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.area_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь ткани на пальто: {self.area_c}'


class consum(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.area_j = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь ткани на костюм: {self.area_j}'

coat = Coat(2.23, 1.85 )
jacket = consum(1.3, 3)
print(coat)
print(jacket)
print(coat.fabric_area)
print(jacket.fabric_area)
print(f'Расход ткани для пальто: {jacket.fabric_coat_cost()}')
print(f'Расход ткани для костюма: {jacket.coat_tissue_consum()}')