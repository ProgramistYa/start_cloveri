"""
1. Предложите описание используемых таблиц в базе данных, включая информацию о названиях и формате полей.
"""

from django.db import models


# работал на Django 3, на Flask не пробовал.


class Doctors(models.Model):
    doctor_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=155)
    location_id = models.ForeignKey(Locations, on_delete=models.CASCADE)


def __str__(self):
    return self.name


# models.CASCADE – при удалении записи из первичной модели (у нас это таблица Doctors) происходит удаление
# всех записей из вторичной модели (Locations), связанных с удаляемой категорией;

class Locations(models.Model):
    location_id = models.IntegerField(primary_key=True)
    doctor_id = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    latitude = models.FloatField(blank=True, null=True)
    # blank = Если True, поле может быть пустым
    # null Если True, Django будет хранить пустые значения как NULL в базе данных.
    longitude = models.FloatField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)


class Routes(models.Model):
    route_id = models.IntegerField(primary_key=True)
    doctor_id = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    start_location_id = models.ForeignKey(Locations, on_delete=models.CASCADE)
    end_location_id = models.ForeignKey(Locations, on_delete=models.CASCADE)
    distance = models.FloatField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)


"""
2.Предложите индексы для каждой из таблиц, которые помогут быстрее выдавать информацию по идентификатору врача

Для таблицы "Врачи" можно создать следующий индекс:
Индекс по полю "идентификатор врача"

Таблица "Местонахождения врачей":
Индекс по полю "Идентификатор врача"

Таблица "Маршруты врачей":
Индекс по полю "Идентификатор врача" (если требуется поиск по врачу)
Индекс по полю "Место прибытия" (если требуется поиск по месту прибытия)
Индекс по полю "Место отправления" (если требуется поиск по месту отправления)

Разумеется, выбор индексов и их организация зависит от конкретных требований и особенностей работы с базой данных.
"""
