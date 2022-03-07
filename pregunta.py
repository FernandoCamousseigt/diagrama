from abc import ABC, abstractclassmethod

class Pregunta():
    def __init__(self, enunciado: str, ayuda: str, requerido: bool):
        self.enunciado = enunciado
        self.ayuda= ayuda
        self.requedio= requerido

    def mostrar_pregunta(self, enunciado):
        pass