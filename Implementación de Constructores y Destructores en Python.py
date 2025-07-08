# Programa: Ejemplo de uso de Constructores y Destructores en Python
# Objetivo: Demostrar cómo se crean y destruyen objetos en una clase
# El constructor __init__ se ejecuta al crear el objeto
# El destructor __del__ se ejecuta al eliminar el objeto

class Persona:
    # Constructor: inicializa los atributos al crear un objeto
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(f"[Constructor] Se ha creado la persona: {self.nombre}, {self.edad} años")

    # Método para mostrar la información de la persona
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

    # Destructor: se llama automáticamente al eliminar el objeto
    def __del__(self):
        print(f"[Destructor] Se ha eliminado la persona: {self.nombre}")

# Crear instancia de Persona
persona1 = Persona("Ana", 30)
persona1.mostrar_info()

# Crear otra instancia
persona2 = Persona("Luis", 25)
persona2.mostrar_info()

# Eliminar un objeto manualmente para que se active el destructor
del persona1

# Al finalizar el programa, el destructor de persona2 se ejecutará automáticamente
print("Fin del programa")
