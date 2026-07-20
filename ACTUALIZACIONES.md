# Registro de Actualizaciones

## Semana 3

Durante esta versión del proyecto se realizaron mejoras orientadas a fortalecer la aplicación de los pilares de la Programación Orientada a Objetos y mejorar la organización del código.

---

### 1. Encapsulamiento

Se implementó el uso de atributos protegidos y privados para controlar el acceso a la información de los objetos.

Además, se incorporaron métodos **getter** y **setter** para consultar y modificar los datos de forma segura, realizando validaciones cuando es necesario.

**Beneficios:**

- Mayor seguridad de los datos.
- Evita modificaciones incorrectas.
- Mejor control sobre los atributos.

---

### 2. Herencia

Se organizó el sistema utilizando una clase base de maquinaria, de la cual heredan clases específicas como **Tractor** y **Sistema de Riego**.

**Beneficios:**

- Reutilización del código.
- Menor duplicidad.
- Mejor organización del proyecto.

---

### 3. Polimorfismo

Se implementó el polimorfismo mediante la redefinición del método `realizar_operacion()` en cada clase hija.

Cada tipo de maquinaria ejecuta una operación diferente utilizando el mismo nombre de método.

**Beneficios:**

- Código más flexible.
- Fácil incorporación de nuevas máquinas.
- Mejor mantenimiento.

---

### 4. Abstracción

Se definió una clase base que representa las características comunes de toda maquinaria.

Las clases hijas implementan únicamente el comportamiento específico que les corresponde.

**Beneficios:**

- Mejor organización.
- Separación de responsabilidades.
- Código más fácil de comprender.

---

### 5. Asociación entre clases

Se implementó la relación entre la clase **Operador** y las diferentes máquinas agrícolas.

Cada operador puede tener asignada una maquinaria y ejecutar las operaciones correspondientes.

---

### 6. Gestión de mantenimiento

Se creó una clase destinada a registrar la información de los mantenimientos realizados a la maquinaria.

Cada mantenimiento almacena:

- Tipo.
- Descripción.
- Costo.
- Fecha.

---

### 7. Gestión de repuestos

Se implementó una clase para administrar el inventario de repuestos.

Se añadieron validaciones para evitar:

- Stock negativo.
- Uso de repuestos inexistentes.

---

### 8. Documentación del código

Se incorporaron comentarios descriptivos en las diferentes clases y métodos para facilitar el mantenimiento y la comprensión del proyecto.

---

## Resultado

Con estas mejoras el sistema presenta una estructura más organizada, reutilizable y fácil de mantener, aplicando correctamente los principios fundamentales de la Programación Orientada a Objetos.