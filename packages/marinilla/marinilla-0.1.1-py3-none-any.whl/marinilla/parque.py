

class operacion:
    "esta clase realiza las operaciones basicas de una calculadora"

    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def suma(self):
        "esta funcion realiza la suma de dos numeros"
        return self.a + self.b