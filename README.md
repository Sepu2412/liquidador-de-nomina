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

Documentación para la ejecución del programa y pruebas unitarias
Pasos para ejecutar el programa main.py desde la terminal de Windows:
Abrir la terminal de Windows:
Presiona Win + R, escribe cmd y presiona Enter.
Navegar al directorio del proyecto:
Utiliza el comando cd para cambiar al directorio donde se encuentra el archivo main.py. Por ejemplo:
cd d:\Documentos\Programación\Proyectos\Liquidador-de-Nomina
Ejecutar el programa:
Una vez en el directorio correcto, ejecuta el programa con el siguiente comando:
python src/view/interfaz-liquidador.py
Pasos para ejecutar las pruebas unitarias test_nomina.py:
Abrir la terminal de Windows:
Presiona Win + R, escribe cmd y presiona Enter.
Navegar al directorio del proyecto:
Utiliza el comando cd para cambiar al directorio donde se encuentra el archivo test_nomina.py. Por ejemplo:
cd d:\Documentos\Programación\Proyectos Pycharm\Liquidador de Nomina\Liquidador-de-Nomina
Ejecutar las pruebas unitarias:
Asegúrate de tener unittest disponible. Es parte de la biblioteca estándar de Python, por lo que no necesitas instalar nada adicional.
Una vez en el directorio correcto, ejecuta las pruebas unitarias con el siguiente comando:
python test/test.py
unittest buscará y ejecutará las pruebas definidas en test_nomina.py y mostrará los resultados en la terminal.
Arquitectura del Proyecto
El proyecto está organizado en una estructura de carpetas que facilita la separación de responsabilidades y la mantenibilidad del código. A continuación se describe la organización de los módulos y las bibliotecas utilizadas:

Estructura de Carpetas
Liquidador-de-Nomina/
│
├── src/
│   ├── model/
│   │   ├── nomina.py
│   │   ├── excepciones.py
│   │   
│   ├── view/
│   |    ├── interfaz-liquidador.py
│   |        
│   |        
|   |
│   └── __init__.py
│   
│
├── test/
│   ├── test.py
│   └── __init__.py
│
├── archivos/
├       ├── ── Liquidador-Nómina-casos.xlsx
├       ├── ── audios
|       ├── ── txt
|
├── README.md
└── requirements.txt

Descripción de Carpetas y Archivos
src/: Contiene el código fuente del proyecto.
model/: Incluye la lógica de negocio y las clases principales.
calculo_nomina.py: Contiene la clase Nomina y las funciones para calcular el salario, horas extras, bonificaciones, etc.
excepciones.py: Define las excepciones personalizadas utilizadas en el proyecto.
view/: Contiene las interfaces de usuario.

test/: Contiene las pruebas unitarias.
test.py: Incluye las pruebas unitarias para la clase Nomina y sus métodos.
README.md: Documentación del proyecto.
txt: Lista de dependencias y bibliotecas necesarias para ejecutar el proyecto.
Bibliotecas Usadas
unittest: Biblioteca estándar de Python para realizar pruebas unitarias.
sys: Biblioteca estándar de Python para manipular el entorno de ejecución.
Dependencias
El proyecto no tiene dependencias externas adicionales a las bibliotecas estándar de Python. Todas las funcionalidades se implementan utilizando las bibliotecas estándar y el código propio del proyecto(por el momento).

Organización de Módulos
model: Contiene la lógica y las clases.
view: Contiene las interfaces de usuario, en este caso, una interfaz de consola.
test: Contiene las pruebas unitarias para asegurar la calidad del código.
Esta organización modular permite una fácil extensión y mantenimiento del proyecto, asegurando que cada componente tenga una responsabilidad clara y definida.




David Garcia Villanueva 
Tomas Sepulveda Giraldo
