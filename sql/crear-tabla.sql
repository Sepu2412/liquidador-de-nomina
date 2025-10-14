-- Crear la base de datos
CREATE DATABASE liquidador_nomina;

-- Conectarse a la base de datos
\c liquidador_nomina

-- Tabla de empleados
CREATE TABLE empleados (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    cedula VARCHAR(20) UNIQUE,
    fecha_ingreso DATE,
    cargo_id INTEGER REFERENCES cargos(id),
    departamento_id INTEGER REFERENCES departamentos(id),
    salario_base NUMERIC(15,2)
);

-- Tabla de cargos
CREATE TABLE cargos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50)
);

-- Tabla de departamentos
CREATE TABLE departamentos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50)
);

-- Tabla de nóminas
CREATE TABLE nominas (
    id SERIAL PRIMARY KEY,
    empleado_id INTEGER REFERENCES empleados(id),
    fecha DATE,
    salario_bruto NUMERIC(15,2),
    salario_neto NUMERIC(15,2)
);

-- Tabla de deducciones
CREATE TABLE deducciones (
    id SERIAL PRIMARY KEY,
    nomina_id INTEGER REFERENCES nominas(id),
    tipo VARCHAR(50),
    monto NUMERIC(15,2)
);




-- Tabla de devengos
CREATE TABLE devengos (
    id SERIAL PRIMARY KEY,
    nomina_id INTEGER REFERENCES nominas(id),
    tipo VARCHAR(50),
    monto NUMERIC(15,2)
);