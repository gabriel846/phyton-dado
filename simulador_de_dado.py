# Simulador de dado
# Simular o uso de um dado, gerando um valor de 1 até 6
import random

class SimuladordeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'voce gostaria de gerar um novo valor para o dado?'

    def Iniciar(self):
        print(self.mensagem)
        resposta = input(self.mensagem)
        try:
            if resposta == 'sim' or resposta =='s':
                self.GerarValordoDado()
            elif resposta == 'não' or resposta =='n':
                print('agradecemos a sua participação!')
            else:
                print('favor digitar sim ou nao')
        except:
            print('Ocorreu um erro ao receber sua resposta')

    def GerarValordoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladordeDado()
simulador.Iniciar()
    