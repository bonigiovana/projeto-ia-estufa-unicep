from pathlib import Path
import sys

raiz_projeto = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(raiz_projeto))

from Parte1.main import SistemaIoT
from imagens.processamento_imagem import analisar_imagem
from chatbot.chatbot import iniciar_chatbot

sistema_parte1 = SistemaIoT()



def prever_temperatura(temperaturas):
    # Cada posição representa uma leitura: 1, 2, 3, 4 e 5
    tempos = list(range(1, len(temperaturas) + 1))

    quantidade = len(temperaturas)
    media_tempo = sum(tempos) / quantidade
    media_temperatura = sum(temperaturas) / quantidade

    numerador = sum(
        (tempos[i] - media_tempo) * (temperaturas[i] - media_temperatura)
        for i in range(quantidade)
    )

    denominador = sum(
        (tempo - media_tempo) ** 2
        for tempo in tempos
    )

    inclinacao = numerador / denominador
    intercepto = media_temperatura - inclinacao * media_tempo

    proximo_tempo = quantidade + 1
    previsao = inclinacao * proximo_tempo + intercepto

    print("\n=== Regressão linear: tendência da temperatura ===")
    if inclinacao > 0:
        print("Tendência: temperatura subindo.")
    elif inclinacao < 0:
        print("Tendência: temperatura descendo.")
    else:
        print("Tendência: temperatura estável.")

    print(f"Variação média por leitura: {inclinacao:.2f} °C")
    print(f"Previsão para a leitura {proximo_tempo}: {previsao:.2f} °C")


def treinar_perceptron():
    # Cada exemplo contém uma temperatura e a classe esperada:
    # 0 = adequada; 1 = risco alto
    exemplos = [
        (22.5, 0),
        (25.7, 0),
        (28.0, 0),
        (30.0, 1),
        (32.6, 1),
        (35.0, 1),
    ]

    peso = 0.0
    vies = 0.0
    taxa_aprendizado = 0.1

    for repeticao in range(20):
        for temperatura, classe_correta in exemplos:
            # Centraliza a temperatura em torno de 30 °C
            entrada = (temperatura - 30.0) / 10.0

            resultado = peso * entrada + vies
            classe_prevista = 1 if resultado >= 0 else 0
            erro = classe_correta - classe_prevista

            peso += taxa_aprendizado * erro * entrada
            vies += taxa_aprendizado * erro

    return peso, vies


def classificar_temperatura(temperatura, peso, vies):
    entrada = (temperatura - 30.0) / 10.0
    resultado = peso * entrada + vies

    if resultado >= 0:
        return "Risco alto"
    else:
        return "Temperatura adequada"

def explicar_redes_neurais():
    print("\n=== Redes neurais e aplicações ===")
    print("Redes neurais aprendem padrões a partir de exemplos.")
    print("IoT: analisam dados de sensores e podem identificar situações incomuns.")
    print("Medicina: podem ajudar profissionais a analisar exames.")
    print("Agronomia: podem analisar dados da lavoura e apoiar decisões.")
    print("Neste projeto, o perceptron é um exemplo didático simples de modelo neural.")

def executar_perceptron(temperatura_atual):
    peso, vies = treinar_perceptron()

    print("\n=== Perceptron: classificação da temperatura ===")
    print(f"Leitura atual: {temperatura_atual:.1f} °C")
    print(
        "Classificação:",
        classificar_temperatura(temperatura_atual, peso, vies)
    )


def menu():
    while True:
        print("\n=== Sistema Inteligente da Estufa ===")
        print("1 - Regressão linear")
        print("2 - Classificar leitura atual com perceptron")
        print("3 - Redes neurais e aplicações")
        print("4 - Processamento de imagem")
        print("5 - Conversar com o chatbot")
        print("6 - Inserir leitura de temperatura")
        print("7 - Exibir leituras")
        print("8 - Exibir estatísticas")
        print("9 - Simular alerta")
        print("10 - Exibir exemplos de probabilidade")
        print("11 - Processar próxima leitura")
        print("12 - Exibir histórico de ações")
        print("13 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            prever_temperatura(sistema_parte1.leituras)
        elif opcao == "2":
            executar_perceptron(sistema_parte1.leituras[-1])
        elif opcao == "3":
            explicar_redes_neurais()
        elif opcao == "4":
            analisar_imagem()
        elif opcao == "5":
            iniciar_chatbot(sistema_parte1.leituras[-1])
        elif opcao == "6":
            sistema_parte1.inserir_leitura()
        elif opcao == "7":
            sistema_parte1.exibir_leituras()
        elif opcao == "8":
            sistema_parte1.exibir_estatisticas()
        elif opcao == "9":
            sistema_parte1.simular_ia()
        elif opcao == "10":
            sistema_parte1.exibir_probabilidades()
        elif opcao == "11":
            sistema_parte1.processar_proxima_leitura()
        elif opcao == "12":
            sistema_parte1.exibir_historico()
        elif opcao == "13":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida. Escolha um número de 1 a 13.")


if __name__ == "__main__":
    menu()