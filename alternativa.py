from abc import ABC, abstractclassmethod

class Alternativa():
    def __init__(self, contenido: str, ayuda: str):
        self.contenido = contenido
        self.ayuda= ayuda

    def mostrar_alternativa(self, contenido):
        pass