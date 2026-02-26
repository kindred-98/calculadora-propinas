# Registro de asistencia de IA

IA utilizada copilot Y chatgpt

Me ayudo a crear funciones basica, a crear validaciones, creamos formato moneda luego multiples formas de propinas fijas y por porcentaje.

Realizacion de interfa con explicacion de cada bloque de codigo generado, documentacion pero revisado y pedida de forma especifica y estructurada.
Refactorizo el codido aplicando clean code, optimizacion, simplificacion y mejora nomenclaturas.

# Documentación de Asistencia de IA  
Este documento recoge cómo se utilizó la inteligencia artificial durante el desarrollo del proyecto *Calculadora de Propinas*. Se detalla la interacción, las preguntas realizadas y las decisiones tomadas en cada commit.

---

## 🤖 Rol de la IA en el Proyecto

La IA actuó como:

- Asistente técnico para resolver dudas de programación.
- Guía para estructurar el proyecto.
- Revisor de código.
- Generador de ejemplos, funciones y buenas prácticas.
- Apoyo en la documentación y planificación.

El desarrollador (Ángel) mantuvo siempre el control del código, revisando, corrigiendo y adaptando las sugerencias.

---

# 🧩 Asistencia por Commit

---

## **Commit 1 — Configuración inicial**

### Preguntas realizadas:
- *“¿Qué archivos debo incluir en .gitignore para un proyecto Python?”*
- *“¿Cómo estructuro un README básico para un proyecto de calculadora?”*

### Aportes de la IA:
- Proporcionó un `.gitignore` estándar para Python.
- Sugirió la estructura inicial del README.
- Recomendó la estructura de carpetas del proyecto.
- Explicó buenas prácticas de organización.

---

## **Commit 2 — Función básica de cálculo**

### Preguntas realizadas:
- *“¿Cómo escribo una función en Python que calcule el 10% de un monto?”*
- *“¿Cómo pruebo manualmente una función en Python?”*

### Aportes de la IA:
- Generó la función `calcular_propina_10()`.
- Explicó cómo usar `if __name__ == "__main__"` para pruebas manuales.

---

## **Commit 3 — Porcentaje personalizable**

### Preguntas realizadas:
- *“¿Cómo modifico mi función para aceptar un porcentaje personalizable?”*
- *“¿Cómo valido que un número sea positivo en Python?”*

### Aportes de la IA:
- Explicó cómo añadir parámetros a funciones.
- Sugirió validaciones con `raise ValueError`.
- Generó la función `calcular_propina_porcentaje()`.

---

## **Commit 4 — División entre personas**

### Preguntas realizadas:
- *“¿Cómo calculo el total incluyendo propina y lo divido entre N personas?”*
- *“¿Qué estructura de datos me recomiendas para devolver múltiples valores?”*

### Aportes de la IA:
- Recomendó usar diccionarios para claridad.
- Generó la función `dividir_cuenta()`.
- Explicó cómo calcular total y monto por persona.

---

## **Commit 5 — Validaciones**

### Preguntas realizadas:
- *“¿Cómo implemento validaciones robustas para entradas numéricas?”*
- *“¿Cómo uso try-except para manejar errores de conversión?”*

### Aportes de la IA:
- Sugirió crear funciones de validación independientes.
- Explicó el uso correcto de `try/except`.
- Mejoró la robustez del programa.

---

## **Commit 6 — Redondeo y formato**

### Preguntas realizadas:
- *“¿Cómo redondeo números a 2 decimales en Python?”*
- *“¿Cómo formateo un número como moneda con el símbolo $?”*

### Aportes de la IA:
- Explicó el uso de `round()` y formato `f"{valor:.2f}"`.
- Generó la función `formatear_moneda()`.

---

## **Commit 7 — Múltiples formas de propina**

### Preguntas realizadas:
- *“¿Cómo diseño una función que acepte diferentes tipos de propina?”*
- *“¿Cómo manejo dos formas diferentes de calcular la propina?”*

### Aportes de la IA:
- Explicó el patrón de “función unificada con selector”.
- Generó la función `calcular_propina()`.
- Añadió soporte para propina fija y porcentaje.
- Ayudó a corregir errores de validación y llamadas incorrectas.

---

### Commit 8 MULTIPLES CAMBIOS

### Inicio de Interfaz Gráfica (GUI)
Preguntas realizadas:
-¿Cómo creo una interfaz gráfica en Python con tkinter?
-¿Cómo conecto la GUI con mis funciones existentes?
-¿Cómo organizo el código para no mezclar lógica y presentación?

Aportes de la IA:
-Explicó la estructura básica de una aplicación tkinter.
-Generó la clase TipCalculatorGUI.
-Mostró cómo crear:
    Ventana principal.
    Labels.
    Entry fields.
    Radiobuttons.
    Botón de cálculo.
-Ayudó a conectar la GUI con la función dividir_cuenta().
-Explicó cada bloque de código generado.
-Orientó en la separación entre lógica (services) y presentación (gui).

### Modularización Completa del Proyecto
Preguntas realizadas:
-¿Cómo estructuro el proyecto de forma más profesional?
-¿Cómo separo validaciones, servicios y utilidades?
-¿Qué estructura usan los proyectos reales en Python?

Aportes de la IA:
-Propuso reorganizar el proyecto dentro de la carpeta src/.
-Sugirió separar en:
    services.py
    validators.py
    utils.py
    menu.py
    gui.py
-Aplicó principios de separación de responsabilidades.
-Refactorizó el código sin cambiar funcionalidad.
-Mejoró nomenclaturas y claridad.
-Aplicó conceptos básicos de Clean Code.

### Historial de Cálculos en GUI
Preguntas realizadas:
-¿Cómo puedo guardar y mostrar un historial en tkinter?
-¿Cómo funciona el widget Treeview?

Aportes de la IA:
-Explicó el uso de ttk.Treeview.
-Implementó una tabla con columnas:
    Monto
    Propina
    Total
    Por persona
-Mostró cómo insertar registros dinámicamente.
-Mejoró la experiencia de usuario.
-Explicó cómo organizar mejor los widgets en la ventana.

### Integración de Gráficos con Matplotlib
Preguntas realizadas:
-¿Cómo integro matplotlib dentro de tkinter?
-¿Cómo muestro un gráfico que se actualice cada vez que calculo?

Aportes de la IA:
-Explicó el uso de FigureCanvasTkAgg.
-Generó el gráfico circular (pie chart).
-Mostró cómo limpiar y redibujar el gráfico.
-Ayudó a integrar visualización dinámica dentro de la GUI.
-Explicó la estructura básica de matplotlib.

### Selector de Modo (CLI / GUI)
Preguntas realizadas:
-¿Cómo puedo tener modo terminal y modo gráfico en el mismo proyecto?
-¿Cómo detecto si hay consola disponible?
-¿Cómo estructuro un main profesional?

Aportes de la IA:
-Diseñó main.py como punto de entrada principal.
-Implementó selector de modo:
    CLI
    GUI
-Explicó el uso de if __name__ == "__main__".
-Orientó sobre detección de consola con sys.stdin.isatty().
-Ayudó a corregir comportamientos inesperados en distintos entornos.
-Refactorizó el main para hacerlo más estable.

### Generación de Ejecutable (.exe)
Preguntas realizadas:
-¿Cómo convierto mi proyecto en un ejecutable?
-¿Por qué mi .exe no abre al hacer doble clic?
-¿Qué hace --windowed en PyInstaller?

Aportes de la IA:
-Explicó el uso de PyInstaller.
-Ayudó a generar ejecutable con:
    --onefile
    --windowed
-Detectó posibles problemas con matplotlib.
-Propuso soluciones con --hidden-import.
-Ayudó a depurar errores silenciosos.
-Explicó diferencias entre ejecutar desde consola y entorno IDE.

### Refactorización Final y Documentación
Preguntas realizadas:
-¿Puedes refactorizar el código aplicando Clean Code?
-Añade docstrings sin cambiar la lógica.
-¿Cómo dejo el proyecto listo para portfolio?

Aportes de la IA:
-Añadió docstrings profesionales.
-Añadió type hints.
-Mejoró organización de imports.
-Simplificó estructuras sin alterar funcionalidad.
-Mejoró nombres de funciones y claridad.
-Ajustó el main para evitar problemas en desarrollo.
-Ayudó a completar el README y documentación técnica.
-Redactó mejoras estructurales para GitHub.


### Commit 9 — Implementación de Testing Automatizado
Preguntas realizadas:
-¿Cómo escribo tests con pytest?
-¿Cómo organizo una carpeta de testing profesional?
-¿Cómo pruebo casos edge y validaciones?
-¿Por qué aparece el error 'ModuleNotFoundError: No module named src'?
-¿Cómo soluciono problemas de PYTHONPATH en pytest?

Aportes de la IA:
-Explicó cómo instalar y configurar pytest.
-Ayudó a estructurar la carpeta test/.
-Generó tests unitarios para:
    dividir_cuenta()
    formatear_moneda()
    Validadores
-Añadió pruebas para:
    Valores negativos
    Ceros
    Entradas inválidas
    Manejo de excepciones

-Explicó cómo convertir src en paquete usando __init__.py.
-Indicó cómo usar pytest.ini para configurar pythonpath.
-Explicó buenas prácticas de ejecución de tests desde la raíz del proyecto.
-Ayudó a interpretar errores de entorno y solucionarlos correctamente.

### Validación Final del Proyecto

El proyecto ahora cuenta con:

-Código modular
-Validaciones robustas
-Manejo de errores
-Formato correcto de moneda
-Soporte para propina fija y porcentaje
-Testing automatizado
-Estructura profesional tipo proyecto real
-Buenas prácticas aplicadas (Clean Code)



# 🧠 Reflexión Final

El uso de IA permitió:

- Acelerar el desarrollo.
- Aprender buenas prácticas.
- Resolver errores rápidamente.
- Documentar el proceso de forma profesional.

El desarrollador mantuvo siempre el control del código, revisando y entendiendo cada parte del proceso.

*Desde el Commit 8 hasta el estado actual, la IA ayudó a transformar el proyecto desde: Script de consola funcional*

hasta:
Aplicación de escritorio modular, con doble interfaz (CLI + GUI), historial dinámico, visualización gráfica y ejecutable distribuible.

El desarrollador mantuvo el control total:
-Revisando cada bloque generado.
-Pidiendo explicaciones detalladas.
-Ajustando el código a sus criterios.
-Decidiendo estructura y organización final.
-Solicitando refactorizaciones específicas sin alterar comportamiento.

La IA actuó como asistente técnico y guía estructural, pero las decisiones finales y validaciones fueron realizadas por el desarrollador.

*En el commit 9 implementación de Testing Automatizado*
La IA no solo ayudó a generar código, sino que también:

-Explicó cada bloque generado.
-Justificó decisiones de arquitectura.
-Detectó problemas de entorno.
-Aplicó estándares profesionales de testing.
-Simuló un entorno real de desarrollo profesional.

El desarrollador mantuvo siempre el control total del proyecto, comprendiendo cada parte del código antes de integrarla.

---

# Evolución del Proyecto 

El proyecto evolucionó desde:
Script básico de consola

hasta:
Aplicación de escritorio modular con doble interfaz, historial dinámico y visualización gráfica integrada.

Se aplicaron conceptos de:

-Arquitectura modular.
-Separación de responsabilidades.
-Buenas prácticas de validación.
-Diseño de interfaces gráficas.
-Integración de librerías externas.
-Empaquetado y distribución de software.

# Estado Actual del Proyecto

-Funcional
-Modular
-Escalable
-Ejecutable
-Documentado
-Portfolio-ready
-TestAutomatizado


# Estado actual del proyecto

El proyecto está completo hasta el Commit 7, con:

- Validaciones robustas.
- Cálculo modular.
- Soporte para propina fija y porcentaje.
- Formato de moneda.
- Código limpio y organizado.
- El proyecto ahora incluye:
- Interfaz en terminal (CLI).
- Interfaz gráfica con tkinter.
- Historial dinámico.
- Visualización con matplotlib.
- Modularización profesional.
- Refactorización con Clean Code.
- Ejecutable funcional.
- Documentación completa.
- Registro detallado de asistencia de IA.
- Testing automatizado.
- Licencia MIT.
Proyecto finalizado y listo para portfolio profesional.
