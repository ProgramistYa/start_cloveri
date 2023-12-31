:white_check_mark: Ответы на 1 и 2 задание в models.py    
:white_check_mark: Ответ на 3 задание в Readme.md    
:white_check_mark: Ответ на 4 и 5 в req.sql    


### 3.API на сервере проекта для сохранения местонахождения врача может принимать следующие параметры:
- Идентификатор врача (doctor_id): уникальный идентификатор, который используется 
для идентификации врача в системе.
- Широта (latitude): значение широты местоположения врача. Широта указывает на 
географическую координату места на поверхности Земли, которая находится в 
север-южном направлении.
- Долгота (longitude): значение долготы местоположения врача. Долгота указывает 
на географическую координату места на поверхности Земли, которая находится в
запад-восток направлении.
- Временная метка (timestamp)(last_seen): время, когда было сохранено местоположение врача. 
Это обычно представлено в виде строки, соответствующей определенному формату даты
и времени.
- Дополнительные параметры (необязательные): в зависимости от требований проекта,
также может потребоваться передача дополнительных параметров, таких как идентификатор
клиента, тип местоположения (например, работа, дом, клиника) и другие детали.
- 
 Эти параметры позволяют сохранить информацию о местонахождении врача на сервере,
чтобы ее можно было использовать, например, для отображения на карте врачей,
поиска ближайших врачей к заданному месту или для других целей, связанных с
локализацией врачей в проекте.
