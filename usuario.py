from abc import ABC, abstractclassmethod

class Usuario():
    def __init__(self, correo: str, edad: int, region: int):
        self.correo = correo
        self.edad= edad
        self.region=region

    def contestar_encuesta(self, correo):
        pass