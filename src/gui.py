import dearpygui.dearpygui as dpg
from cardiac import Cardiac

def setup():
    # Configuración de la interfaz de usuario
    with dpg.window(tag="Primary Window"):
        dpg.add_text("Hello, world")
        dpg.add_button(label="Save")
        dpg.add_input_text(label="string", default_value="Quick brown fox")
        dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

    with dpg.window(label="Example Window"):
        dpg.add_text("Hello, world")
        dpg.add_button(label="Save")
        dpg.add_input_text(label="string", default_value="Quick brown fox")
        dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

    dpg.create_viewport(title='Cardiac Cardboard', width=600, height=300)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("Primary Window", True)

def loop():
    # Bucle principal de la aplicación
    while dpg.is_dearpygui_running():
        # Renderizar el frame
        dpg.render_dearpygui_frame()

def main():
    dpg.create_context()
    setup()
    loop()
    dpg.destroy_context()

if __name__ == "__main__":
    main()