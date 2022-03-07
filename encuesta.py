from abc import ABC, abstractclassmethod

class Encuesta():
    def __init__(self, nombre: str,):
        self.nombre = nombre
      

    def mostrar_encuesta(self, nombre):
        pass
    
    def agregar_listado_preguntas(self, nombre):
        pass