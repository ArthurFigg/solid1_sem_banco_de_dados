class ProcessadorDePedidos:
    def __init__(self, carrinho, lista_de_regras, processador_pagamento):
        self.carrinho = carrinho
        self.lista_de_regras = lista_de_regras
        self.processador_pagamento = processador_pagamento

    def processar_pedido(self):
        if not self.carrinho.produtos_no_carrinho:
            print("O carrinho está vazio. Adicione itens para processar o pedido.")
            return
        
        print("--- Iniciando processamento do pedido ---")
        
        total_bruto = self.carrinho.calcular_total()
        
        desconto_total = 0
        for regra in self.lista_de_regras:
            desconto_total += regra.calcular_desconto(self.carrinho)
            
        total_final = total_bruto - desconto_total
        total_final = max(0, total_final)

        print(f"Total Bruto: R${total_bruto:.2f}")
        print(f"Total de Descontos: R${desconto_total:.2f}")
        print(f"Valor a Pagar: R${total_final:.2f}")
        
        print("\nIniciando pagamento...")
        self.processador_pagamento.pagar(total_final)
        
        print("\n--- Pedido Finalizado com Sucesso! ---")


