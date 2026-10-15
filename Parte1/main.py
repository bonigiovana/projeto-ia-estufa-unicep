from collections import deque

class SistemaIoT:
    """Gerencia leituras simuladas de temperatura."""

    def __init__(self):
        # Este atributo guarda os dados do sistema.
        self.leituras = [22.5, 23.1, 21.8, 24.0, 22.9]
        self.fila_processamento = deque()
        self.pilha_acoes = []
        self.configuracoes = {
            "nome": "Estufa didática",
            "cultura": "tomate (exemplo)",
            "limite_alerta_c": 30.0
        }

    def inserir_leitura(self):
        """Pede uma nova temperatura e guarda na lista."""
        try:
            temperatura = float(input("Digite a temperatura (°C): "))
            self.leituras.append(temperatura)
            self.fila_processamento.append(temperatura)
            self.pilha_acoes.append(
    f"Adicionou a leitura de {temperatura:.1f} °C"
)
            print(f"Leitura de {temperatura:.1f} °C adicionada.")
        except ValueError:
            print("Entrada inválida. Digite um número, por exemplo: 23.5")

    def exibir_leituras(self):
        """Mostra todas as temperaturas guardadas."""
        if not self.leituras:
            print("Ainda não há leituras.")
            return

        print("\nLeituras de temperatura:")
        for numero, temperatura in enumerate(self.leituras, start=1):
            print(f"{numero}. {temperatura:.1f} °C")

    def exibir_estatisticas(self):
        """Calcula e mostra estatísticas das leituras."""
        if not self.leituras:
            print("Não há leituras para calcular estatísticas.")
            return

        quantidade = len(self.leituras)
        media = sum(self.leituras) / quantidade

        variancia = sum(
            (leitura - media) ** 2 for leitura in self.leituras
        ) / quantidade

        desvio_padrao = variancia ** 0.5

        print("\n=== Estatísticas das leituras ===")
        print(f"Quantidade de leituras: {quantidade}")
        print(f"Média: {media:.2f} °C")
        print(f"Variância: {variancia:.2f} °C²")
        print(f"Desvio padrão: {desvio_padrao:.2f} °C")

    def simular_ia(self):
        """Faz uma demonstração simples com a leitura mais recente."""
        if not self.leituras:
            print("Adicione uma leitura antes de simular a análise.")
            return

        ultima_leitura = self.leituras[-1]
        limite = self.configuracoes["limite_alerta_c"]

        if ultima_leitura >= limite:
            print(
                f"Alerta: temperatura elevada detectada "
                f"na {self.configuracoes['nome']}."
            )
        else:
            print("Nenhum alerta de temperatura elevada.")


    def exibir_probabilidades(self):
        """Mostra exemplos de probabilidade aplicados à estufa."""
        if not self.leituras:
            print("Adicione leituras antes de calcular a probabilidade.")
            return

        limite = self.configuracoes["limite_alerta_c"]
        temperaturas_altas = [
            temperatura
            for temperatura in self.leituras
            if temperatura >= limite
        ]

        probabilidade_observada = (
            len(temperaturas_altas) / len(self.leituras)
        )

        print("\n=== Exemplos de probabilidade ===")
        print(
            "Probabilidade observada de temperatura alta "
            f"(>= {limite} °C): {probabilidade_observada:.1%}"
        )

        # Exemplo hipotético: 12 de 30 leituras da tarde foram altas.
        altas_a_tarde = 12
        total_a_tarde = 30
        probabilidade_condicional = altas_a_tarde / total_a_tarde

        print(
            "Exemplo condicional: probabilidade de temperatura alta "
            f"à tarde = {altas_a_tarde}/{total_a_tarde} "
            f"= {probabilidade_condicional:.1%}"
        )

        # Exemplo hipotético de um sensor de alerta.
        prob_alta = 0.20
        prob_alerta_se_alta = 0.90
        prob_alerta_se_normal = 0.10

        prob_alta_se_alerta = (
            prob_alta * prob_alerta_se_alta
            / (
                prob_alta * prob_alerta_se_alta
                + (1 - prob_alta) * prob_alerta_se_normal
            )
        )

        print(
            "Exemplo de Bayes: se o sensor emitir alerta, "
            "a probabilidade estimada de a temperatura estar alta é "
            f"{prob_alta_se_alerta:.1%}"
        )

    def processar_proxima_leitura(self):
        """Processa a próxima leitura que chegou à fila."""
        if not self.fila_processamento:
            print("Não há leituras aguardando processamento.")
            return

        temperatura = self.fila_processamento.popleft()
        self.pilha_acoes.append(
    f"Processou a leitura de {temperatura:.1f} °C"
)
        print(f"Leitura de {temperatura:.1f} °C processada.")

    def exibir_historico(self):
        """Mostra as ações mais recentes primeiro."""
        if not self.pilha_acoes:
            print("Ainda não há ações no histórico.")
            return

        print("\n=== Histórico de ações (mais recente primeiro) ===")
        for numero, acao in enumerate(
            reversed(self.pilha_acoes), start=1
        ):
            print(f"{numero}. {acao}")

    def mostrar_menu(self):
        """Exibe as opções do programa."""
        print("\n=== Sistema Inteligente de Monitoramento IoT ===")
        print("1 - Inserir leitura de temperatura")
        print("2 - Exibir leituras")
        print("3 - Exibir estatísticas")
        print("4 - Simular análise inteligente")
        print("5 - Exibir exemplos de probabilidade")
        print("6 - Processar próxima leitura")
        print("7 - Exibir histórico de ações")
        print("8 - Sair")

    def executar(self):
        """Executa o menu até a pessoa escolher sair."""
        while True:
            self.mostrar_menu()
            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                self.inserir_leitura()
            elif opcao == "2":
                self.exibir_leituras()
            elif opcao == "3":
                self.exibir_estatisticas()
            elif opcao == "4":
                self.simular_ia()
            elif opcao == "5":
                self.exibir_probabilidades()
            elif opcao == "6":
                self.processar_proxima_leitura()
            elif opcao == "7":
                self.exibir_historico()
            elif opcao == "8":
                print("Programa encerrado.")
                break
            else:
                print("Opção inválida. Escolha um número de 1 a 8.")


if __name__ == "__main__":
    sistema = SistemaIoT()
    sistema.executar()