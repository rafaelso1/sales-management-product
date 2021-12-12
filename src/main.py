import os
import color

os.system("cls")
colors = color.Colors()

# Adiciona uma venda 
def adiciona(list, sellers):
    global id
    id += 1
    sales = {
        "ID": id,
        "Seller Name": input("\nPor favor, insira o primeiro nome dentre os vendedores\nRafael Soares da Silva\nAnderson Abrahão Santos\nClayton Nogueira da Silva\nLudmilla Silva Dutra\nJennifer Augusto Almeida: "),
        "Customer Name": input('Nome do Cliente: '),
        "Date of Sale": input('Data da Venda: '),
        "Sale Item Name": input('Nome do item vendido: '),
        "Sale Value": float(input('Valor da Venda: R$'))
    }

    name = sales["Seller Name"]

    found = vendedor(name, sellers)

    if found:
        list.append(sales)
        print(colors.GREEN + '\nVenda registrada com sucesso!' + colors.END)
        lista_vendas(list)
    else:
        print(colors.RED + '\nVendedor não registrado!' + colors.END)
        id -= 1
        lista_vendas(list)

#Traz se encontrou o vendedor escrito.
def vendedor(name, sellers):
    for i in range(len(sellers)):
        firstName = sellers[i].split()[0]
        if name == firstName:
            found = True
            break
        else:
            found = False

    return found


# Edita a venda
def edita(list, sellers):
    if len(list) > 0:
        change_id = int(input('\nColoque com o código da venda para editar o produto: '))
        for i in range(len(list)):
            if list[i]['ID'] == change_id:
                if verifica_venda(change_id, list):
                    while True:
                        print(colors.YELLOW + '\n--- Editor de vendas ---\n' + colors.END)
                        print('O que deseja editar? ')
                        print('[1] Nome do Vendedor')
                        print('[2] Nome do Cliente')
                        print('[3] Data da Venda')
                        print('[4] Nome do Item Vendido')
                        print('[5] Valor da Venda')

                        option = int(input('\nColoque com a opção correspondente: '))

                        if option == 1:
                            name = input("\nColoque o novo nome do vendedor: ")
                            found = vendedor(name, sellers)

                            if found:
                                list[i]['Seller Name'] = name
                                print(colors.GREEN + "\nO nome do vendedor foi alterado com sucesso!" + colors.END)

                            else:
                                print(colors.RED + "\nNome não registrado!" + colors.END)

                            break

                        elif option == 2:
                            list[i]['Customer Name'] = input("\nColoque o nome do cliente: ")
                            print(colors.GREEN + "\nO nome do cliente foi alterado com sucesso!" + colors.END)
                            break

                        elif option == 3:
                            list[i]['Date of Sale'] = input("\nColoque a data da venda: ")
                            print(colors.GREEN + "\nA data da venda foi alterada com sucesso!" + colors.END)
                            break

                        elif option == 4:
                            list[i]['Sale Item Name'] = input("\nColoque o nome do item da venda: ")
                            print(colors.GREEN + "\nO nome do item vendido foi alterado com sucesso!" + colors.END)
                            break

                        elif option == 5:
                            list[i]['Sale Value'] = float(input("\nColoque o valor do item: R$"))
                            print(colors.GREEN + "\nO valor do item foi alterado com sucesso!" + colors.END)
                            break

                        else:
                            print(colors.RED + '\nOpção Inválida, tente novamente!' + colors.END)

                lista_vendas(list)
                break

        else:
            print(colors.RED + "\nSem venda registrada com este Código!" + colors.END)

    else:
        print(colors.RED + "\nNão tem venda registrada!" + colors.END)


# Verifica se existe a venda
def verifica_venda(id, list):
    if len(list) > 0:
        for sales in list:
            if sales['ID'] == id:
                return True

    return False


# Remove uma venda
def remove(list):
    if len(list) > 0:
        del_id = int(input("\nColoque o código da venda: "))
        if verifica_venda(del_id, list):
            for i in range(len(list)):
                if list[i]['ID'] == del_id:
                    del list[i]
                    print(colors.GREEN + "\nVenda Removida!" + colors.END)
                    lista_vendas(list)
                    break

        else:
            print(colors.RED + "\nSem venda registrada com este código!" + colors.END)

    else:
        print(colors.RED + "\nNão existe vendas!" + colors.END)


# Ordena as vendas baseadas pelo valor
def order(e):
    return e['Sale Value']


# Mostra a lista de vendas
def lista_vendas(list):
    print(colors.YELLOW + "\n--- Lista de Vendas ---\n" + colors.END)
    list.sort(reverse=True, key=order)

    if len(list) > 0:
        for sales in list:
            print("Código da venda: {}".format(sales['ID']),
                  "Nome do Vendedor: {}".format(sales['Seller Name']),
                  "Nome do Cliente: {}".format(sales['Customer Name']),
                  "Data da Venda: {}".format(sales['Date of Sale']),
                  "Nome do Item Vendido: {}".format(sales['Sale Item Name']),
                  "Valor da Venda: R${}".format(sales['Sale Value']),
                  sep='     ')
    else:
        print(colors.RED + "Sem venda registrada!" + colors.END)


# Mostra os vendedores dentro da base de dados
def lista_vendedores(list):
    print(colors.YELLOW + "\n--- Lista de Vendedores---\n" + colors.END)
    for i in range(0, len(list)):
        print(list[i])


def clear():
    input(colors.GREEN + "\nAperte Enter para continuar..." + colors.END)
    os.system("cls")


id = 0


# Main
def main():
    list = []
    sellers = ['Rafael Soares da Silva', 'Anderson Abrahão Santos', 'Clayton Nogueira da Silva', 'Ludmilla Silva Dutra', 'Jennifer Augusto Almeida']

    while True:
        print(colors.YELLOW + '\n--- Gerenciador de Vendas ---\n' + colors.END)
        print('[1] Registrar Venda')
        print('[2] Editar Venda')
        print('[3] Remover Venda')
        print('[4] Listar Vendas')
        print('[5] Listar Vendedores')
        print('[6] Sair')

        option = int(input('\nColoque a opção correspondente: '))

        if option == 1:
            adiciona(list, sellers)

        elif option == 2:
            edita(list, sellers)

        elif option == 3:
            remove(list)

        elif option == 4:
            lista_vendas(list)

        elif option == 5:
            lista_vendedores(sellers)

        elif option == 6:
            print(colors.GREEN + '\nFim do programa, espero vê-lo novamente!' + colors.END)
            break
        else:
            print(colors.RED + '\nOpção inválida, tente novamente!' + colors.END)

        clear()


if __name__ == "__main__":
    main()
