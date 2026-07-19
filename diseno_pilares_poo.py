# =========================================================
# diseno_pilares_poo.py
# =========================================================
# Clase Base del sistema
# Contiene la información y el comportamiento común para
# todas las transacciones del sistema.
# ********** ACTUALIZACIÓN SEMANA 3 **********
# Se reemplaza la antigua clase Transaccion por una clase
# base para implementar Herencia y facilitar la creación
# de nuevos tipos de transacciones.
# =========================================================

class TransaccionBase:
    """
    Clase base que encapsula la información común
    a cualquier tipo de transacción.
    """

    def __init__(self, cliente_id, tipo, monto):
        self.cliente_id = cliente_id
        self.tipo = tipo
        self.monto = float(monto)

    # -------------------------
    # Encapsulamiento
    # -------------------------
# Encapsulamiento
# ********** ACTUALIZACIÓN SEMANA 3 **********
# Los atributos ahora son privados (_cliente_id, _tipo,
# _monto). Esto evita modificaciones directas y obliga
# a acceder mediante getters y setters.
# -------------------------
# ********** ACTUALIZACIÓN SEMANA 3 **********
# Getter del atributo cliente_id.
# Permite consultar el dato sin acceder directamente
# al atributo privado.

    @property
    def cliente_id(self):
        return self._cliente_id

# ********** ACTUALIZACIÓN SEMANA 3 **********
# Setter del atributo cliente_id.
# Se valida que el identificador del cliente no esté vacío,
# evitando datos inválidos en el sistema.

    @cliente_id.setter
    def cliente_id(self, valor):
        if not str(valor).strip():
            raise ValueError("El ID del cliente no puede estar vacío.")
        self._cliente_id = valor

# ********** ACTUALIZACIÓN SEMANA 3 **********
# Getter del tipo de transacción.

    @property
    def tipo(self):
        return self._tipo
    
# ********** ACTUALIZACIÓN SEMANA 3 **********
# Setter del tipo de transacción.
# Se valida que únicamente existan transacciones
# de tipo CREDITO o DEBITO.

    @tipo.setter
    def tipo(self, valor):
        valor = str(valor).upper().strip()
        if valor not in ("CREDITO", "DEBITO"):
            raise ValueError("Tipo de transacción inválido.")
        self._tipo = valor

# ********** ACTUALIZACIÓN SEMANA 3 **********
# Getter del monto.

    @property
    def monto(self):
        return self._monto
    
# ********** ACTUALIZACIÓN SEMANA 3 **********
# Setter del monto.
# Se impide registrar montos negativos para mantener
# la integridad de la información.

    @monto.setter
    def monto(self, valor):
        valor = float(valor)
        if valor < 0:
            raise ValueError("El monto no puede ser negativo.")
        self._monto = valor

    def obtener_informacion(self):
        return (
            f"Cliente: {self.cliente_id} | "
            f"Tipo: {self.tipo} | "
            f"Monto: ${self.monto:,.2f}"
        )

    def calcular_impacto(self):
        raise NotImplementedError(
            "Este método debe implementarse en las clases hijas."
        )

# =========================================================
# Herencia
# ********** ACTUALIZACIÓN SEMANA 3 **********
# Se crean clases hijas que heredan de TransaccionBase.
# De esta manera se reutiliza la lógica común sin
# duplicar código.
# =========================================================
# ********** ACTUALIZACIÓN SEMANA 3 **********
# Clase hija para transacciones de crédito.
# Sobrescribe calcular_impacto() aplicando un
# comportamiento específico.

class TransaccionCredito(TransaccionBase):

    def calcular_impacto(self):
        # Ejemplo: interés del 5 %
        return self.monto * 0.05
    
# ********** ACTUALIZACIÓN SEMANA 3 **********
# Clase hija para transacciones de débito.
# Sobrescribe calcular_impacto() aplicando una
# comisión fija.

class TransaccionDebito(TransaccionBase):

    def calcular_impacto(self):
        # Ejemplo: comisión fija
        return 2000

# =========================================================
# Polimorfismo
# ********** ACTUALIZACIÓN SEMANA 3 **********
# El método calcular_impacto() es el mismo para todas
# las transacciones, pero cada clase hija implementa
# un comportamiento diferente.
# =========================================================


# =========================================================
# Método Fábrica
# ********** ACTUALIZACIÓN SEMANA 3 **********
# Se centraliza la creación de objetos. Según el tipo
# leído del archivo se crea automáticamente una
# TransaccionCredito o una TransaccionDebito.
#
# Esta mejora facilita futuras ampliaciones del sistema
# siguiendo el principio SOLID Open/Closed (OCP).
# =========================================================

def crear_transaccion(cliente_id, tipo, monto):

    if tipo.upper() == "CREDITO":
        return TransaccionCredito(cliente_id, tipo, monto)

    elif tipo.upper() == "DEBITO":
        return TransaccionDebito(cliente_id, tipo, monto)

    else:
        raise ValueError(f"Tipo de transacción desconocido: {tipo}")

# =========================================================
# Lectura del archivo
# ********** ACTUALIZACIÓN SEMANA 3 **********
# Ya no se crean objetos Transaccion directamente.
# Ahora la creación de objetos se delega al método
# crear_transaccion().
# =========================================================

def leer_y_almacenar_datos(nombre_archivo):

    transacciones = []

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:

        for linea in archivo:

            linea = linea.strip()

            if not linea:
                continue

            cliente_id, tipo, monto = linea.split(",")

            transaccion = crear_transaccion(cliente_id, tipo, monto)

            transacciones.append(transaccion)

    return transacciones

# ********** ACTUALIZACIÓN SEMANA 3 **********
# Se mantiene la función de cálculo del total.
# Gracias al encapsulamiento el acceso al monto se
# realiza mediante la propiedad monto.

def calcular_total(transacciones):

    total = 0

    for transaccion in transacciones:
        total += transaccion.monto

    return total

# ********** ACTUALIZACIÓN SEMANA 3 **********
# Filtra las transacciones por tipo utilizando las
# propiedades públicas de los objetos.

def filtrar_por_tipo(transacciones, tipo_busqueda):

    resultado = []

    for transaccion in transacciones:

        if transaccion.tipo == tipo_busqueda.upper():
            resultado.append(transaccion)

    return resultado


# =========================================================
# Programa principal
# =========================================================
# ********** ACTUALIZACIÓN SEMANA 3 **********
# Demostración del Polimorfismo.
# Aunque todos los objetos utilizan el método
# calcular_impacto(), el resultado cambia dependiendo
# del tipo de transacción (Crédito o Débito).

if __name__ == "__main__":

    try:

        transacciones = leer_y_almacenar_datos("transacciones.txt")

        total = calcular_total(transacciones)

        print(f"\nMonto Total de Transacciones: ${total:,.2f}")

        print("\n" + "-" * 50)

        creditos = filtrar_por_tipo(transacciones, "CREDITO")

        print("\nTransacciones filtradas por tipo [CREDITO]:\n")

        for transaccion in creditos:
            print(transaccion.obtener_informacion())

        print("\n" + "-" * 50)
        print("Impacto de cada transacción:\n")

        for transaccion in transacciones:

            print(transaccion.obtener_informacion())

            print(
                f"Impacto: ${transaccion.calcular_impacto():,.2f}"
            )

            print("-" * 40)

# ********** ACTUALIZACIÓN SEMANA 3 **********
# Se agrega manejo de excepciones para evitar que el
# programa termine inesperadamente cuando exista un
# archivo inexistente o datos inválidos.

    except FileNotFoundError:
        print("Error: No se encontró el archivo 'transacciones.txt'.")

    except ValueError as e:
        print(f"Error en los datos: {e}")

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
