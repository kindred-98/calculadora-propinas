import pytest
from unittest.mock import Mock, MagicMock, patch, call
import tkinter as tk
from src.gui import TipCalculatorGUI


@pytest.fixture
def mock_tk_root():
    """Fixture que proporciona un mock de tk.Tk para evitar crear ventanas reales."""
    root = Mock(spec=tk.Tk)
    root.title = Mock()
    root.geometry = Mock()
    root.resizable = Mock()
    root.configure = Mock()
    return root


@pytest.fixture
def mock_widgets():
    """Fixture que mockea todos los widgets de ttk y tk."""
    with patch('src.gui.ttk.Frame') as mock_frame, \
         patch('src.gui.ttk.Label') as mock_label, \
         patch('src.gui.ttk.Entry') as mock_entry, \
         patch('src.gui.ttk.Button') as mock_button, \
         patch('src.gui.ttk.Radiobutton') as mock_radio, \
         patch('src.gui.ttk.Treeview') as mock_tree, \
         patch('src.gui.ttk.Style') as mock_style, \
         patch('src.gui.tk.StringVar') as mock_stringvar, \
         patch('src.gui.plt.subplots') as mock_subplots, \
         patch('src.gui.FigureCanvasTkAgg') as mock_canvas:
        
        # Configurar mocks básicos
        mock_frame.return_value.pack = Mock()
        mock_label.return_value.pack = Mock()
        mock_entry_instance = Mock()
        mock_entry_instance.pack = Mock()
        mock_entry_instance.get = Mock(return_value="100")
        mock_entry.return_value = mock_entry_instance
        
        mock_button.return_value.pack = Mock()
        mock_radio.return_value.pack = Mock()
        
        mock_tree_instance = Mock()
        mock_tree_instance.heading = Mock()
        mock_tree_instance.column = Mock()
        mock_tree_instance.pack = Mock()
        mock_tree_instance.insert = Mock()
        mock_tree.return_value = mock_tree_instance
        
        mock_style_instance = Mock()
        mock_style_instance.theme_use = Mock()
        mock_style_instance.configure = Mock()
        mock_style.return_value = mock_style_instance
        
        mock_stringvar_instance = Mock()
        mock_stringvar_instance.get = Mock(return_value="porcentaje")
        mock_stringvar.return_value = mock_stringvar_instance
        
        # Mock matplotlib
        mock_fig = Mock()
        mock_ax = Mock()
        mock_ax.clear = Mock()
        mock_ax.pie = Mock()
        mock_ax.set_title = Mock()
        mock_subplots.return_value = (mock_fig, mock_ax)
        
        mock_canvas_instance = Mock()
        mock_canvas_instance.get_tk_widget = Mock(return_value=Mock(pack=Mock()))
        mock_canvas_instance.draw = Mock()
        mock_canvas.return_value = mock_canvas_instance
        
        yield {
            'frame': mock_frame,
            'label': mock_label,
            'entry': mock_entry,
            'button': mock_button,
            'radio': mock_radio,
            'tree': mock_tree,
            'style': mock_style,
            'stringvar': mock_stringvar,
            'subplots': mock_subplots,
            'canvas': mock_canvas,
            'fig': mock_fig,
            'ax': mock_ax,
            'canvas_instance': mock_canvas_instance,
            'tree_instance': mock_tree_instance,
            'entry_instance': mock_entry_instance,
            'stringvar_instance': mock_stringvar_instance
        }


def test_inicializar_gui_con_valores_por_defecto(mock_tk_root, mock_widgets):
    """
    Verifica que la GUI se inicializa con los valores por defecto correctos:
    - dark_mode = False
    - historial = []
    """
    gui = TipCalculatorGUI(mock_tk_root)
    
    assert gui.dark_mode is False
    assert gui.historial == []
    assert gui.root == mock_tk_root


def test_configurar_estilos_modo_claro(mock_tk_root, mock_widgets):
    """
    Verifica que los estilos se configuran correctamente en modo claro:
    - Fondo blanco
    - Texto negro
    """
    gui = TipCalculatorGUI(mock_tk_root)
    gui.dark_mode = False
    gui.configurar_estilos()
    
    # Verificar que se configuró el fondo de la ventana
    mock_tk_root.configure.assert_called()
    
    # Verificar que se configuraron los estilos
    style_calls = mock_widgets['style'].return_value.configure.call_args_list
    assert len(style_calls) > 0


def test_configurar_estilos_modo_oscuro(mock_tk_root, mock_widgets):
    """
    Verifica que los estilos se configuran correctamente en modo oscuro:
    - Fondo oscuro (#1e1e1e)
    - Texto blanco
    """
    gui = TipCalculatorGUI(mock_tk_root)
    gui.dark_mode = True
    gui.configurar_estilos()
    
    # Verificar que se configuró el fondo de la ventana con color oscuro
    mock_tk_root.configure.assert_called()
    
    # Verificar que se llamó a configure en el estilo
    style_calls = mock_widgets['style'].return_value.configure.call_args_list
    assert len(style_calls) > 0


def test_crear_widgets_crea_todos_los_componentes(mock_tk_root, mock_widgets):
    """
    Verifica que se crean todos los widgets necesarios:
    - Etiquetas, entradas, botones, radiobuttons
    - Tabla de historial (Treeview)
    - Gráfico (matplotlib)
    """
    gui = TipCalculatorGUI(mock_tk_root)
    
    # Verificar que se crearon los Entry widgets
    assert mock_widgets['entry'].call_count >= 3  # monto, valor, personas
    
    # Verificar que se creó el Treeview
    mock_widgets['tree'].assert_called_once()
    
    # Verificar que se creó el gráfico
    mock_widgets['subplots'].assert_called_once()
    mock_widgets['canvas'].assert_called_once()


def test_actualizar_grafico_con_distribucion_correcta(mock_tk_root, mock_widgets):
    """
    Verifica que el gráfico circular se actualiza con la distribución correcta
    entre monto base y propina.
    """
    gui = TipCalculatorGUI(mock_tk_root)
    
    monto = 100.0
    propina = 15.0
    
    gui.actualizar_grafico(monto, propina)
    
    # Verificar que se limpió el gráfico anterior
    mock_widgets['ax'].clear.assert_called_once()
    
    # Verificar que se llamó a pie con los valores correctos
    mock_widgets['ax'].pie.assert_called_once()
    call_args = mock_widgets['ax'].pie.call_args
    assert call_args[0][0] == [monto, propina]  # valores
    
    # Verificar que se estableció el título
    mock_widgets['ax'].set_title.assert_called_once_with("Distribución del Pago")
    
    # Verificar que se redibujó el canvas
    mock_widgets['canvas_instance'].draw.assert_called_once()


@patch('src.gui.dividir_cuenta')
@patch('src.gui.formatear_moneda')
def test_calcular_con_propina_porcentaje(mock_formatear, mock_dividir, mock_tk_root, mock_widgets):
    """
    Verifica que el cálculo funciona correctamente con propina por porcentaje:
    - Lee los valores de entrada
    - Llama a dividir_cuenta con los parámetros correctos
    - Actualiza el historial
    - Actualiza el gráfico
    """
    gui = TipCalculatorGUI(mock_tk_root)
    
    # Configurar mocks de entrada
    gui.monto_entry.get = Mock(return_value="100")
    gui.valor_entry.get = Mock(return_value="15")
    gui.personas_entry.get = Mock(return_value="2")
    gui.tipo_var.get = Mock(return_value="porcentaje")
    
    # Configurar respuesta de dividir_cuenta
    mock_dividir.return_value = {
        "propina": 15.0,
        "total": 115.0,
        "por_persona": 57.5
    }
    
    # Configurar formatear_moneda
    mock_formatear.side_effect = lambda x: f"${x:.2f}"
    
    gui.calcular()
    
    # Verificar que se llamó a dividir_cuenta con los parámetros correctos
    mock_dividir.assert_called_once_with(100.0, "porcentaje", 15.0, 2)
    
    # Verificar que se insertó en el historial
    mock_widgets['tree_instance'].insert.assert_called_once()
    
    # Verificar que se llamó a formatear_moneda
    assert mock_formatear.call_count == 4  # monto, propina, total, por_persona


@patch('src.gui.dividir_cuenta')
@patch('src.gui.formatear_moneda')
def test_calcular_con_propina_fija(mock_formatear, mock_dividir, mock_tk_root, mock_widgets):
    """
    Verifica que el cálculo funciona correctamente con propina fija:
    - Lee los valores de entrada
    - Llama a dividir_cuenta con tipo 'fija'
    - Actualiza el historial y gráfico
    """
    gui = TipCalculatorGUI(mock_tk_root)
    
    # Configurar mocks de entrada
    gui.monto_entry.get = Mock(return_value="200")
    gui.valor_entry.get = Mock(return_value="25")
    gui.personas_entry.get = Mock(return_value="4")
    gui.tipo_var.get = Mock(return_value="fija")
    
    # Configurar respuesta de dividir_cuenta
    mock_dividir.return_value = {
        "propina": 25.0,
        "total": 225.0,
        "por_persona": 56.25
    }
    
    # Configurar formatear_moneda
    mock_formatear.side_effect = lambda x: f"${x:.2f}"
    
    gui.calcular()
    
    # Verificar que se llamó a dividir_cuenta con tipo 'fija'
    mock_dividir.assert_called_once_with(200.0, "fija", 25.0, 4)
    
    # Verificar que se insertó en el historial
    mock_widgets['tree_instance'].insert.assert_called_once()


@patch('src.gui.messagebox.showerror')
@patch('src.gui.dividir_cuenta')
def test_manejar_valor_error_de_entrada_invalida(mock_dividir, mock_showerror, mock_tk_root, mock_widgets):
    """
    Verifica que se maneja correctamente un ValueError cuando la entrada es inválida:
    - Muestra un mensaje de error apropiado
    - No actualiza el historial ni el gráfico
    """
    gui = TipCalculatorGUI(mock_tk_root)
    
    # Configurar entrada inválida
    gui.monto_entry.get = Mock(return_value="abc")  # No es un número
    gui.valor_entry.get = Mock(return_value="15")
    gui.personas_entry.get = Mock(return_value="2")
    gui.tipo_var.get = Mock(return_value="porcentaje")
    
    gui.calcular()
    
    # Verificar que se mostró un mensaje de error
    mock_showerror.assert_called_once()
    assert mock_showerror.call_args[0][0] == "Error de entrada"
    
    # Verificar que NO se insertó en el historial
    mock_widgets['tree_instance'].insert.assert_not_called()


@patch('src.gui.messagebox.showerror')
@patch('src.gui.dividir_cuenta')
@patch('src.gui.formatear_moneda')
def test_manejar_excepcion_inesperada(mock_formatear, mock_dividir, mock_showerror, mock_tk_root, mock_widgets):
    """
    Verifica que se maneja correctamente una excepción inesperada:
    - Muestra un mensaje de error genérico
    - No interrumpe la aplicación
    """
    gui = TipCalculatorGUI(mock_tk_root)
    
    # Configurar entrada válida
    gui.monto_entry.get = Mock(return_value="100")
    gui.valor_entry.get = Mock(return_value="15")
    gui.personas_entry.get = Mock(return_value="2")
    gui.tipo_var.get = Mock(return_value="porcentaje")
    
    # Configurar dividir_cuenta para lanzar una excepción inesperada
    mock_dividir.side_effect = RuntimeError("Error inesperado")
    
    gui.calcular()
    
    # Verificar que se mostró un mensaje de error genérico
    mock_showerror.assert_called_once()
    assert mock_showerror.call_args[0][0] == "Error inesperado"
    assert "error interno" in mock_showerror.call_args[0][1].lower()


@patch('src.gui.dividir_cuenta')
@patch('src.gui.formatear_moneda')
def test_agregar_resultados_a_tabla_historial(mock_formatear, mock_dividir, mock_tk_root, mock_widgets):
    """
    Verifica que los resultados calculados se agregan correctamente a la tabla de historial:
    - Los valores se formatean correctamente
    - Se insertan en el orden correcto (Monto, Propina, Total, Por Persona)
    """
    gui = TipCalculatorGUI(mock_tk_root)
    
    # Configurar mocks de entrada
    gui.monto_entry.get = Mock(return_value="150")
    gui.valor_entry.get = Mock(return_value="20")
    gui.personas_entry.get = Mock(return_value="3")
    gui.tipo_var.get = Mock(return_value="porcentaje")
    
    # Configurar respuesta de dividir_cuenta
    mock_dividir.return_value = {
        "propina": 30.0,
        "total": 180.0,
        "por_persona": 60.0
    }
    
    # Configurar formatear_moneda para retornar valores específicos
    mock_formatear.side_effect = ["$150.00", "$30.00", "$180.00", "$60.00"]
    
    gui.calcular()
    
    # Verificar que se insertó en el Treeview con los valores correctos
    mock_widgets['tree_instance'].insert.assert_called_once()
    call_args = mock_widgets['tree_instance'].insert.call_args
    
    # Verificar el orden de los valores
    valores = call_args[1]['values']
    assert valores == ("$150.00", "$30.00", "$180.00", "$60.00")
