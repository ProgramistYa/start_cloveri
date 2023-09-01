/* 4. Напишите SQL-запрос, который выведет информацию о врачах, которые в последние 10 минут переместились более чем на 1 км.*/


select *
from doctors
where distance_moved > 1
and last_seen >= NOW() - interval 10 minute

--TIMESTAMPDIFF ?? (unit, datetime1, datetime2)
--Возвращает разницу между двумя DATE или DATETIME в конкретной единице измерения


/* 5. Напишите SQL-запрос, который выведет всех врачей, для которых нет информации об их перемещениях за последний час*/

select *
from doctors as d
where not exists (
  select 1
  from movements as m
  where m.doctor_id = d.id
    and m.last_seen > DATE_SUB(NOW(), interval 1 hour)
);

--В данном запросе мы выбираем все строки из таблицы doctors, где для каждого
--врача не существует записи в таблице movements с указанным doctor_id и
--временной меткой last_seen, больше текущего времени минус 1 час.