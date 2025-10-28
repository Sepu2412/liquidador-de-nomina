from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 🔹 Ruta principal: redirige automáticamente a /nomina/calcular
@app.route("/")
def inicio():
    return redirect(url_for("calcular_nomina"))

# 🔹 Ruta del formulario y cálculo
@app.route("/nomina/calcular", methods=["GET", "POST"])
def calcular_nomina():
    if request.method == "POST":
        nombre = request.form["nombre"]
        cargo = request.form["cargo"]
        salario_base = float(request.form["salario_base"])
        horas_extras = float(request.form["horas_extras"])
        dias_trabajados = int(request.form["dias_trabajados"])
        bonificaciones = float(request.form["bonificaciones"])

        valor_hora = salario_base / 240
        pago_horas_extras = horas_extras * valor_hora * 1.25
        salario_proporcional = (salario_base / 30) * dias_trabajados
        total_pagar = salario_proporcional + pago_horas_extras + bonificaciones

        return f"""
        <h3>Resultado de Nómina</h3>
        <p><b>Empleado:</b> {nombre}</p>
        <p><b>Cargo:</b> {cargo}</p>
        <p><b>Total a pagar:</b> ${total_pagar:,.2f}</p>
        """

    return render_template("calc_nomina.html")


if __name__ == "__main__":
    app.run(debug=True)
