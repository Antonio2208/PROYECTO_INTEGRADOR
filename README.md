# Proyecto Integrador – Lógica de Programación
## Piedra, Papel o Tijeras (Consola y GUI)

Autor: Luis Antonio Burgos Albarracín 

Asignatura: Lógica de Programación 

Lenguaje: Python 

Fecha: 21 de Diciembre 2025

---

## 1. Nombre del proyecto

El impacto de las nuevas tecnologías en la sociedad: visualización del futuro.

Este proyecto integra los contenidos vistos a lo largo de la asignatura, aplicados al desarrollo de un software funcional en Python.

---

## 2. Descripción general del proyecto

El proyecto consiste en el desarrollo del juego Piedra, Papel o Tijeras, implementado en Python, el cual permite al usuario interactuar con el sistema tanto mediante consola como mediante una interfaz gráfica (GUI).

El objetivo principal es demostrar cómo la programación permite crear sistemas interactivos, simulando decisiones humanas y mostrando cómo la tecnología transforma la forma en la que las personas interactúan con el software.

---

## 3. Propósito del proyecto

- Aplicar los conocimientos adquiridos durante las cuatro unidades de la materia.
- Comprender la lógica detrás de la toma de decisiones en un programa.
- Visualizar cómo un mismo programa puede adaptarse a diferentes formas de interacción (consola y GUI).
- Reflexionar sobre el impacto de las tecnologías interactivas en la sociedad actual y futura.

---

## 4. Funcionalidades del programa

El software permite:

- Seleccionar el modo de juego:
  - Modo fácil: una sola ronda.
  - Modo difícil: cinco rondas con un sistema de conteo que analiza las elecciones del usuario.
- Elegir entre:
  - Piedra
  - Papel
  - Tijeras
- Mostrar el resultado de cada ronda.
- Mostrar el resultado final (victorias, derrotas y empates).
- Validar correctamente las entradas del usuario.
- Manejar errores mediante estructuras try / except.

---

## 5. Interfaz gráfica (GUI)

Además de funcionar por consola, el programa incluye una interfaz gráfica básica desarrollada con la librería Tkinter.

La interfaz gráfica cuenta con botones para la selección del modo de juego y de la jugada del usuario, así como un área de texto que muestra la salida del programa de manera equivalente a la consola.

La interfaz no modifica la lógica del programa, únicamente reemplaza los mecanismos de entrada y salida de datos por elementos visuales, manteniendo la esencia del código original.

---

## 6. Justificación del uso de estructuras de datos

Durante una de las semanas de la asignatura se estudiaron listas, tuplas y diccionarios. Sin embargo, en este proyecto no fue necesario utilizarlos por las siguientes razones:

- El programa maneja un conjunto reducido de opciones fijas (1, 2 y 3).
- La lógica del juego se basa principalmente en estructuras condicionales, bucles repetitivos y contadores numéricos simples.
- El uso de listas o diccionarios no aportaba una mejora funcional significativa al desarrollo del programa.
- Se priorizó la claridad y comprensión del código, considerando que se trata de un proyecto de aprendizaje.

Aunque hubiera sido posible utilizar diccionarios para mapear valores (por ejemplo, 1 = Piedra), se decidió no hacerlo para mantener el código más directo y comprensible.

Esta decisión fue tomada de manera consciente y justificada, alineada con los objetivos del proyecto.

---

## 7. Requisitos técnicos

- Python 3
- Librerías utilizadas:
  - random
  - math
  - tkinter

---

## 8. Ejecución del programa

Modo consola:

- Ocupar el primer archivo con el nombre "Piedra, papel y tijeras.py" 

Modo interfaz gráfica:

- Ocupar el segundo archivo con el nombre "Piedra, papel y tijeras (GUI).py"

---

## 9. Conclución

Este proyecto demuestra cómo la programación permite crear soluciones interactivas utilizando lógica, validaciones y estructuras básicas. La integración de una interfaz gráfica evidencia cómo el software puede evolucionar hacia experiencias más visuales, reflejando el impacto de las nuevas tecnologías en la sociedad actual.

