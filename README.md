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