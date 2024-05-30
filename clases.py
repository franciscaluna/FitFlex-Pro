class Usuario:
    def __init__(self, nombre, edad, peso, altura): #constructor
        self.nombre = nombre #atributos
        self.edad = edad
        self.peso = peso
        self.altura = altura

    def serialize(self):
        return {
            'Nombre': self.nombre,
            'Edad': self.edad,
            'Peso': self.peso,
            'Altura': self.altura
        }
class Ejercicios:
    def tipos_ejercicios(self):
        self.tipo1 = "Fortalecer brazos"
        self.tipo2 = "Fortalecer espalda"
        self.tipo3 = "Fortalecer piernas"
        self.tipo4 = "Fortalecer gluteos"

    __entrenador = "Juan" # encapsulamiento
    def obtener_entrenado(self):
        return self.__entrenador

