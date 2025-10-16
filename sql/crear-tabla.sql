-- Script para crear la tabla empleado
CREATE TABLE IF NOT EXISTS empleado (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    cedula VARCHAR(20) UNIQUE NOT NULL,
    fecha_ingreso DATE NOT NULL,
    salario_base NUMERIC(15,2) NOT NULL
);