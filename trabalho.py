"""
Supermercado Python - Projeto M1
Ana Carolina Alquini Knoll - 8482209
Miguel Vanelli -
Izabela Andreza -
"""

arroz = 25.50
feijao = 8.90
oleo = 7.00
cafe = 50.00
leite = 4.50

carrinho = []

def adicionar_item(): #esta criando uma função chamada adicionar_item
    produto = input("Digite o nome do produto: ").strip().lower() #.strip remove os espaços e .lower deixa minusculo
    if produto == "arroz" or produto == "feijao" or produto == "oleo de soja" or produto == "oleo" or produto == "cafe" or produto == "leite":
        qtd_str = input("Digite a quantidade: ")

        if qtd_str.isdigit(): #isdigit garante que só tenha digitos
            qtd = int(qtd_str) #converte para inteiro

            if produto == "arroz":
                preco_uni = arroz
            elif produto == "feijao":
                preco_uni = feijao
            elif produto == "oleo de soja" or produto == "oleo":
                preco_uni = oleo
            elif produto == "cafe":
                preco_uni = cafe
            elif produto == "leite":
                preco_uni = leite

            subtotal = qtd * preco_uni

            if qtd > 3: #da desconto se comprar mais q 3 unidades
                desconto = subtotal * 0.03
                subtotal = subtotal - desconto
                print("-> Desconto de 3% por comprar mais de 3 unidades.")

            carrinho.append([produto, qtd, preco_uni, subtotal]) #adiciona no carrinho, armazena o nome do produto, qtd, preço e o subtotal
        else:
            print("Quantidade inválida. Digite um número inteiro.")
    else:
        print("Produto não encontrado.")
