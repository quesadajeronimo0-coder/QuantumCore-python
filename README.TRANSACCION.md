# Sistema de Gestión de Transacciones

## Descripción

Este proyecto fue desarrollado en Python aplicando los principios de la Programación Orientada a Objetos (POO). El sistema permite leer un archivo de transacciones, crear objetos según el tipo de transacción, calcular el monto total, filtrar transacciones por tipo y demostrar el uso de los pilares de la POO mediante Herencia, Encapsulamiento y Polimorfismo.

---

## Características

- Lectura de transacciones desde un archivo de texto.
- Creación automática de objetos mediante un método fábrica.
- Cálculo del monto total de las transacciones.
- Filtrado de transacciones por tipo (CRÉDITO o DÉBITO).
- Cálculo del impacto de cada transacción utilizando Polimorfismo.
- Validación de datos mediante propiedades (Properties).
- Manejo de excepciones para archivos inexistentes o datos inválidos.

---

## Requisitos

- Python 3.10 o superior.
- Sistema operativo Windows.
- Consola CMD (Símbolo del sistema).

---

## Archivos del proyecto

```
Proyecto/
│
├── diseno_pilares_poo.py
├── transacciones.txt
├── README.md
└── ACTUALIZACIONES.md
```

---

## Ejecución desde CMD

### 1. Abrir la consola

Presione las teclas:

```
Windows + R
```

Escriba:

```
cmd
```

y presione **Enter**.

---

### 2. Ubicarse en la carpeta del proyecto

Utilice el comando `cd`.

Ejemplo:

```cmd
cd C:\Users\ERIK\OneDrive\Escritorio\Proyecto
```

(Reemplace la ruta por la ubicación donde tenga guardado el proyecto).

---

### 3. Ejecutar el programa

Escriba el siguiente comando:

```cmd
python diseno_pilares_poo.py
```

Si su instalación utiliza el lanzador de Python, puede ejecutar:

```cmd
py diseno_pilares_poo.py
```

---

## Archivo de entrada

El programa utiliza el archivo:

```
transacciones.txt
```

Cada línea debe seguir el siguiente formato:

```
ClienteID,Tipo,Monto
```

Ejemplo:

```
C001,DEBITO,150000
C002,CREDITO,250000
C003,DEBITO,80000
```

Los únicos tipos válidos son:

- CREDITO
- DEBITO

---

## Salida del programa

El sistema mostrará en pantalla:

- Monto total de las transacciones.
- Transacciones filtradas por tipo CRÉDITO.
- Impacto calculado para cada transacción.
- Mensajes de error cuando exista información inválida.

---

## Conceptos de Programación Orientada a Objetos implementados

Durante el desarrollo del proyecto se aplicaron los siguientes conceptos:

- Encapsulamiento mediante Properties.
- Herencia utilizando una clase base (`TransaccionBase`).
- Polimorfismo mediante el método `calcular_impacto()`.
- Método Fábrica para crear objetos según el tipo de transacción.
- Manejo de excepciones (`try`, `except`).

---

## Autores

Proyecto desarrollado como práctica académica de Programación Orientada a Objetos (POO).
## Documentación adicional

Las modificaciones realizadas durante el desarrollo del proyecto se encuentran registradas en el archivo **ACTUALIZACIONES.md**, donde se describen las mejoras implementadas y los cambios realizados en cada versión del sistema.
