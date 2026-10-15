def responder(pergunta, temperatura_atual):
    pergunta = pergunta.lower()

    if "temperatura" in pergunta:
        return f"A última temperatura simulada registrada é {temperatura_atual:.1f} °C."
    elif "alerta" in pergunta:
        return "O alerta é exibido quando a temperatura chega a 30 °C ou mais."
    elif "previsao" in pergunta or "previsão" in pergunta:
        return "A regressão linear estima a tendência usando as leituras anteriores."
    elif "oi" in pergunta or "ola" in pergunta or "olá" in pergunta:
        return "Olá! Posso responder perguntas simples sobre a estufa."
    else:
        return "Ainda não sei responder. Tente perguntar sobre temperatura, alerta ou previsão."


def iniciar_chatbot(temperatura_atual=22.9):
    print("=== Chatbot da estufa ===")
    print("Pergunte sobre temperatura, alerta ou previsão.")
    print("Digite 'sair' para encerrar.")

    while True:
        pergunta = input("\nVocê: ").strip()

        if pergunta.lower() == "sair":
            print("Chatbot: Até logo!")
            break

        resposta = responder(pergunta, temperatura_atual)
        print("Chatbot:", resposta)


if __name__ == "__main__":
    iniciar_chatbot()