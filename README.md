## Instalación
1. Clonar el repositorio:

# Calculadora de Propinas

Este proyecto es una calculadora de propinas desarrollada en Python. Permite calcular
propinas con porcentaje fijo o personalizado, dividir la cuenta entre varias personas
y validar las entradas del usuario. El objetivo es practicar programación, Git y el uso
de herramientas de IA para generar y mejorar código.

## Objetivos
- Calcular propinas con porcentaje fijo o personalizado.
- Dividir la cuenta entre varias personas.
- Validar entradas del usuario.
- Crear una interfaz interactiva en terminal.
- Documentar el proceso de desarrollo y asistencia de IA.
## Objetivo educativo
Este proyecto forma parte de un ejercicio práctico para aprender:
- Control de versiones con Git.
- Programación en Python.
- Buenas prácticas de desarrollo.
- Uso de IA para generar y mejorar código

## Estructura del proyecto
- `src/`: Código fuente.
- `docs/`: Documentación adicional.
- `requirements.txt`: Dependencias.
- `.gitignore`: Archivos ignorados por Git.

## Funcionalidades
- Cálculo de propina con porcentaje fijo (10%).
- Cálculo de propina con porcentaje personalizado.
- División del total entre varias personas.
- Validaciones de entrada.
- Interfaz interactiva en terminal.



QUÉ HACE CADA BLOQUE DE CÓDIGO
1. VALIDACIONES
Funciones que aseguran que los datos sean correctos antes de calcular nada:
monto > 0
porcentaje >= 0
propina fija >= 0
personas entero positivo

2. UTILIDADES
Funciones auxiliares:
formatear_moneda() → convierte números a formato $12.34

3. CÁLCULO DE PROPINAS
Tres funciones:
porcentaje
fija
función unificada que decide cuál usar

4. DIVISIÓN DE LA CUENTA
Calcula:
propina
total
total por persona
Devuelve un diccionario limpio.

5. PRUEBAS MANUALES
Simula el menú del commit 8 pero sin bucle:
pide datos
calcula
muestra resultados
Esto hace tu código modular, limpio, escalable y fácil de mantener.


COMMIT 8 / para la parte de la interfaz copilot se quedo colgado.
asi que hare el resto del pyoyecto con ChatGPT

ACABAMOS DE BORRAR todo lo que eran las prubas manuales para mejorar

🔁 1. Bucle principal
El programa se repite hasta que el usuario elige salir.

🧠 2. Validación en tiempo real
Si el usuario introduce texto en vez de número:

❌ Entrada inválida. Debes introducir un número válido.
No se rompe el programa.

💬 3. Mensajes claros y profesionales
Separadores, emojis discretos y estructura visual clara.

🚪 4. Opción de salir limpia
Termina con break correctamente.

🏗 5. Código modular
Ahora tu menú está separado en:
mostrar_menu()
ejecutar_calculo()
funciones auxiliares

Esto es diseño limpio tipo producción.

Estructura mental que debes entender

Un menú interactivo profesional tiene 3 capas:

1️⃣ Mostrar opciones
2️⃣ Capturar entrada
3️⃣ Validar entrada
4️⃣ Ejecutar acción
5️⃣ Repetir

Y todo eso se controla con:

while

if/elif

try/except

break

Resumen claro
🧭 Menú interactivo

Se crea con:

while True

input()

if/elif

break

🔒 Validación en bucle

Se hace con:

try/except

validaciones lógicas

repetir hasta que sea válido

Esto es separación real de responsabilidades.

tip_calculator/
│
├── main.py          → Punto de entrada
├── menu.py          → Interfaz de usuario (CLI)
├── services.py      → Lógica de negocio
├── validators.py    → Validaciones
└── utils.py         → Utilidades


PERFECTO.
Ahora sí vamos a hacerlo como proyecto serio.

Vamos a:

✅ Hacer proyecto híbrido (CLI + GUI)

🎨 Mejorar la GUI visualmente

🧠 Mantener arquitectura limpia

🚀 Dejarlo escalable

¿Qué mejoramos en la GUI?

✅ Uso de ttk (más moderno que Tk básico)
✅ Tema visual "clam"
✅ Layout limpio con padding
✅ Botón limpiar
✅ Mensajes elegantes
✅ Diseño más profesional

🎯 Ahora tienes

✔ Proyecto híbrido real
✔ Arquitectura limpia
✔ CLI funcional
✔ GUI moderna
✔ Código desacoplado
✔ Escalable