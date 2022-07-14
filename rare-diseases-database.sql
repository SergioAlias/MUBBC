--------------------------------
---- RARE DISEASES DATABASE ----
--------------------------------
-- Sergio Alías Segura, 20211028


-------------------
-- CREATE TABLES --
-------------------

-- DROP TABLE Paciente
-- DROP TABLE Enfermedad
-- DROP TABLE Mutación
-- DROP TABLE Caso
-- DROP TABLE Tratamiento
-- DROP TABLE Casopaciente


CREATE TABLE Paciente
    (
    id_paciente INT PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL,
    apellido_1 VARCHAR(20) NOT NULL,
    apellido_2 VARCHAR(20),
    ano_nacimiento DECIMAL(4),
    genero CHAR(1) CONSTRAINT genero_invalido CHECK ((genero = 'M') OR (genero = 'F')),
    ciudad VARCHAR(30),
    provincia VARCHAR(30),
    pais VARCHAR(15)
    );

CREATE TABLE Enfermedad
    (
    id_enfermedad INT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    nombre_abrev VARCHAR(10),
    descripcion VARCHAR(100)
    );

CREATE TABLE Mutacion
    (
    id_mutacion INT PRIMARY KEY,
    gen VARCHAR(40),
    gen_abrev VARCHAR(10),
    autosoma SMALLINT CONSTRAINT autosoma_inexistente CHECK ((0 < autosoma) AND (autosoma < 23)),
    crom_sexual CHAR(1) CONSTRAINT crom_sexual_inexistente CHECK ((crom_sexual = 'X') OR (crom_sexual = 'Y')),
    efecto VARCHAR(100)
    );

CREATE TABLE Caso
    (
    id_caso INT PRIMARY KEY,
    id_enfermedad INT REFERENCES Enfermedad,
    id_mutacion INT REFERENCES Mutacion
    );

CREATE TABLE Tratamiento
    (
    id_tratamiento INT PRIMARY KEY,
    id_caso INT REFERENCES Caso,
    nombre VARCHAR(40),
    descripcion VARCHAR(100)
    );

CREATE TABLE Casopaciente
    (
    id_casopaciente INT PRIMARY KEY,
    id_caso INT REFERENCES Caso,
    id_paciente INT REFERENCES Paciente,
    ano_registro DECIMAL(4)
    );


-------------
-- INSERTS --
-------------

INSERT INTO Paciente VALUES (1, 'Juan', 'Belmonte', 'García', 1994, 'M', 'Armilla', 'Granada', 'España');
INSERT INTO Paciente VALUES (2, 'María José', 'Trujillo', 'del Bosque', 2004, 'F', 'Zaidín', 'Huesca', 'España');
INSERT INTO Paciente VALUES (3, 'Adrien', 'Moreau', NULL, 1983, 'M', 'Montpellier', 'Occitania', 'Francia');
INSERT INTO Paciente VALUES (4, 'Bruno', 'Silveira', 'Santos', 2003, 'M', 'Madeira', 'Región Autónoma de Madeira', 'Portugal');
INSERT INTO Paciente VALUES (5, 'Angustias', 'Montesinos', 'García', 1955, 'F', 'La Maya', 'Salamanca', 'España');
INSERT INTO Paciente VALUES (6, 'Basilio', 'Herrera', 'Bueno', 1942, 'M', 'Roquetas de Mar', 'Almería', 'España');
INSERT INTO Paciente VALUES (7, 'Victoria', 'Ocaña', 'Castro', 1984, 'F', 'Arjona', 'Jaén', 'España');
INSERT INTO Paciente VALUES (8, 'Antonio', 'del Olmo', 'Fraile', 1971, 'M', 'Haro', 'La Rioja', 'España');
INSERT INTO Paciente VALUES (9, 'Carmen', 'Pina', 'Morilla', 2002, 'F', 'Consuegra', 'Toledo', 'España');
INSERT INTO Paciente VALUES (10, 'Juliana', 'Pereira', 'Sousa', 1996, 'F', 'Oporto', 'Distrito de Oporto', 'Portugal');
INSERT INTO Paciente VALUES (11, 'Ildefonso', 'Zabala', 'Alonso', 1990, 'M', 'Mahora', 'Albacete', 'España');
INSERT INTO Paciente VALUES (12, 'Macarena', 'Sanz', 'Luna', 2001, 'F', 'Badajoz', 'Badajoz', 'España');
INSERT INTO Paciente VALUES (13, 'Juan Pablo', 'Reyes', 'Rodríguez', 1986, 'M', 'Laredo', 'Cantabria', 'España');
INSERT INTO Paciente VALUES (14, 'Ismael', 'Cantón', 'Ramos', 1998, 'M', 'Pizarra', 'Málaga', 'España');
INSERT INTO Paciente VALUES (15, 'Dolores', 'Fuertes', 'de Cabeza', 1951, 'M', 'Punta Umbría', 'Huelva', 'España');


INSERT INTO Enfermedad VALUES (1, 'Distrofia muscular de Duchenne', 'DMD', 'Debilidad muscular progresiva desde la infancia');
INSERT INTO Enfermedad VALUES (2, 'Distrofia muscular de Becker', 'BMD', 'Debilidad muscular de piernas y pelvis');
INSERT INTO Enfermedad VALUES (3, 'Albinismo oculocutáneo tipo 1 subtipo A', 'OCA1A', 'Ausencia de melanina en piel, pelo y ojos');
INSERT INTO Enfermedad VALUES (4, 'Albinismo oculocutáneo tipo 1 subtipo B', 'OCA1B', 'Reducción de melanina en piel, pelo y ojos');
INSERT INTO Enfermedad VALUES (5, 'Albinismo oculocutáneo tipo 2', 'OCA2', 'Reducción de melanina, visión reducida, queratosis solar');
INSERT INTO Enfermedad VALUES (6, 'Síndrome X frágil', 'FXS', 'Retrasos en el desarrollo y discapacidades del aprendizaje');
INSERT INTO Enfermedad VALUES (7, 'Síndrome de Moebius', 'MBS', 'Parálisis facial no progresiva y alteración de la abducción ocular de uno o ambos ojos');
INSERT INTO Enfermedad VALUES (8, 'Esclerosis lateral amiotrófica', 'ELA', 'Problemas de movimiento y control muscular');
INSERT INTO Enfermedad VALUES (9, 'Síndrome de Prader-Willi', 'PWS', 'Amplia variedad de síntomas, incluidos retrasos de desarrollo y obesidad');
INSERT INTO Enfermedad VALUES (10, 'Síndrome de Angelman', 'AS', 'Retraso en el desarrollo, problemas de habla y equilibrio, discapacidad intelectual y convulsiones');


INSERT INTO Mutacion VALUES (1, 'Gen de la distrofina', 'Xp21', NULL, 'X', 'Distrofina alterada o no funcional'); -- Duchenne y Becker
INSERT INTO Mutacion VALUES (2, 'Gen de la tirosinasa', 'TYR', 11, NULL, 'Interrupcción ruta de síntesis de melanina'); -- OCA1A y OCA1B
INSERT INTO Mutacion VALUES (3, 'Oculocutaneous albinism type 2', 'OCA2', 15, NULL, 'Se altera el pH de los melanosomas'); -- OCA2
INSERT INTO Mutacion VALUES (4, 'Fragile X Mental Retardation 1', 'FMR1', NULL, 'X', 'Ausencia de proteína FMRP, necesaria para el desarrollo del cerebro'); -- FXS
INSERT INTO Mutacion VALUES (5, 'Plexin D1', 'PLXND1', 3, NULL, 'Se altera la migración de los nervios durante el revelado del cerebro'); -- Moebius (I)
INSERT INTO Mutacion VALUES (6, 'Protein Reversionless 3-Like', 'REV3L', 6, NULL, 'Se pierde protección frente a daños en el DNA'); -- Moebius (II)
INSERT INTO Mutacion VALUES (7, 'Chromosome 9 open reading frame 72', 'C9ORF72', 9, NULL, 'Se altera la función de los terminales presinápticos'); -- ELA
INSERT INTO Mutacion VALUES (8, 'Región 15q11-q13', '15q11-q13', 15, NULL, 'Fallo en el imprinting'); -- PWS y AS


INSERT INTO Caso VALUES (1, 1, 1); -- Duchenne
INSERT INTO Caso VALUES (2, 2, 1); -- Becker
INSERT INTO Caso VALUES (3, 3, 2); -- OCA1A
INSERT INTO Caso VALUES (4, 4, 2); -- OCA1B
INSERT INTO Caso VALUES (5, 5, 3); -- OCA2
INSERT INTO Caso VALUES (6, 6, 4); -- FXS
INSERT INTO Caso VALUES (7, 7, 5); -- Moebius (I)
INSERT INTO Caso VALUES (8, 7, 6); -- Moebius (II)
INSERT INTO Caso VALUES (9, 8, 7); -- ELA
INSERT INTO Caso VALUES (10, 9, 8); -- PWS
INSERT INTO Caso VALUES (11, 10, 8); -- AS


INSERT INTO Tratamiento VALUES (1, 1, 'Glucocorticoides', 'Aumentan la fuerza muscular y la función respiratoria, y retardan la progresión de la debilidad'); -- Duchenne
INSERT INTO Tratamiento VALUES (2, 1, 'Anticonvulsivos', 'Ayudan a controlar las convulsiones y algunos espasmos musculares'); -- Duchenne
INSERT INTO Tratamiento VALUES (3, 1, 'Inmunosupresores', 'Retrasan el daño de las células musculares moribundas'); -- Duchenne
INSERT INTO Tratamiento VALUES (4, 1, 'Salto de exón', 'Se produce distrofina funcional saltando la parte del gen que causa problemas'); -- Duchenne
INSERT INTO Tratamiento VALUES (5, 2, 'Terapia física', 'Ayuda a mejorar el movimiento, postura y a aliviar el dolor'); -- Becker
INSERT INTO Tratamiento VALUES (6, 2, 'Terapia celular', 'Tratamiento de mioblastos o uso de células madre'); -- Becker
INSERT INTO Tratamiento VALUES (7, 2, 'Betabloqueantes', 'Actúan contra la presión arterial alta y la insuficiencia cardíaca'); -- Becker
INSERT INTO Tratamiento VALUES (8, 7, 'Cirugía de reanimación facial', 'Transferencia de un músculo funcional libre'); -- Moebius (I)
INSERT INTO Tratamiento VALUES (9, 8, 'Corrección quirúrgica del estrabismo', 'Recesión de ambos rectos medios con respecto al limbo esclerocorneal'); -- Moebius (II)
INSERT INTO Tratamiento VALUES (10, 9, 'Riluzol', 'Aumento de la esperanza de vida de tres a seis meses'); -- ELA
INSERT INTO Tratamiento VALUES (11, 9, 'Edaravone', 'Reduce la disminución del funcionamiento diario'); -- ELA
INSERT INTO Tratamiento VALUES (12, 10, 'Hormona del crecimiento humana', 'Acelera el crecimiento, mejora el tono muscular y reduce la grasa corporal'); -- PWS
INSERT INTO Tratamiento VALUES (13, 10, 'Terapia de reemplazo hormonal', 'Repone los niveles bajos de hormonas sexuales'); -- PWS
INSERT INTO Tratamiento VALUES (14, 11, 'Medicamentos anticonvulsivos', 'Controlan las convulsiones'); -- AS
INSERT INTO Tratamiento VALUES (15, 11, 'Fisioterapia', 'Ayuda con los problemas para caminar y moverse'); -- AS


INSERT INTO Casopaciente VALUES (1, 6, 1, 1997);
INSERT INTO Casopaciente VALUES (2, 8, 1, 1996);
INSERT INTO Casopaciente VALUES (3, 5, 2, 2004);
INSERT INTO Casopaciente VALUES (4, 2, 3, 1983);
INSERT INTO Casopaciente VALUES (5, 5, 3, 1983);
INSERT INTO Casopaciente VALUES (6, 11, 4, 2003);
INSERT INTO Casopaciente VALUES (7, 1, 4, 2004);
INSERT INTO Casopaciente VALUES (8, 10, 5, 1955);
INSERT INTO Casopaciente VALUES (9, 2, 5, 1958);
INSERT INTO Casopaciente VALUES (10, 7, 6, 1942);
INSERT INTO Casopaciente VALUES (11, 4, 7, 1984);
INSERT INTO Casopaciente VALUES (12, 10, 7, 1984);
INSERT INTO Casopaciente VALUES (13, 2, 7, 1986);
INSERT INTO Casopaciente VALUES (14, 3, 8, 1971);
INSERT INTO Casopaciente VALUES (15, 1, 9, 2002);
INSERT INTO Casopaciente VALUES (16, 5, 9, 2003);
INSERT INTO Casopaciente VALUES (17, 9, 10, 2015);
INSERT INTO Casopaciente VALUES (18, 9, 11, 2008);
INSERT INTO Casopaciente VALUES (19, 7, 11, 1994);
INSERT INTO Casopaciente VALUES (20, 1, 12, 2001);
INSERT INTO Casopaciente VALUES (21, 4, 12, 2002);
INSERT INTO Casopaciente VALUES (22, 3, 13, 1986);
INSERT INTO Casopaciente VALUES (23, 5, 14, 1998);
INSERT INTO Casopaciente VALUES (24, 2, 14, 1999);
INSERT INTO Casopaciente VALUES (25, 11, 15, 1951);
INSERT INTO Casopaciente VALUES (26, 8, 15, 1952);


-------------
-- QUERIES --
-------------

-- Query 1: Ver el nombre completo y lugar de procedencia de los pacientes que no son españoles

SELECT nombre, apellido_1, apellido_2, ciudad, provincia, pais
FROM Paciente
WHERE Pais NOT LIKE 'España';

-- Query 2: Ordenar a los pacientes anteriores según su edad (de mayor a menor edad)

SELECT ano_nacimiento, nombre, apellido_1, apellido_2, ciudad, provincia, pais
FROM Paciente
WHERE Pais NOT LIKE 'España'
ORDER BY ano_nacimiento ASC;

-- Query 3: Ordenar a todos los pacientes según su número de casos

CREATE VIEW Tabla_num_casos AS
SELECT id_paciente, COUNT(*) as num_casos
FROM Casopaciente
GROUP BY id_paciente;

SELECT nombre, apellido_1, apellido_2, num_casos
FROM Paciente NATURAL INNER JOIN Tabla_num_casos
ORDER BY num_casos DESC;

-- Query 4: Igual que la anterior, pero solamente pacientes andaluces (usa la misma view)

CREATE VIEW Tabla_num_casos AS
SELECT id_paciente, COUNT(*) as num_casos
FROM Casopaciente
GROUP BY id_paciente;

SELECT nombre, apellido_1, apellido_2, provincia, num_casos
FROM Paciente NATURAL INNER JOIN Tabla_num_casos
WHERE provincia LIKE 'Almería' OR provincia LIKE 'Granada' OR provincia LIKE 'Cádiz' OR provincia LIKE 'Málaga' OR provincia LIKE 'Jaén' OR provincia LIKE 'Córdoba' OR provincia LIKE 'Sevilla' OR provincia LIKE 'Huelva'
ORDER BY num_casos DESC;

-- Query 5: Edad que tenían los pacientes cuando registraron sus casos, de mayor a menor

SELECT Paciente.nombre, Apellido_1, Apellido_2, Enfermedad.nombre, (ano_registro-ano_nacimiento) AS edad_cuando_registro
FROM Paciente NATURAL INNER JOIN Casopaciente NATURAL INNER JOIN Caso, Enfermedad
WHERE Caso.id_enfermedad = Enfermedad.id_enfermedad
ORDER BY (ano_registro-ano_nacimiento) DESC;

-- Query 6: Casos (enfermedades) registrados antes del año 2000, con el nombre del paciente

SELECT Paciente.nombre, apellido_1, apellido_2, Enfermedad.nombre, ano_registro
FROM Enfermedad NATURAL INNER JOIN Caso NATURAL INNER JOIN Casopaciente, Paciente
WHERE ano_registro < 2000 AND Casopaciente.id_paciente = Paciente.id_paciente
ORDER BY ano_registro;

-- Query 7: Nombre y descripción de las enfermedades causadas por mutaciones localizadas en el cromosoma 15

SELECT nombre, descripcion
FROM Enfermedad NATURAL INNER JOIN Caso NATURAL INNER JOIN Mutacion
WHERE autosoma = 15;

-- Query 8: Tratamientos disponibles para cada una de las enfermedades anteriores (No aparecen tratamientos para el Albinismo oculocutáneo tipo 2 porque el albinismo no tiene trtatamiento)

SELECT Enfermedad.nombre AS enfermedad, Tratamiento.nombre AS tratamiento, Tratamiento.descripcion
FROM Tratamiento, Enfermedad NATURAL INNER JOIN Caso NATURAL INNER JOIN Mutacion
WHERE Mutacion.autosoma = 15 AND Tratamiento.id_caso = Caso.id_caso;

-- Query 9: Lo mismo para mutaciones localizadas en el cromosoma X (El Síndrome X Frágil no aparece porque no tiene tratamientos conocidos)

SELECT Enfermedad.nombre AS enfermedad, Tratamiento.nombre AS tratamiento, Tratamiento.descripcion
FROM  Tratamiento, Enfermedad NATURAL INNER JOIN Caso NATURAL INNER JOIN Mutacion
WHERE Mutacion.crom_sexual = 'X' AND Tratamiento.id_caso = Caso.id_caso;

-- Query 10: Ver nombre completo y tipo de albinismo de los pacientes que lo presenten

CREATE VIEW Casos_albinismo AS
SELECT *
FROM Paciente NATURAL INNER JOIN Casopaciente NATURAL INNER JOIN Caso
WHERE id_caso IN
	(SELECT id_caso
	FROM Enfermedad NATURAL INNER JOIN Caso
	WHERE Enfermedad.nombre LIKE 'Alb%'
	);

SELECT Casos_albinismo.nombre, Casos_albinismo.apellido_1, Casos_albinismo.apellido_2, Enfermedad.nombre
FROM Enfermedad, Casos_albinismo
WHERE Casos_albinismo.id_enfermedad = Enfermedad.id_enfermedad;

-- Query 10.5: Una forma más compacta de hacer lo anterior sin crear view

SELECT Paciente.nombre, Paciente.apellido_1, Paciente.apellido_2, Enfermedad.nombre
FROM Enfermedad, Paciente NATURAL INNER JOIN Casopaciente NATURAL INNER JOIN Caso
WHERE Caso.id_enfermedad = Enfermedad.id_enfermedad AND id_caso IN
	(SELECT id_caso
	FROM Enfermedad NATURAL INNER JOIN Caso
	WHERE Enfermedad.nombre LIKE 'Alb%'
	);

-- Query 11: Consultar las enfermedades que presentan los pacientes no españoles (los de la primera query)

SELECT Paciente.nombre, apellido_1, apellido_2, pais, Enfermedad.nombre, descripcion
FROM Enfermedad, Paciente NATURAL INNER JOIN Casopaciente NATURAL INNER JOIN Caso
WHERE Pais NOT LIKE 'España' AND Caso.id_enfermedad = Enfermedad.id_enfermedad;

-- Query 12: Lo anterior, pero obviando la descripción de la enfermedad y ordenado por el cromosoma afectado de menor a mayor (siendo el último el X)

SELECT Paciente.nombre, apellido_1, apellido_2, pais, Enfermedad.nombre, Mutacion.autosoma, Mutacion.crom_sexual
FROM Enfermedad, Paciente NATURAL INNER JOIN Casopaciente NATURAL INNER JOIN Caso, Mutacion
WHERE Pais NOT LIKE 'España' AND Caso.id_enfermedad = Enfermedad.id_enfermedad AND Caso.id_mutacion = Mutacion.id_mutacion
ORDER BY Mutacion.autosoma;

-- Query 13: Lo anterior, pero primero que muestre primero a los pacientes franceses, luego a los portugueses y finalmente que añada a los españoles

(SELECT Paciente.nombre, apellido_1, apellido_2, pais, Enfermedad.nombre, Mutacion.autosoma, Mutacion.crom_sexual
FROM Enfermedad, Paciente NATURAL INNER JOIN Casopaciente NATURAL INNER JOIN Caso, Mutacion
WHERE Pais LIKE 'Francia' AND Caso.id_enfermedad = Enfermedad.id_enfermedad AND Caso.id_mutacion = Mutacion.id_mutacion
ORDER BY Mutacion.autosoma)
UNION ALL (SELECT Paciente.nombre, apellido_1, apellido_2, pais, Enfermedad.nombre, Mutacion.autosoma, Mutacion.crom_sexual
FROM Enfermedad, Paciente NATURAL INNER JOIN Casopaciente NATURAL INNER JOIN Caso, Mutacion
WHERE Pais LIKE 'Portugal' AND Caso.id_enfermedad = Enfermedad.id_enfermedad AND Caso.id_mutacion = Mutacion.id_mutacion
ORDER BY Mutacion.autosoma)
UNION ALL (SELECT Paciente.nombre, apellido_1, apellido_2, pais, Enfermedad.nombre, Mutacion.autosoma, Mutacion.crom_sexual
FROM Enfermedad, Paciente NATURAL INNER JOIN Casopaciente NATURAL INNER JOIN Caso, Mutacion
WHERE Pais LIKE 'España' AND Caso.id_enfermedad = Enfermedad.id_enfermedad AND Caso.id_mutacion = Mutacion.id_mutacion
ORDER BY Mutacion.autosoma);


--------------
-- TRIGGERS --
--------------

-------------------------------------------------------
-- Trigger 1: Control del fallecimiento de pacientes --
-------------------------------------------------------

-- Query para comprobar si se ha borrado lo que se tiene que borrar (ver fichero .pdf para más información)

SELECT Paciente.nombre, Paciente.apellido_1, Paciente.apellido_2, Casopaciente.id_casopaciente
FROM Casopaciente NATURAL INNER JOIN Paciente
WHERE id_paciente = 1;

-- Acción que desencadenará el trigger

DELETE FROM Paciente
WHERE id_paciente=1;

-- El Trigger 1 con su procedimiento:

-- DROP FUNCTION BORRANDO_CASOS() CASCADE;
CREATE FUNCTION BORRANDO_CASOS() RETURNS TRIGGER AS $$
BEGIN
	DELETE FROM Casopaciente
	WHERE Casopaciente.id_paciente = OLD.id_paciente;
	RETURN OLD;
END;
$$ LANGUAGE 'plpgsql';

-- DROP TRIGGER PACIENTE_FALLECE ON Paciente;
CREATE TRIGGER PACIENTE_FALLECE
BEFORE DELETE ON Paciente
FOR EACH ROW EXECUTE PROCEDURE BORRANDO_CASOS();

--------------------------------
-- Trigger 2: Caso erradicado --
--------------------------------

-- Query de comprobación

SELECT id_tratamiento, id_caso, id_casopaciente
FROM Tratamiento NATURAL INNER JOIN Caso NATURAL INNER JOIN Casopaciente
WHERE id_caso = 1;

-- Acción que desencadenará el trigger

DELETE FROM Caso
WHERE id_caso=1;

-- El Trigger 2 con su procedimiento:

-- DROP FUNCTION BORRANDO_REFERENCIAS_AL_CASO() CASCADE;
CREATE FUNCTION BORRANDO_REFERENCIAS_AL_CASO() RETURNS TRIGGER AS $$
BEGIN
	DELETE FROM Casopaciente
	WHERE Casopaciente.id_caso = OLD.id_caso;
    DELETE FROM Tratamiento
    WHERE Tratamiento.id_caso = OLD.id_caso;
	RETURN OLD;
END;
$$ LANGUAGE 'plpgsql';

-- DROP TRIGGER CASO_RECLASIFICADO ON Caso;
CREATE TRIGGER CASO_RECLASIFICADO
BEFORE DELETE ON Caso
FOR EACH ROW EXECUTE PROCEDURE BORRANDO_REFERENCIAS_AL_CASO();