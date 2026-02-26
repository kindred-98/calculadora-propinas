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
├── README.md
├── .gitignore
├── requirements.txt
│
├── src/
│   └── calculadora_propinas.py
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

---

## 🧪 Casos de Prueba Recomendados

- Monto negativo.
- Porcentaje negativo.
- Propina fija negativa.
- Número de personas = 0.
- Entradas no numéricas.
- Montos grandes.
- Porcentajes altos (ej. 200%).

---

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









