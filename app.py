from flask import Flask, render_template, request
from src.model.nomina import LiquidadorNomina

app = Flask(__name__)

@app.route('/')
def inicio():
    # Muestra el formulario de cálculo
    return render_template('calc_nomina.html')

@app.route('/nomina/calcular', methods=['POST'])
def calcular_nomina():
    try:
        # Obtener los datos del formulario
        salario_base = float(request.form['salario_base'])
        dias_laborados = int(request.form['dias_laborados'])
        horas_extra_diurnas = int(request.form['horas_extra_diurnas'])
        horas_extra_nocturnas = int(request.form['horas_extra_nocturnas'])
        bonificacion = float(request.form['bonificacion'])

        # Crear el objeto y calcular la nómina
        liquidador = LiquidadorNomina(
            salario_base=salario_base,
            dias_laborados=dias_laborados,
            horas_extra_diurnas=horas_extra_diurnas,
            horas_extra_nocturnas=horas_extra_nocturnas,
            bonificacion=bonificacion
        )

        salario_neto = liquidador.liquidar()

        # Mostrar resultado en pantalla
        return f"<h2>Salario Neto Calculado: ${salario_neto:,.2f}</h2><br><a href='/'>Volver</a>"

    except Exception as e:
        return f"<h3>Error en el cálculo: {str(e)}</h3><br><a href='/'>Volver</a>"

if __name__ == '__main__':
    app.run(debug=True)




