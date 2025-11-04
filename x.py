import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

DB_FILE = "nominas.db"

def crear_tabla():
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS nominas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cedula TEXT NOT NULL,
            nombre TEXT NOT NULL,
            salario_base REAL NOT NULL,
            dias_laborados INTEGER NOT NULL,
            horas_extra_diurnas INTEGER NOT NULL,
            horas_extra_nocturnas INTEGER NOT NULL,
            bonificacion REAL NOT NULL,
            salario_neto REAL NOT NULL
        )
        """)
        conn.commit()

def insertar_nomina(cedula, nombre, salario_base, dias_laborados, horas_extra_diurnas, horas_extra_nocturnas, bonificacion, salario_neto):
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute("""
        INSERT INTO nominas (cedula, nombre, salario_base, dias_laborados, horas_extra_diurnas, horas_extra_nocturnas, bonificacion, salario_neto)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (cedula, nombre, salario_base, dias_laborados, horas_extra_diurnas, horas_extra_nocturnas, bonificacion, salario_neto))
        conn.commit()

def buscar_nomina(cedula):
    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.execute("SELECT * FROM nominas WHERE cedula = ?", (cedula,))
        return cur.fetchone()

def calcular_neto(salario_base, dias_laborados, horas_extra_diurnas, horas_extra_nocturnas, bonificacion):
    # Ejemplo de lógica de cálculo
    extra_diurna = horas_extra_diurnas * 1.25 * (salario_base / 30 / 8)
    extra_nocturna = horas_extra_nocturnas * 1.75 * (salario_base / 30 / 8)
    salario = (salario_base / 30 * dias_laborados) + extra_diurna + extra_nocturna + bonificacion
    return salario

@app.route('/', methods=["GET"])
def menu():
    return render_template("calc_nomina.html", vista="menu")

@app.route('/crear_tabla', methods=["GET"])
def ruta_crear_tabla():
    crear_tabla()
    return render_template("calc_nomina.html", vista="mensaje", mensaje="Tabla creada exitosamente.")

@app.route('/insertar', methods=["GET", "POST"])
def ruta_insertar():
    if request.method == "POST":
        cedula = request.form["cedula"]
        nombre = request.form["nombre"]
        salario_base = float(request.form["salario_base"])
        dias_laborados = int(request.form["dias_laborados"])
        horas_extra_diurnas = int(request.form["horas_extra_diurnas"])
        horas_extra_nocturnas = int(request.form["horas_extra_nocturnas"])
        bonificacion = float(request.form["bonificacion"])
        salario_neto = calcular_neto(salario_base, dias_laborados, horas_extra_diurnas, horas_extra_nocturnas, bonificacion)
        insertar_nomina(cedula, nombre, salario_base, dias_laborados, horas_extra_diurnas, horas_extra_nocturnas, bonificacion, salario_neto)
        return render_template("calc_nomina.html", vista="mensaje", mensaje=f"Nomina insertada. Salario Neto: ${salario_neto:,.2f}")
    return render_template("calc_nomina.html", vista="insertar")

@app.route('/buscar', methods=["GET", "POST"])
def ruta_buscar():
    nomina = None
    if request.method == "POST":
        cedula = request.form["cedula"]
        nomina = buscar_nomina(cedula)
    return render_template("calc_nomina.html", vista="buscar", nomina=nomina)

if __name__ == "__main__":
    app.run(debug=True)



















<!DOCTYPE html>
<html>
<head>
    <title>Nóminas Local</title>
</head>
<body>
{% if vista == "menu" %}
    <h1>Menú Nómina</h1>
    <ul>
        <li><a href="/crear_tabla">Crear tabla de nóminas</a></li>
        <li><a href="/insertar">Insertar nómina/calcular salario</a></li>
        <li><a href="/buscar">Buscar nómina por cédula</a></li>
    </ul>
{% elif vista == "insertar" %}
    <h2>Insertar nómina y calcular salario</h2>
    <form method="POST">
        Cedula: <input type="text" name="cedula" required><br>
        Nombre: <input type="text" name="nombre" required><br>
        Salario base: <input type="number" name="salario_base" step="0.01" required><br>
        Días laborados: <input type="number" name="dias_laborados" required><br>
        Horas extra diurnas: <input type="number" name="horas_extra_diurnas" required><br>
        Horas extra nocturnas: <input type="number" name="horas_extra_nocturnas" required><br>
        Bonificación: <input type="number" name="bonificacion" step="0.01" required><br>
        <input type="submit" value="Insertar y calcular">
    </form>
    <a href="/">Volver al menú</a>
{% elif vista == "buscar" %}
    <h2>Buscar nómina</h2>
    <form method="POST">
        Cedula: <input type="text" name="cedula" required>
        <input type="submit" value="Buscar">
    </form>
    {% if nomina %}
        <h3>Resultado:</h3>
        <ul>
            <li>Cédula: {{ nomina[1] }}</li>
            <li>Nombre: {{ nomina[2] }}</li>
            <li>Salario base: {{ nomina[3] }}</li>
            <li>Días laborados: {{ nomina[4] }}</li>
            <li>Horas extra diurnas: {{ nomina[5] }}</li>
            <li>Horas extra nocturnas: {{ nomina[6] }}</li>
            <li>Bonificación: {{ nomina[7] }}</li>
            <li>Salario Neto: <b>${{ "%.2f"|format(nomina[8]) }}</b></li>
        </ul>
    {% elif nomina is not none %}
        <p>No se encontró nómina para esa cédula.</p>
    {% endif %}
    <a href="/">Volver al menú</a>
{% elif vista == "mensaje" %}
    <h2>{{ mensaje }}</h2>
    <a href="/">Volver al menú</a>
{% endif %}
</body>
</html>
