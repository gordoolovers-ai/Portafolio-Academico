/*querys ejemplo clase 06-08-2024*/
-- Ejemplo sentencia SELECT

select *
from persona;

select nombre as "NOMBRE_PERSONA", apellido1 "APELLIDO_MATERNO", APELLIDO2 "Apellido_Paterno", fecha_nacimiento
from persona
order by apellido1, apellido2, nombre;

---OPERADOR LIKE
select nombre as "NOMBRE_PERSONA", apellido1 "APELLIDO_MATERNO", APELLIDO2 "Apellido_Paterno", fecha_nacimiento
from persona
WHERE nombre like 'A%'
order by apellido1, apellido2, nombre;

select nombre as "NOMBRE_PERSONA", apellido1 "APELLIDO_MATERNO", APELLIDO2 "Apellido_Paterno", fecha_nacimiento
from persona
where fecha_nacimiento between date '1990-01-01' and date '1996-12-31' 
order by apellido1, apellido2, nombre;

-- uso calificadores para tablas
select p.nombre as "NOMBRE_PERSONA", p.apellido1 "APELLIDO_MATERNO", p.APELLIDO2 "Apellido_Paterno", p.fecha_nacimiento,
year (curdate())-year(p.fecha_nacimiento) ANIOS_CUMPLIDOS_EDAD
from persona p
where fecha_nacimiento between date '1990-01-01' and date '1996-12-31' 
order by apellido1, apellido2, nombre;

desc persona;

-- Ejemplo Funciones de GRUPO
select max(fecha_nacimiento),min(fecha_nacimiento)
from persona;

SELECT id_departamento, COUNT(id_profesor) AS total_profesores
FROM profesor
GROUP BY id_departamento
ORDER BY 1;

-- Ejemplo de funciones de grupo filtrando con HAVING
SELECT id_departamento, COUNT(id_profesor) AS total_profesores
FROM profesor
GROUP BY id_departamento
HAVING COUNT(id_profesor)>=2
ORDER BY 1;
-- el query más grande sintacticamente
SELECT ASIG.TIPO, count(ASIG.TIPO) 
FROM ASIGNATURA ASIG
where asig.cuatrimestre=2
group by ASIG.TIPO
having count(ASIG.TIPO) >12
order by 1;

SELECT * FROM ASIGNATURA where tipo='optativa' and cuatrimestre=2;
desc ASIGNATURA;

-- EJEMPLO NATURAL JOIN
select *
from profesor natural join  departamento
order by 1;

-- EJEMPLO JOIN
select p.id_profesor,p.id_departamento, b.nombre,b.curso,pe.nombre AS "NOMBRE_PROF",pe.apellido1,pe.apellido2
from persona pe inner join profesor p on (pe.id=p.id_profesor) 
inner join asignatura b on (p.id_profesor=b.id_profesor)
where b.curso=1
order by 1,2;

desc asignatura;

-- EJEMPLO LEFT JOIN
select p.id_profesor,p.id_departamento,pe.nombre AS "NOMBRE_PROF",pe.apellido1,pe.apellido2
from persona pe inner join profesor p on (pe.id=p.id_profesor) 
order by 1,2;

select p.id_profesor,p.id_departamento,pe.nombre AS "NOMBRE_PROF",pe.apellido1,pe.apellido2
from persona pe left join profesor p on (pe.id=p.id_profesor) 
order by 1,2;

-- EJEMPLO RIGHT JOIN
select p.id_profesor,p.id_departamento,pe.nombre AS "NOMBRE_PROF",pe.apellido1,pe.apellido2
from persona pe right join profesor p on (pe.id=p.id_profesor) 
order by 1,2;

-- CROSS JOIN o producto cartesiano
select p.id_profesor,p.id_departamento,pe.nombre AS "NOMBRE_PROF",pe.apellido1,pe.apellido2
from persona pe, profesor p 
order by 1,2;

-- EJEMPLOS DE JOINS SIMPLIFICADO
select id_profesor 
from persona p, profesor pr
where p.id=pr.id_profesor;

-- EJEMPLOS DE SUBQUERYS
select *
from asignatura
where id_profesor = (select id_profesor from persona p, profesor pr
where p.id=pr.id_profesor
and nombre='Manolo');

-- EJEMPLO INSERT
INSERT INTO asignatura (id,nombre,creditos,tipo,curso,cuatrimestre,id_profesor,id_grado) values (84,'CIENCIA DE DATOS',6,'obligatoria',3,2,null,7);
INSERT INTO asignatura (nombre,creditos,tipo,curso,cuatrimestre,id_profesor,id_grado,id) values ('CIENCIA DE DATOS',6,'obligatoria',3,2,null,7,86);
-- EJEMPLO DELETE
delete from asignatura where id=84;
commit;
-- EJEMPLO TRUNCATE
truncate table departamento;