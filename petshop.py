#Função para questionar ao usuário o PESO do cachorro
#Repete até o momento em que for preenchido um peso menor que 50Kg
def cachorro_peso():
    while True:
        try:
            peso = int(input('Entre com o peso do cachorro: '))
        except:
            print('Você digitou um avalor não numérico')
            print('Por favor entre com o peso do cachorro novamente.\n')
        else:
            if(peso < 3):
                preco_base = 40
            elif(peso < 10):
                preco_base = 50
            elif(peso < 30):
                preco_base = 60
            elif(peso < 50):
                preco_base = 70
            elif(peso >= 50):
                print('Não aceitamos cachorros tão grandes.')
                print('Por favor entre com o peso do cachorro novamente.\n')
                continue
            return preco_base #retorna o preço referente ao peso do cachorro

#Função para questionar ao usuário o PELO do cachorro
#Repete até o momento em que for selecionado alaguma das opções (c /m /l)
def cachorro_pelo():
    while True:
        pelo = (input('\nEntre com o pelo do cachorro \nc - Pelo Curto \nm - Pelo Médio \nl - Pelo Longo \n>> '))
        if(pelo == 'c'):
            return 1.0 #retorna o valor com base na pelagem do cachorro
        elif(pelo == 'm'):
            return 1.5 #retorna o valor com base na pelagem do cachorro
        elif (pelo == 'l'):
            return 2.0 #retorna o valor com base na pelagem do cachorro
        else:
            print('Você digitou um valor diferente de ( c/ m/ l)')
            print('Por favor entre com o peso do cachorro novamente.')
            continue

#Função para questionar ao usuário se o mesmo deseja algum adicional
#Repete até o momento em que for selecionado a opção (0)
def cachorro_extra():
    soma_adicionais = 0
    while True:
        print('\nDeseja adicionar mais algum serviço?')
        print('1 - Corte de Unhas - R$ 10,00')
        print('2 - Escovar dentes - R$ 12,00')
        print('3 - Limpeza de Orelhas - R$ 15,00')
        print('0 - Não desejo mais nada')
        try:
            adicional = int(input('>> '))
        except ValueError:
            print('Você digitou um valor diferente de (0/ 1/ 2/ 3)')
            print('Por favor, digite novamente.')
        else:
            if(adicional == 1):
                soma_adicionais = soma_adicionais + 10
            elif(adicional == 2):
                soma_adicionais = soma_adicionais + 12
            elif(adicional == 3):
                soma_adicionais = soma_adicionais + 15
            elif(adicional == 0):
                break
            else:
                print('Você digitou um valor diferente de (0/ 1/ 2/ 3)')
                print('Por favor, digite novamente.')
                continue
            continue
    return soma_adicionais #retorna a soma dos adicionais selecionados

#---------------------------------------------------------------------------- Main
print('Seja bem-vindo ao PetShop do Jean Amaral\n') #mensagem de boas-vindas

peso = cachorro_peso() #recebendo o resultado da função
pelo =  cachorro_pelo() #recebendo o resultado da função
adicionais = cachorro_extra() #recebendo o resultado da função

valor_total = peso * pelo + adicionais #cálculo do valor total do pedido

#Print do valor total do pedido
print('\nTotal a pagar: R${:.2f} (peso: {} * pelo: {} + adicional(is): {})'.format(valor_total, peso, pelo, adicionais))