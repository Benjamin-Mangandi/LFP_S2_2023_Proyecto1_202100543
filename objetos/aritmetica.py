import math
class operacion:
    def __init__(self, tipo, valor1, valor2, resultado):
        self.tipo =tipo
        self.valor1 = valor1
        self.valor2 = valor2
        self.resultado = resultado
    def operar(tipo, valor1, valor2):
        if tipo.lower() == "suma":
            try:
                return valor1+valor2
            except Exception:
                return 0
        if tipo.lower() == "resta":
            try:
                return valor1-valor2
            except Exception:
                return 0
        if tipo.lower() == "multiplicacion":
            try:
                return round(valor1*valor2,4)
            except Exception:
                return 0
        if tipo.lower() == "division":
            try:
                if valor2 != 0:
                    return round(valor1/valor2,4)
            except Exception:
                return 0
        if tipo.lower() == "potencia":
            try:
                return math.pow(valor1,valor2)
            except Exception:
                return 0
        if tipo.lower() == "raiz":
            try:
                return round(math.pow(valor1,1/valor2),4)
            except Exception:
                return 0
        if tipo.lower() == "inverso":
            try:
                return round(1/valor1,4)
            except Exception:
                return 0
        if tipo.lower() == "seno":
            try:
                angulo_en_radianes = (valor1 * math.pi) / 180.0
                return round(math.sin(angulo_en_radianes),4)
            except Exception:
                return 0
        if tipo.lower() == "coseno":
            try:
                angulo_en_radianes = (valor1 * math.pi) / 180.0
                return round(math.cos(angulo_en_radianes),4)
            except Exception:
                return 0
        if tipo.lower() == "tangente":
            try:
                angulo_en_radianes = (valor1 * math.pi) / 180.0
                return round(math.tan(angulo_en_radianes),4)
            except Exception:
                return 0
        if tipo.lower() == "mod":
            try:
                return valor1%valor2
            except Exception:
                return 0
        


