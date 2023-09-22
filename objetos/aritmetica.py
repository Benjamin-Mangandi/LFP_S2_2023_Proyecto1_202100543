import math
class operacion:
    def __init__(self, tipo, valor1, valor2, resultado):
        self.tipo =tipo
        self.valor1 = valor1
        self.valor2 = valor2
        self.resultado = resultado
    def operar(tipo, valor1, valor2):
        if tipo == "suma":
            return valor1+valor2
        if tipo == "resta":
            return valor1-valor2
        if tipo == "multiplicacion":
            return valor1*valor2
        if tipo == "division":
            if valor2 != 0:
                return valor1/valor2
        if tipo == "potencia":
            return math.pow(valor1,valor2)
        if tipo == "raiz":
            return math.sqrt(valor1)
        if tipo == "inverso":
            return 1/valor1
        if tipo == "seno":
            angulo_en_radianes = (valor1 * math.pi) / 180.0
            return round(math.sin(angulo_en_radianes),4)
        if tipo == "coseno":
            angulo_en_radianes = (valor1 * math.pi) / 180.0
            return round(math.cos(angulo_en_radianes),4)
        if tipo == "tangente":
            angulo_en_radianes = (valor1 * math.pi) / 180.0
            return round(math.tan(angulo_en_radianes),4)
        if tipo == "mod":
            return valor1%valor2
        


