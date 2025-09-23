import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

from src.model.excepciones import (
    ErrorSalarioBase,
    ErrorDiasLaborados,
    ErrorHorasExtras,
    ErrorHorasExtrasMaximas
)
from src.model.nomina import LiquidadorNomina

class NominaForm(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.inputs = {}

        self.add_widget(Label(text="Liquidador de Nómina", font_size=22, size_hint=(1, 0.2)))

        campos = [
            ("salario_base", "Salario base:"),
            ("dias_laborados", "Días laborados (0-30):"),
            ("horas_extra_diurnas", "Horas extras diurnas:"),
            ("horas_extra_nocturnas", "Horas extras nocturnas:"),
            ("bonificacion", "Bonificación (0 si no hay):")
        ]

        for key, label in campos:
            box = BoxLayout(orientation='horizontal', size_hint=(1, 0.12))
            box.add_widget(Label(text=label, size_hint=(0.6, 1)))
            ti = TextInput(multiline=False, input_filter='float' if key in ['salario_base', 'bonificacion'] else 'int')
            self.inputs[key] = ti
            box.add_widget(ti)
            self.add_widget(box)

        btn = Button(text="Calcular Nómina", size_hint=(1, 0.18))
        btn.bind(on_press=self.calcular_nomina)
        self.add_widget(btn)

    def calcular_nomina(self, instance):
        try:
            salario_base = float(self.inputs["salario_base"].text)
            dias_laborados = int(float(self.inputs["dias_laborados"].text))
            horas_extra_diurnas = int(float(self.inputs["horas_extra_diurnas"].text))
            horas_extra_nocturnas = int(float(self.inputs["horas_extra_nocturnas"].text))
            bonificacion = float(self.inputs["bonificacion"].text)

            liquidador = LiquidadorNomina(
                salario_base,
                dias_laborados,
                horas_extra_diurnas,
                horas_extra_nocturnas,
                bonificacion
            )
            salario_neto = liquidador.liquidar()
            self.mostrar_popup("Resultado", f"Total a pagar (Salario Neto):\n${salario_neto:,.2f}")

        except ValueError:
            self.mostrar_popup("Error", "Debe ingresar valores numéricos.")
        except (ErrorSalarioBase, ErrorDiasLaborados, ErrorHorasExtras, ErrorHorasExtrasMaximas) as e:
            self.mostrar_popup("Error", str(e))
        except Exception as e:
            self.mostrar_popup("Error inesperado", str(e))

    def mostrar_popup(self, titulo, mensaje):
        popup = Popup(title=titulo,
                      content=Label(text=mensaje),
                      size_hint=(0.7, 0.4))
        popup.open()

class LiquidadorNominaApp(App):
    def build(self):
        return NominaForm()

if __name__ == "__main__":
    LiquidadorNominaApp().run()