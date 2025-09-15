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

def obter_opcao_menu(): #fica repetindo até o usuário digitar uma opção válida
    while True:
        print("** Supermercado Python **")
        print("1. Adicionar item ao carrinho")
        print("2. Ver total da compra")
        print("3. Finalizar compra")
        escolha = input("Escolha uma opção (1/2/3): ").strip() #.strip remove espaços em branco e tambem quebras de linha
        if escolha in ["1", "2", "3"]:
            return escolha #sai da função retornando a escolha 
        print("Opção inválida. Tente novamente.\n")

def adicionar_item(): #esta criando uma função chamada adicionar_item
    produto = input("Digite o nome do produto: ").strip().lower() #.strip remove os espaços e .lower deixa minusculo
    if produto in ["oleo", "oleo de soja"]:
        produto = "oleo"

    if produto in ["arroz", "feijao", "oleo de soja", "oleo", "cafe", "leite"]: 
        qtd_str = input("Digite a quantidade: ")
        if qtd_str.isdigit(): #isdigit garante que só tenha digitos
            qtd = int(qtd_str)

            if produto == "arroz":
                preco_uni = arroz
            elif produto == "feijao":
                preco_uni = feijao
            elif produto == "oleo":
                preco_uni = oleo
            elif produto == "cafe":
                preco_uni = cafe
            elif produto == "leite":
                preco_uni = leite

            desconto = 0 #pra variavel sempre existir (se n da erro no append la em baixo)

            #verifica se ja existe no carrinho
            achou = False
            for item in carrinho:
                if item[0] == produto:
                    item[1] += qtd  # soma quantidade
                    subtotal = item[1] * preco_uni
                    desconto = subtotal * 0.03 if item[1] > 3 else 0
                    item[3] = subtotal - desconto
                    item[4] = desconto
                    achou = True
                    break

            #se não achou, adiciona
            if not achou:
                subtotal = qtd * preco_uni
                desconto = subtotal * 0.03 if qtd > 3 else 0
                subtotal -= desconto
                carrinho.append([produto, qtd, preco_uni, subtotal, desconto])
        else:
            print("Quantidade inválida. Digite um número inteiro.")
    else:
        print("Produto não encontrado.")

def ver_total_parcial():
    if len(carrinho) == 0: #caso n tenha nada ainda
        print("Carrinho vazio.")
    else:
        total = 0 #aq vai somar todos os subtotais
        print("\n--- Total Parcial ---")
        for item in carrinho: #
            produto = item[0]
            qtd = item[1]
            subtotal = item[3]
            nome_formatado = produto[0].upper() + produto[1:]
            #pega a 1 letra e deixa maiusculo (upper), pega o resto da string a partir do indice 1 (1:) dai faz o nome bonito concatenando ----> arroz: a -> A + rroz -> Arroz 

            print(str(qtd) + "x " + nome_formatado + " - R$ " + str(round(subtotal, 2))) #round p ficar em mercado
            total += subtotal
        print("Total até agora: R$ " + str(round(total, 2)) + "\n") #sem desconto geral

def finalizar_compra():
    if len(carrinho) == 0: #caso esteja vazio
        print("Carrinho vazio.")
        return

    print("="*25 + " RECIBO " + "="*25)
    print("------------- ITENS COMPRADOS -------------")
    print("Qtd. Produto (Preco Un.) Subtotal")
    print("-"*45)

    total = 0 #total bruto da compra
    for item in carrinho: #percorre cada item do carrinho
        produto = item[0]
        qtd = item[1]
        preco_uni = item[2]
        subtotal = item[3]
        desconto = item[4]

        total += subtotal
        nome_formatado = produto[0].upper() + produto[1:] if produto else produto

        print(str(qtd) + "x " + nome_formatado + " (R$ " + str(round(preco_uni, 2)) + "/un)  R$ " + str(round(subtotal, 2)))
        if desconto > 0: #se tiver desconto
            print("   -> Desconto de 3% por volume aplicado.")

    print("-"*45)
    print("Total Bruto: R$ " + str(round(total, 2)))
    print("Desconto da Compra (10%): R$ " + str(round(total * 0.10, 2)))
    print("-"*45)
    print("Valor Final a Pagar: R$ " + str(round(total * 0.90, 2)))
    print("="*55)
    print("Obrigado pela sua compra!")

def main():
    while True:
        opcao = obter_opcao_menu()
        if opcao == "1":
            adicionar_item()
        elif opcao == "2":
            ver_total_parcial()
        else: #se escolhe 3 chama a funcao do recibo e entao sai do loop finalizando o programa
            finalizar_compra()
            break #sai do loop

if __name__ == "__main__":
    main()