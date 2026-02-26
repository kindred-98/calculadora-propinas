# Calculadora de Propinas  
Proyecto educativo desarrollado en Python para practicar programación, control de versiones con Git y uso de herramientas de IA. La aplicación permite calcular propinas, dividir cuentas entre varias personas y manejar diferentes tipos de propina (porcentaje o monto fijo).

---

## 🎯 Objetivos del Proyecto

- Practicar Git mediante commits incrementales.
- Aprender a interactuar con herramientas de IA para generar y mejorar código.
- Desarrollar funciones modulares y validadas en Python.
- Implementar una interfaz interactiva en terminal.
- Documentar el proceso de asistencia de IA.
- Aplicar buenas prácticas de programación y documentación.

---

## 📁 Estructura del Proyecto

```
calculadora-propinas/
│
├── main.py
├── main_gui.py
├── README.md
├── requirements.txt
│
├── src/
│   ├── gui.py
│   ├── menu.py
│   ├── services.py
│   ├── utils.py
│   ├── validators.py
│
└── docs/
    └── asistencia_ia.md
```

---

## ⚙️ Instalación

1. Clonar el repositorio:
   ```bash
   git clone <URL-del-repositorio>
   ```

2. Crear un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv .venv
   ```

3. Activarlo:
   - Windows:
     ```bash
     .\.venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source .venv/bin/activate
     ```

4. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Ejecución

Ejecutar el archivo principal:

```bash
python src/calculadora_propinas.py
```

---

## 🧩 Funcionalidades Implementadas (Commits 1–7)

### **Commit 1 — Configuración inicial**
- Creación de estructura de carpetas.
- Archivo README inicial.
- `.gitignore` configurado para Python.
- `requirements.txt` creado.
- Repositorio Git inicializado.

### **Commit 2 — Función básica**
- Función para calcular propina fija del 10%.
- Pruebas manuales.

### **Commit 3 — Porcentaje personalizable**
- Función que acepta un porcentaje variable.
- Validación de porcentaje positivo.

### **Commit 4 — División entre personas**
- Función para dividir el total entre varias personas.
- Retorno estructurado mediante diccionario.

### **Commit 5 — Validaciones y manejo de errores**
- Validación de montos, porcentajes y número de personas.
- Manejo de errores con `try/except`.
- Código más robusto y seguro.

### **Commit 6 — Redondeo y formato moneda**
- Redondeo a 2 decimales.
- Función `formatear_moneda()` para mostrar valores como dinero.

### **Commit 7 — Múltiples formas de propina**
- Propina por porcentaje.
- Propina fija.
- Función unificada `calcular_propina()`.

### **Commit 8 MULTIPLES CAMBIOS**

**Inicio de Interfaz Gráfica (GUI)**
-Creación de la clase TipCalculatorGUI.
-Implementación de ventana principal con tkinter.
-Campos de entrada para:
    Monto total
    Tipo de propina (porcentaje o fija)
    Valor de la propina
    Número de personas
-Botón de cálculo conectado a la lógica existente.
-Separación clara entre lógica (services.py) y presentación (gui.py).

**Separación de Capas y Modularización**
-Creación de estructura modular dentro de src/:
    services.py → lógica de negocio.
    utils.py → utilidades (formateo de moneda).
    validators.py → validaciones.   
    menu.py → interfaz en terminal (CLI).
    gui.py → interfaz gráfica.
-Implementación de arquitectura más escalable.
-Separación clara entre:
    Lógica
    Validaciones
    Presentación
-Mejora en mantenibilidad del código.

**Historial de Cálculos**
-Implementación de Treeview (ttk) para mostrar historial.
-Cada cálculo se almacena en tabla con:
    Monto
    Propina
    Total
    Total por persona
-Mejora de experiencia de usuario.

**Visualización con Gráfico**
-Integración de matplotlib con tkinter.
-Implementación de gráfico circular (pie chart).
-Visualización de:
    Monto base
    Propina
-Actualización dinámica del gráfico tras cada cálculo.
-Integración mediante FigureCanvasTkAgg.

**Selector de Modo (CLI / GUI)**
-Creación de main.py como punto de entrada principal.
-Detección automática de entorno:
    Si hay consola → menú CLI/GUI.
    Si no hay consola → apertura directa de GUI.
-Posibilidad de ejecutar:
-Modo Terminal.
-Modo Gráfico.
-Mejora en flexibilidad del programa.

**Ejecutable (.exe)**
-Generación de ejecutable mediante PyInstaller.
-Compatibilidad con modo --windowed.
-Ajustes para evitar errores silenciosos.
-Aplicación ejecutable sin necesidad de entorno Python instalado.

**Refactorización y Documentación Interna**

-Añadido de docstrings en:
    GUI
    Entry points
    Funciones principales
-Mejora de legibilidad.
-Añadido de type hints.
-Limpieza de estructura sin alterar funcionalidad.
-Código preparado para portfolio profesional.

## 🧪 Casos de Prueba Recomendados

- Monto negativo.
- Porcentaje negativo.
- Propina fija negativa.
- Número de personas = 0.
- Entradas no numéricas.
- Montos grandes.
- Porcentajes altos (ej. 200%).

---

### **Commit 9 Testing Automatizado**

Implementacion de pruebas automatizadas utilizando pytest para garantizar la robustez y calidad del proyecto.

📌 Cobertura de pruebas
Se añadieron tests para:

-Funciones de servicios (dividir_cuenta)
-Funciones de utilidades (formatear_moneda)
-Validadores de entrada
-Casos edge (valores negativos, cero, entradas inválidas)
-Manejo correcto de excepciones (ValueError)

Estructura de testing
calculadora-propinas/
│
├── src/
│   ├── services.py
│   ├── utils.py
│   ├── validators.py
│
├── test/
│   ├── test_services.py
│   ├── test_utils.py
│   ├── test_validators.py

Cómo ejecutar los tests
Desde la raíz del proyecto:
python -m pytest o simplemente: pytest

## 📌 Objetivo Educativo

Este proyecto forma parte de un ejercicio práctico para aprender:

- Programación modular en Python.
- Buenas prácticas de validación.
- Control de versiones con Git.
- Documentación técnica.
- Uso responsable y crítico de herramientas de IA.

---

## 📜 Licencia MIT

Proyecto educativo. Uso libre para aprendizaje.









