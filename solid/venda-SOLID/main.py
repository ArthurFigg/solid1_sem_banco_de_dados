from entidades import  CarrinhoDeCompras
from descontos import RegraDeDescontoFixo, RegraDeDescontoPercentual, RegraDeDesconto
from pagamentos import Pagavel, Estornavel, PagamentoCartao, PagamentoPIX
from estoque import catalogo, estoque, Produto
from processador import ProcessadorDePedidos


def main():
    
    meu_catalogo = catalogo()
    meu_estoque = estoque()

    # Adicionando produtos ao catálogo
    produto1 = Produto(1, "Produto A", 50.0)
    produto2 = Produto(2, "Produto B", 75.0)
    
    meu_catalogo.adicionar_produto(produto1)
    meu_catalogo.adicionar_produto(produto2)

    # Adicionando estoque para os produtos
    meu_estoque.adicionar_estoque(produto1.id, 2)
    meu_estoque.adicionar_estoque(produto2.id, 1)

    # Criando o carrinho de compras
    carrinho = CarrinhoDeCompras(meu_catalogo, meu_estoque)

    # Adicionando produtos ao carrinho
    carrinho.adicionar_produto(produto1, 2)
    carrinho.adicionar_produto(produto2, 1)

    # Calculando o total do carrinho
    total = carrinho.calcular_total()
    print(f"Total do carrinho: R${total:.2f}")

    # Configurando regras de desconto
    desconto_fixo = RegraDeDescontoFixo(20)  # Desconto fixo de R$20
    desconto_percentual = RegraDeDescontoPercentual(10)  # 10% se total > 100
    regras_de_desconto = [desconto_fixo, desconto_percentual]

    # Escolhendo o método de pagamento
    metodo_pagamento = PagamentoCartao()  
    # metodo_pagamento = PagamentoPIX()
    processador = ProcessadorDePedidos(carrinho, regras_de_desconto, metodo_pagamento)
    processador.processar_pedido()

if __name__ == "__main__":
    main()