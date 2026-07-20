# Registro de Actualizaciones

# Semana 3

Durante esta versión del proyecto se realizó una refactorización del sistema para aplicar los pilares de la Programación Orientada a Objetos (POO), mejorando la organización del código y facilitando su mantenimiento.

---

## 1. Encapsulamiento

Se implementó el encapsulamiento mediante propiedades (`@property`) para los atributos `cliente_id`, `tipo` y `monto`.

Se añadieron getters y setters que validan la información antes de almacenarla, evitando datos inválidos como identificadores vacíos, tipos de transacción incorrectos o montos negativos.

**Beneficios:**

- Mayor protección de los datos.
- Validación automática de la información.
- Mejor control sobre los atributos del objeto.

---

## 2. Herencia

La antigua clase `Transaccion` fue reemplazada por una clase base denominada `TransaccionBase`.

A partir de ella se implementaron las clases:

- TransaccionCredito
- TransaccionDebito

Estas clases reutilizan el comportamiento común de la clase base y únicamente implementan la lógica específica de cada tipo de transacción.

**Beneficios:**

- Reutilización del código.
- Menor duplicidad.
- Facilidad para ampliar el sistema.

---

## 3. Polimorfismo

Se implementó el método `calcular_impacto()` utilizando polimorfismo.

Cada tipo de transacción calcula su impacto de manera diferente utilizando el mismo método.

**Beneficios:**

- Código flexible.
- Fácil incorporación de nuevos tipos de transacción.
- Mejor mantenimiento.

---

## 4. Método Fábrica

Se implementó la función `crear_transaccion()`, encargada de crear automáticamente el tipo de objeto correspondiente según la información leída desde el archivo.

**Beneficios:**

- Centraliza la creación de objetos.
- Reduce el acoplamiento.
- Facilita futuras ampliaciones del sistema.

---

## 5. Validación de datos

Se incorporaron validaciones para garantizar que:

- El identificador del cliente no esté vacío.
- El tipo de transacción sea válido.
- El monto no sea negativo.

Estas validaciones generan excepciones cuando la información no cumple los requisitos establecidos.

---

## 6. Documentación

Se añadieron comentarios descriptivos en clases, funciones y métodos para facilitar la comprensión y mantenimiento del proyecto.

---

## Resultado

El sistema quedó estructurado bajo los pilares de la Programación Orientada a Objetos, incorporando Encapsulamiento, Herencia, Polimorfismo y un método fábrica para mejorar la organización y escalabilidad del código.

---

# Semana 4

*(Aquí dejas exactamente la que ya tienes sobre el manejo de excepciones, try-except, registro de errores y continuidad del procesamiento de registros.)*

---

# Semana 5

Durante esta versión del proyecto se realizó una reorganización de la estructura del programa con el objetivo de separar las responsabilidades en diferentes módulos, facilitando el mantenimiento y la reutilización del código.

---

## 1. Separación de responsabilidades

La lógica del sistema fue dividida en diferentes archivos para que cada uno tenga una función específica.

Se creó un módulo encargado de procesar las transacciones y otro destinado únicamente a representar la clase `Transaccion`.

**Beneficios:**

- Código más organizado.
- Menor acoplamiento entre componentes.
- Mayor facilidad para realizar modificaciones futuras.

---

## 2. Modularización del proyecto

Las funciones encargadas de leer el archivo, calcular el monto total y filtrar las transacciones fueron agrupadas dentro de un módulo independiente del programa principal.

**Beneficios:**

- Mejor distribución del código.
- Mayor reutilización de funciones.
- Facilita el trabajo colaborativo.

---

## 3. Separación entre datos y procesamiento

La clase `Transaccion` quedó dedicada únicamente al almacenamiento y representación de la información, mientras que el procesamiento de los datos se realiza desde un módulo diferente.

**Beneficios:**

- Cumple con el Principio de Responsabilidad Única (SRP).
- Reduce la dependencia entre clases.
- Facilita el mantenimiento del sistema.

---

## 4. Organización del punto de entrada

Se creó una función principal (`ejecutar_sistema()`) que centraliza el flujo de ejecución del programa.

Esto permite que todas las operaciones se ejecuten desde un único punto de entrada.

**Beneficios:**

- Mejor organización.
- Código más legible.
- Flujo de ejecución más claro.

---

## Resultado

Con estas mejoras el proyecto quedó organizado en módulos independientes, donde cada archivo cumple una responsabilidad específica. Esta estructura facilita el mantenimiento, mejora la reutilización del código y hace que el sistema sea más escalable para futuras versiones.