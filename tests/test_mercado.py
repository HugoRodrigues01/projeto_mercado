lista: list = [['2', '2', '12','22', '22', '22'],'12', '22', '29', '23', '2']
print(lista)
import os

"""for n in lista:
    if type(n) == list:
        pass
    else:
        numero_de_itens: int = lista[0].count(n) + 1
        if numero_de_itens == 0:
            numero_de_itens += 1
        print(f'N = {numero_de_itens} {n}.nome_produto')"""

"""delet: str = input("Digite o ID para a remoção dele do carrinho: ")
for e in lista:
    if e == delet:
        elementos = lista[0].count(e) + 1
        print(f'Exixtem {elementos} elementos dentro de seu carrinho!')
        print('Digite quantos você deseja remover')
        rem: str = input("Digite o numero de elementos para a remoção: ")
        if int(rem) > elementos:
            print(f"Só existem {elementos} dentro do carrinho só eles seram removidos")
        try:
            for n in range(int(rem)):
                lista[0].remove(delet)
        except ValueError:
            lista.remove(delet)
        
        
print(lista)
#lista.remove(delet)"""


lis = [
    (12, "macarão", "5", 4.50),
    (1, "arroz", "6", 6.70),
    (4, "macarão", "5", 4.50),
    (5, "bolinho de chocolate", "5", 4.50)
    ]

print(lis)

print("=" * 50)
print(" " * 19, 'BOLETO')
print("=" * 50)
for t in lis:
    print(f"quantidade: {t[0]}, nome: {t[1]}, id: {t[2]}, preco: {t[3]}")
print('-' * 50)
print("Valor Total: R$1,234.00")
print('Dinheiro: R$2,000.00')
print('Troco: R$50.00')
print("-" * 50)
print("Data de geramento: 2021-03-10")
print('CPF: 000.000.000-00')
print('*' * 50)
print("Obrigado pela preferencia. Volte sempre :).")
print("=" * 50)

"""
                for preco in ret:
                    print(preco[0][0])
                    preco_compra.append(preco[0][0])
                    # soamndo todos os preços dos produtos no carrinho
                    print(preco_compra)
                    print(f'O valor total foi de = {formatacao_real(sum(preco_compra))}')
                    preco_compra.clear()"""
                """arq.write(
                    f"Valor Total: {formatacao_real()}"
                    )"""