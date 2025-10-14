import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.view import interfaz_liquidador_gui
interfaz_liquidador_gui.LiquidadorNominaApp().run()