
<div align="center"> 

# 💰 Calculadora de Propinas

**Calculadora de propinas y división de cuentas desarrollada en Python**  
*CLI + GUI · Arquitectura modular · Testing automatizado · Ejecutable .exe*

---

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Pytest](https://img.shields.io/badge/Testing-pytest-2ea44f?style=for-the-badge&logo=pytest&logoColor=white)](https://pytest.org)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-yellow?style=for-the-badge&logo=python&logoColor=white)](https://docs.python.org/3/library/tkinter.html)
[![Matplotlib](https://img.shields.io/badge/Charts-Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white)](https://matplotlib.org)
[![Clean Code](https://img.shields.io/badge/Code-Clean-blueviolet?style=for-the-badge)](https://github.com/kindred-98)
[![CLI](https://img.shields.io/badge/Interface-CLI-lightgrey?style=for-the-badge)](https://github.com/kindred-98)
[![GUI](https://img.shields.io/badge/Interface-GUI-orange?style=for-the-badge)](https://github.com/kindred-98)
[![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)

</div>

---

## 📌 Índice

- [Descripción](#-descripción)
- [Evolución del proyecto](#-evolución-del-proyecto)
- [Características](#-características)
- [Arquitectura](#-arquitectura-del-proyecto)
- [Instalación](#-instalación)
- [Uso](#️-uso)
- [Testing](#-testing)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Tecnologías](#-tecnologías)
- [Changelog](#-changelog)
- [Autor](#-autor)
- [Licencia](#-licencia)

---

## 📖 Descripción

**Calculadora de Propinas** es una aplicación Python que permite calcular propinas, dividir cuentas entre varias personas y elegir entre propina por porcentaje o monto fijo. Cuenta con dos modos de uso: interfaz de terminal (CLI) e interfaz gráfica (GUI) con historial de cálculos y visualización mediante gráfico circular.

El proyecto fue construido con foco en:

- 🏗️ **Arquitectura modular** — separación clara entre lógica, validaciones, utilidades y presentación
- 🖥️ **Doble interfaz** — CLI para terminal y GUI con tkinter, seleccionables desde el punto de entrada
- 🧪 **Testing automatizado** — suite con pytest cubriendo servicios, utilidades y validadores
- 📦 **Ejecutable standalone** — generado con PyInstaller, no requiere Python instalado
- 📐 **Separación de responsabilidades** — cada módulo tiene un único propósito

---

## 🔄 Evolución del proyecto

El proyecto creció de forma incremental a lo largo de 9 commits documentados:

| Etapa | Descripción |
|---|---|
| **v0.1 — Función básica** | `calcular_propina()` con porcentaje fijo del 10%. Pruebas manuales. |
| **v0.2 — Porcentaje variable** | Porcentaje personalizable con validación de valor positivo. |
| **v0.3 — División entre personas** | División del total con retorno estructurado en diccionario. |
| **v0.4 — Validaciones** | Validación de montos, porcentajes y número de personas con `try/except`. |
| **v0.5 — Formato moneda** | Redondeo a 2 decimales y función `formatear_moneda()`. |
| **v0.6 — Propina unificada** | Función única `calcular_propina()` que acepta porcentaje o monto fijo. |
| **v0.7 — Modularización + GUI** | Separación en capas (`services`, `validators`, `utils`, `menu`, `gui`). Interfaz gráfica con tkinter, historial en Treeview y gráfico circular con matplotlib. Selector CLI/GUI en `main.py`. |
| **v0.8 — Ejecutable** | Generación de `.exe` con PyInstaller en modo `--windowed`. |
| **v1.0 — Testing automatizado** | Suite pytest para servicios, utilidades, validadores y casos edge. |

---

## 🚀 Características

| Funcionalidad | Descripción | Estado |
|---|---|---|
| Propina por porcentaje | Cálculo con porcentaje personalizable | ✅ |
| Propina fija | Monto fijo independiente del porcentaje | ✅ |
| División entre personas | Total por persona con retorno estructurado | ✅ |
| Validaciones completas | Montos, porcentajes, personas y entradas no numéricas | ✅ |
| Formato moneda | Redondeo y presentación como valor monetario | ✅ |
| Interfaz CLI | Menú interactivo en terminal | ✅ |
| Interfaz GUI | Ventana tkinter con campos de entrada | ✅ |
| Historial de cálculos | Tabla Treeview con operaciones previas | ✅ |
| Gráfico circular | Visualización base vs propina con matplotlib | ✅ |
| Selector de modo | Detección automática CLI/GUI desde `main.py` | ✅ |
| Ejecutable .exe | Standalone generado con PyInstaller | ✅ |
| Testing automatizado | Suite pytest con casos edge y excepciones | ✅ |

---

## 🧠 Arquitectura del proyecto

```
┌────────────────────────────────────────────────────────────────┐
│                    Calculadora de Propinas                     │
│                                                                │
│  ┌─────────────────┐        ┌──────────────────────────────┐   │
│  │    main.py      │        │           src/               │   │
│  │                 │        │                              │   │
│  │  Detecta        │───────►│  menu.py     → CLI           │   │
│  │  entorno        │        │  gui.py      → GUI tkinter   │   │
│  │  CLI / GUI      │        └──────────────────────────────┘   │
│  └─────────────────┘                     │                     │
│                                          ▼                     │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                    Capa de lógica                        │  │
│  │                                                          │  │
│  │  services.py   → calcular_propina · dividir_cuenta       │  │
│  │  validators.py → validación de entradas                  │  │
│  │  utils.py      → formatear_moneda · redondeo             │  │
│  └──────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────┘
```

---

## 📦 Instalación

### Requisitos previos

- Python 3.12 o superior
- pip

### Pasos

**1. Clonar el repositorio:**

```bash
git clone https://github.com/kindred-98/calculadora-propinas.git
cd calculadora-propinas
```

**2. Crear entorno virtual:**

```bash
python -m venv .venv
```

**3. Activar entorno:**

```bash
# Windows
.venv\Scripts\activate

# Linux / Mac
source .venv/bin/activate
```

**4. Instalar dependencias:**

```bash
pip install -r requirements.txt
```

---

## ▶️ Uso

### Modo terminal (CLI)

```bash
python main.py
```

Si hay consola disponible, se presentará un menú para elegir entre CLI y GUI.

### Modo gráfico directo

```bash
python main_gui.py
```

### Ejecutable standalone

Si descargaste el `.exe` generado con PyInstaller, simplemente ejecútalo sin necesidad de tener Python instalado.

---

## 🧪 Testing

El proyecto incluye una suite de tests automatizados con **pytest**.

**Ejecutar todos los tests:**

```bash
pytest
```

**Con salida detallada:**

```bash
python -m pytest -v
```

**Módulos cubiertos:**

| Módulo | Qué se prueba |
|---|---|
| `test_services.py` | `calcular_propina`, `dividir_cuenta` |
| `test_utils.py` | `formatear_moneda`, redondeo |
| `test_validators.py` | Entradas inválidas, valores negativos, cero |

**Casos edge cubiertos:**

- Monto negativo
- Porcentaje negativo o mayor a 100%
- Número de personas igual a 0
- Entradas no numéricas
- Montos muy grandes
- Manejo correcto de `ValueError`

---

## 📂 Estructura del proyecto

```
calculadora-propinas/
│
├── main.py                   # Punto de entrada — selector CLI / GUI
├── main_gui.py               # Apertura directa de GUI
├── requirements.txt
├── .gitignore
├── README.md
│
├── src/
│   ├── services.py           # Lógica de negocio: calcular y dividir
│   ├── validators.py         # Validación de entradas del usuario
│   ├── utils.py              # Formateo de moneda y redondeo
│   ├── menu.py               # Interfaz de terminal (CLI)
│   └── gui.py                # Interfaz gráfica con tkinter
│
├── test/
│   ├── test_services.py
│   ├── test_utils.py
│   └── test_validators.py
│
└── docs/
    └── asistencia_ia.md      # Documentación del uso de IA
```

---

## 🛠 Tecnologías

| Tecnología | Uso |
|---|---|
| [Python 3.12+](https://python.org) | Lenguaje principal |
| [Tkinter](https://docs.python.org/3/library/tkinter.html) | Interfaz gráfica |
| [Matplotlib](https://matplotlib.org) | Gráfico circular de resultados |
| [Pytest](https://pytest.org) | Testing automatizado |
| [PyInstaller](https://pyinstaller.org) | Generación de ejecutable .exe |

---

## 📋 Changelog

### v1.0.0

- ✅ Suite de testing con pytest — servicios, utilidades y validadores
- ✅ Cobertura de casos edge y manejo de excepciones

### v0.8.0

- ✅ Ejecutable `.exe` generado con PyInstaller en modo `--windowed`
- ✅ Compatibilidad sin entorno Python instalado

### v0.7.0

- ✅ Arquitectura modular: `services`, `validators`, `utils`, `menu`, `gui`
- ✅ Interfaz gráfica con tkinter — campos de entrada y botón de cálculo
- ✅ Historial de cálculos en tabla Treeview
- ✅ Gráfico circular con matplotlib integrado en la ventana
- ✅ Selector automático CLI/GUI en `main.py`
- ✅ Docstrings, type hints y limpieza de código

### v0.6.0

- ✅ Función unificada `calcular_propina()` — porcentaje o monto fijo

### v0.5.0

- ✅ Redondeo a 2 decimales y función `formatear_moneda()`

### v0.4.0

- ✅ Validaciones completas con `try/except`

### v0.3.0

- ✅ División de cuenta entre personas con retorno en diccionario

### v0.2.0

- ✅ Porcentaje personalizable con validación de valor positivo

### v0.1.0

- ✅ Función `calcular_propina()` básica con porcentaje fijo del 10%

---

<div align="center"> 

## 👨‍💻 Autor

**A.D.E.V.**

*Proyecto educativo del Módulo 2 — Estrategias de Generación de Código con IA · Dicampus*  
*Enfocado en programación modular, testing automatizado y evolución incremental de software.*

[![GitHub](https://img.shields.io/badge/GitHub-kindred--98-181717?style=for-the-badge&logo=github)](https://github.com/kindred-98)

---

## 📜 Licencia

Este proyecto está distribuido bajo la licencia **MIT**.

---

*Hecho con 💰 Python, tkinter y arquitectura incremental*

⭐ Si este proyecto te resulta útil, considera dejarle una estrella en GitHub

</div>