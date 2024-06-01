
class Vegetable():
    def __init__(self, name, water_supply, nutrient_supply, light_supply):
        self.name = name
        self.water_supply = water_supply
        self.nutrient_supply = nutrient_supply
        self.light_supply = light_supply

    def print_info(self):
        print('Вид образца:', self.name)
        print('Обеспеченность водой: ', self.water_supply)
        print('Обеспеченность питательными веществами:', self.nutrient_supply)
        print('Обеспеченность светом: ', self.light_supply)


class Assistant:
    samples = []
    count = 0

    def __init__(self, name, job_title):
        self.name = name
        self.job_title = job_title

    def print_info(self):
        print('Имя:', self.name)
        print('Должность:', self.job_title)

    def watering_sample(self, sample1):
        if sample1 not in self.samples:
            sample1.water_supply += 1
            self.samples.append(sample1)

    def fertilizer_sample(self, sample2):
        if sample2 not in self.samples:
            sample2.nutrient_supply += 1
            self.samples.append(sample2)

    def additional_light(self, sample3):
        if sample3 not in self.samples:
            sample3.light_supply += 1
            self.samples.append(sample3)

    def attestation_of_laboranrt_half2(self):
        self.count = 0
        for i in self.samples:
            if i.water_supply >= 10 and i.nutrient_supply >= 10 and i.light_supply >= 10:
                self.count += 1
            else:
                print('Результат: образец погиб\n')

        if len(self.samples) == self.count:
            print('Прошёл аттестацию и допущен до работы с настоящими опытными образцами')
        else:
            print('Не прошёл аттестацию. Отправляется на пересдачу')



Totmato = Vegetable('totmato', 10, 10, 10)

Axmet = Assistant('Ахмет', 'лошара')

Axmet.print_info()

Potato = Vegetable('potato', 11, 11, 11)

Axmet.watering_sample(Potato)

Axmet.fertilizer_sample(Potato)

Axmet.additional_light(Potato)

Axmet.watering_sample(Totmato)

Axmet.fertilizer_sample(Totmato)

Axmet.additional_light(Totmato)

Axmet.attestation_of_laboranrt_half2()
