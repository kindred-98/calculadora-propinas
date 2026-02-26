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

# 🧠 Reflexión Final

El uso de IA permitió:

- Acelerar el desarrollo.
- Aprender buenas prácticas.
- Resolver errores rápidamente.
- Documentar el proceso de forma profesional.

El desarrollador mantuvo siempre el control del código, revisando y entendiendo cada parte del proceso.

---

# 📌 Estado actual del proyecto

El proyecto está completo hasta el Commit 7, con:

- Validaciones robustas.
- Cálculo modular.
- Soporte para propina fija y porcentaje.
- Formato de moneda.
- Código limpio y organizado.

Listo para avanzar al Commit 8 (menú interactivo).

