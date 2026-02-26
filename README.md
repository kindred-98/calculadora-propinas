![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python)
![Pytest](https://img.shields.io/badge/Testing-pytest-green?style=for-the-badge&logo=pytest)
![Clean Code](https://img.shields.io/badge/Code-Clean-blueviolet?style=for-the-badge)
![CLI](https://img.shields.io/badge/Interface-CLI-lightgrey?style=for-the-badge)
![GUI](https://img.shields.io/badge/Interface-GUI-yellow?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)

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

### **Inicio de Interfaz Gráfica (GUI)**
1) Creación de la clase TipCalculatorGUI.
2) Implementación de ventana principal con tkinter.
3) Campos de entrada para:
    - Monto total
    - Tipo de propina (porcentaje o fija)
    - Valor de la propina
    - Número de personas
4) Botón de cálculo conectado a la lógica existente.
5) Separación clara entre lógica (services.py) y presentación (gui.py).

### **Separación de Capas y Modularización**
1) Creación de estructura modular dentro de src/:
    - services.py → lógica de negocio.
    - utils.py → utilidades (formateo de moneda).
    - validators.py → validaciones.   
    - menu.py → interfaz en terminal (CLI).
    - gui.py → interfaz gráfica.
2) Implementación de arquitectura más escalable.
3) Separación clara entre:
    - Lógica
    - Validaciones
    - Presentación
4) Mejora en mantenibilidad del código.

### **Historial de Cálculos**
1) Implementación de Treeview (ttk) para mostrar historial.
2) Cada cálculo se almacena en tabla con:
    - Monto
    - Propina
    - Total
    - Total por persona
3) Mejora de experiencia de usuario.

### **Visualización con Gráfico**
1) Integración de matplotlib con tkinter.
2) Implementación de gráfico circular (pie chart).
3) Visualización de:
   - Monto base
   - Propina
4) Actualización dinámica del gráfico tras cada cálculo.
5) Integración mediante FigureCanvasTkAgg.

### **Selector de Modo (CLI / GUI)**
1) Creación de main.py como punto de entrada principal.
2) Detección automática de entorno:
   - Si hay consola → menú CLI/GUI.
   - Si no hay consola → apertura directa de GUI.
3) Posibilidad de ejecutar:
4) Modo Terminal.
5) Modo Gráfico.
6) Mejora en flexibilidad del programa.

### **Ejecutable (.exe)**
1) Generación de ejecutable mediante PyInstaller.
2) Compatibilidad con modo --windowed.
3) Ajustes para evitar errores silenciosos.
4) Aplicación ejecutable sin necesidad de entorno Python instalado.

### **Refactorización y Documentación Interna**

1) Añadido de docstrings en:
    - GUI
    - Entry points
    - Funciones principales
4) Mejora de legibilidad.
5) Añadido de type hints.
6) Limpieza de estructura sin alterar funcionalidad.
7) Código preparado para portfolio profesional.

## Casos de Prueba Recomendados

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

1) Cobertura de pruebas
Se añadieron tests para:

- Funciones de servicios (dividir_cuenta)
- Funciones de utilidades (formatear_moneda)
- Validadores de entrada
- Casos edge (valores negativos, cero, entradas inválidas)
- Manejo correcto de excepciones (ValueError)

2) Estructura de testing
calculadora-propinas/
```
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
```

3) Cómo ejecutar los tests
Desde la raíz del proyecto: python -m pytest o simplemente: pytest

## Objetivo Educativo

Este proyecto forma parte de un ejercicio práctico para aprender:

- Programación modular en Python.
- Buenas prácticas de validación.
- Control de versiones con Git.
- Documentación técnica.
- Uso responsable y crítico de herramientas de IA.

---

## 📜 Licencia MIT

Proyecto educativo. Uso libre para aprendizaje.









