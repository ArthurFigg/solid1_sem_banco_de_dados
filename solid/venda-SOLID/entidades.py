

# O código completo e corrigido para a classe CarrinhoDeCompras

class CarrinhoDeCompras:
    # 1. Recebe as dependências (catálogo e estoque), não as cria.
    def __init__(self, catalogo, estoque):
        self.produtos_no_carrinho = {} # Dicionário: id_produto -> quantidade
        self.catalogo = catalogo
        self.estoque = estoque

    # 2. Método indentado corretamente dentro da classe
    def adicionar_produto(self, produto, quantidade=1):
        # Usa o self.estoque que recebeu para verificar
        if self.estoque.verificar_disponibilidade(produto.id, quantidade):
            # Adiciona ao seu dicionário interno
            self.produtos_no_carrinho[produto.id] = self.produtos_no_carrinho.get(produto.id, 0) + quantidade
            print(f"{quantidade}x '{produto.nome}' adicionado(s) ao carrinho.")
        else:
            raise ValueError(f"Estoque insuficiente para o produto '{produto.nome}'.")

    # 3. Método indentado corretamente e com a lógica corrigida
    def calcular_total(self):
        total = 0
        # Percorre o seu próprio dicionário de produtos
        for id_produto, quantidade in self.produtos_no_carrinho.items():
            # Pergunta ao catálogo o preço do produto
            produto = self.catalogo.buscar_produto(id_produto)
            if produto:
                total += produto.preco * quantidade
        return total