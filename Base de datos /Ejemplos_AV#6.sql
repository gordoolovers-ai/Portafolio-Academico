DELIMITER $$
CREATE FUNCTION CONTAR_PROF_DEPTO (DEPTO_ID INT)
RETURNS INT
BEGIN
DECLARE TOTAL INT;
	SELECT COUNT(id_profesor) INTO TOTAL
    FROM profesoR
    WHERE ID_DEPARTAMENTO=DEPTO_ID;
RETURN TOTAL;
END;

//procedimiento
DELIMITER $$
CREATE procedure u_mod_nif (IN nif_ant varchar(18), IN nif_act varchar(18))
BEGIN
	update persona set nif = nif_act
    where nif=nif_ant;
END;


//TRIGGER
DELIMITER $$
CREATE trigger miTrigger 
BEFORE INSERT 
ON curso_escolar
FOR EACH ROW
BEGIN
	SET NEW.anio_inicio = 2025;
    SET NEW.anio_fin = 2026;
END;

create unique index uk_nif_persona  ON persona (id,nif);

alter table persona drop index uk_nif_persona;

create view MI_VISTA AS 
SELECT  id_profesor, nombre,cuatrimestre, id_grado
FROM profesor NATURAL JOIN asignatura; 

SELECT * FROM MI_VISTA;


/*Para ejecutar las funciones o procedimientos*/
SELECT funcion_nombre(argumentos);

CALL procedimiento_nombre(argumentos);