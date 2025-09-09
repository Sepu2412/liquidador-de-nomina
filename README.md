# liquidador-de-nomina
link audio : https://udemedellin-my.sharepoint.com/:f:/r/personal/tsepulveda913_soyudemedellin_edu_co/Documents/codigo%20limpio?csf=1&web=1&e=cBmg2h
# Autores:
David Garcia 
Tomas Sepulveda 

# 💼 Liquidador de Nómina

## 📋 Descripción del Proyecto

Este proyecto tiene como objetivo desarrollar un **Liquidador de Nómina**, una herramienta capaz de calcular automáticamente los pagos que un empleador debe realizar a sus trabajadores, teniendo en cuenta diversos factores como el salario base, horas extras, descuentos legales, prestaciones sociales, entre otros.


## 🎯 Objetivos

- Automatizar el proceso de cálculo de nómina para empleados.
- Implementar fórmulas y reglas legales relacionadas con salarios, prestaciones y deducciones.
- Generar reportes detallados de liquidación por empleado y por periodo.
- Diseñar una interfaz amigable para ingresar y visualizar información.

## ⚙️ Funcionalidades Principales

- Cálculo de salario mensual (proporcional si aplica).
- Registro de horas extras, recargos nocturnos y festivos.
- Deducciones legales: salud, pensión, fondo de solidaridad.
- Prestaciones sociales: prima, cesantías, intereses de cesantías, vacaciones.
- Generación de comprobante de pago (PDF/Excel).
- Administración de empleados y configuración de parámetros salariales.


## Variables de Entrada

Datos Base del Empleado:
salario_base (numérico, varía por cargo): Salario mensual base del empleado.
auxilio_transporte (numérico, según ley vigente): Auxilio de transporte, determinado por la ley actual.
cargo (texto, determina salario y bonificaciones): Cargo o puesto del empleado, utilizado para determinar su salario base y bonificaciones.
horarios (lista de días/horas laborales): Información de los días y horas laborales del empleado.
horas_extras (cantidad y tipo: diurnas/nocturnas/festivas): Detalles de horas extras trabajadas, clasificados según el tipo (diurnas, nocturnas, festivas).
Deducciones:

prestamos (monto, cuotas, tasa de interés 6%): Préstamos del empleado, indicando el monto, el número de cuotas y la tasa de interés (6% anual).
Variables de Salida
salario_neto: Salario del empleado después de aplicar las deducciones y bonos.
desglose_pago: Detalle de las horas extras, bonos, auxilio de transporte y deducciones.
reporte_legal: Reporte con el cumplimiento de las normativas laborales en el cálculo de la liquidación.

## 📤 Variables de Salida

salario_neto (numérico):
Valor total que recibe el empleado después de aplicar deducciones legales, descuentos y sumar bonificaciones o auxilios correspondientes.

desglose_pago (objeto/detalle):
Detalle completo del cálculo de nómina, incluyendo:

Salario base.

Horas extras (diurnas, nocturnas, festivas).

Recargos.

Auxilio de transporte.

Deducciones (salud, pensión, fondo de solidaridad, préstamos).

Bonificaciones (si aplican).


## Documentación para la ejecución del programa y pruebas unitarias

### Pasos para ejecutar el programa `main.py` desde la terminal de Windows:
 ## 📥 Clonar el Repositorio

Antes de ejecutar el programa o realizar pruebas, clona este repositorio en tu máquina local:

git clone https://github.com/usuario/Liquidador-de-Nomina.git


Reemplaza la URL con la correcta si es diferente.

1. ## Abrir la terminal de Windows

Presiona Win + R, escribe cmd y presiona Enter.

2. ## Navegar al directorio del proyecto

Utiliza el comando cd para acceder al directorio donde clonaste el repositorio. Por ejemplo:

cd d:\Documentos\Programación\Proyectos\Liquidador-de-Nomina

3. ## Ejecutar el programa

Desde la raíz del proyecto, ejecuta:

python src/view/console/main.py

### Pasos para ejecutar las pruebas unitarias `test_nomina.py`:

1. ## Abrir la terminal de Windows

Presiona Win + R, escribe cmd y presiona Enter.

2. ## Navegar al directorio del proyecto

Accede a la raíz del repositorio clonado:

cd d:\Documentos\Programación\Proyectos\Liquidador-de-Nomina

3. ## Ejecutar las pruebas

Ejecuta el siguiente comando para correr las pruebas unitarias con unittest:

python -m unittest test/test.py


unittest detectará y ejecutará las pruebas definidas en test.py, mostrando los resultados en la terminal.

## Requisitos

Python 3.7 o superior

Sistema operativo: Windows

No se requieren librerías externas adicionales (solo unittest, incluido en la biblioteca estándar de Python)



David Garcia Villanueva 
Tomas Sepulveda Giraldo
