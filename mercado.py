#!mercado/bin/python3.9

# Projeto mercado
    # esse projeto será capas de realizar as seguintes funcionalidades
    # Criar banco e tabela de dados no MySQL
    # Criar Arquivo de Configuração de banco
    # 1 cadastrar produto
    # 2 remover produto cadastrado
    # 3 adicionar produto ao carrinho
    # 4 remover produto do carrino
    # 5 finalizar compra
    # 5 registrar a compra 
 
####################################
# Versões:
  # python v3.9.4
  # jsonpickle v2.0.0
  # PyMySQL v1.0.2

####################################
# importes

import time
import pymysql
from typing import List, Dict
from models.configuracao import Config
from models.banco_mercado import BancoMercado
from utils import hoje, formatacao_real
import jsonpickle
import os
#####################################
# configuraçoẽs do banco de dados

def confg_database() -> None:
    """
    Função que Criar um menu de configurações para acesso
    au banco de dados, auterando as configurações nas portas de 
    acessso.
    """

    try:
        print('\033[1;31m=' * 50)
        print("\033[m\033[1mConfiguracoes do banco de dados\033[m\033[1;31m".center(50))
        print('=' * 50)
        print('*' * 50)

        # Menu de Configuração
        print(
            '\033[m\033[1m1 - Colocar o local do banco\n'
            '2 - Colocar o usuario do banco\n'
            '3 - Colocar a senha do banco\n'
            '4 - Trocar o nome do banco\n'
            '5 - Restauração configuracoes Padroes\n'
            '7 - Salvar Alteracoes\n'
            '111 - Help\n'
            '6 - cancelar\033[m\033[1;31m'
        )
        print('*' * 50)
        print('\033[m')

        # opção dos valores do menu
        opc: str = input("\033[1mDigite uma das opcoes acima >>> \033[m")

        # tratamento erro
        while opc not in ['1', '2', '3', '4', '5', '6', '7', '111']:
            print('\033[1;31mVoce digitou uma opcao nao existente digite novamente\033[m')
            opc: str = input("\033[1mDigite uma das opcoes acima >>> \033[m")

        if opc == "1":

            local: str = input("Digite o local onde o banco esta: ")
            conf.host = local
            conti: str = input("Voce deseja continuar alterando as configuracoes [S/N]").upper()[0]

            if conti == "S":
                confg_database()

            else:
                
                try:
                    conf.atualizar_configuracao()
                    main()

                except:
                    print('\033[1;31mErro: Atencao as configuracoes não sao validas para acessar o banco\033[m')
                    confg_database()

        elif opc == "2":

            user: str = input("Digite o Usuario do banco: ")
            conf.user = user
            conti: str = input("Voce deseja continuar alterando as configuracoes [S/N]").upper()[0]

            if conti == "S":
                confg_database()

            else:
                
                try:
                    conf.atualizar_configuracao()
                    main()

                except:
                    print('\033[1;31mErro: Atencao as configuracoes nao sao validas para acessar o banco\033[m')
                    confg_database()


        elif opc == "3":
            senha: str = input("Digite a nova senha: ")
            conf.passwd = senha

            conti: str = input("Você deseja continuar alterando as configuraçoẽs [S/N]").upper()[0]
            if conti == "S":
                confg_database()
            else:
                
                try:
                    conf.atualizar_configuracao()
                    main()

                except:
                    print('\033[1;31mErro: Atenção as configurações não são validas para acessar o banco\033[m')
                    confg_database()

        elif opc == "4":
            nome_banco: str = input("Digite o Nome do banco: ")
            conf.nome_banco = nome_banco

            conti: str = input("Voce deseja continuar alterando as configuracoes [S/N]").upper()[0]
            if conti == "S":
                confg_database()

            else:
                conf.atualizar_configuracao()

                try:

                    main()
                except:
                    print('\033[1;31mErro: Atencao as configuracoes nao sao validas para acessar o banco\033[m')
                    confg_database()

        elif opc == "5":
            conf.configuracao_padrao()

            try:   
                main()

            except:
                print('\033[1;31mErro: Atenção as configuracoes nao sao validas para asseçar o banco\033[m')
                confg_database()

        elif opc == "6":
            try:
                main()

            except:
                print('\033[1;31mErro: Atenção as configuracoes não são validas para acessar o banco\033[m')
                exit(0)


        elif opc == "7":

            try:
                conf.atualizar_configuracao()
                main()

            except:
                print('\033[1;31mErro: Atenção as configuracoes nao sao validas para acessar o banco\033[m')
                confg_database()
        
        elif opc == "111":
            print('@' * 50)
            print("""\033[1m
    Você ativou a ajuda, alguma coisas pode esta emcomandando você!,
    ATENÇÃO. Caso você não esteja conseguindo continuar,
    o problema pode estar nas configurações do banco de dados,
    se o programa não conseguir entrar no banco ele pode 
    não funcionar.
        Esse programa tem configurações padrões, ou seja o banco
    não estara com senha e no modo root caso você tenha uma banco de 
    dados,e queira testar o programa por ele altere as configurações
    do banco. Também pode ser que o usuário, que você estar usando não 
    tenha aspermissões para escrever ou ler no banco, desse jeito o 
    programa não funcionara.
            \033[m""")
            print('@' * 50)
            confg_database()

    except KeyboardInterrupt:
        print('\nSaindo...')
        time.sleep(3)
        exit(0)
    except SystemExit:
        pass
    except TypeError:
        print("\033[1;31mErro de tipo!\033[m")
    except ValueError:
        print("\033[1;31mErro de valor!\033[m")
    except IndentationError:
        print("\033[1;31mErro de indentacao!\033[m")
    except:
        print("\033[1;31mAulgo deu errado por favor tente reiniciar o programa!!\033[m")

#####################################
# main Painel

def main() -> None:
    try:
        mercado = Mercado()

        print("=" * 50)
        print('\033[1mMercado HugoMais <3\033[m'.center(50))
        print("=" * 50)

        print("#" * 50)

        print(
        '\033[1m1 - fazer compra\n'
        '2 - cadastrar produto\n'
        '3 - remover produto\n'
        '4 - Ver painel de produtos\n'
        '5 - Entrar nas configuracoes do banco\n'
        '999 - Creditos\n'
        '6 - sair\033[m'
        )
        print("#" * 50)

        opcao: str = input("\033[1;36mDigite uma das opcoes acima: \033[m")

        while opcao not in ['1', '2', '3', '4', '5', '6', '999']:
            opcao: str = input("\033[1;31mErro voce digitou uma opcao inesistente: \033[m")

        if opcao == "1":
            compra()
        elif opcao == "2":
            mercado.cadastrar_produto_no_banco()
        elif opcao == "3":
            mercado.excluir_produto_do_banco()
        elif opcao == "4":
            mercado.ver_painel_de_produtos()
        elif opcao == "5":
            confg_database()
        elif opcao == "999":
            print("-" * 50)
            print("""\033[1m
    Esse progrma foi criado pelo estudante de programacao:
    Hugo Rodrigues Pereira.
    Siga e o reposirio no GutHub: 
    >>  https://github.com/HugoRodrigues01/projeto_mercado   
            \033[m""")
            print("-" * 50)
            main()

        elif opcao == "6":
            exit(0)

        print("#" * 50)
    except KeyboardInterrupt:
        print('\nSaindo...')
        time.sleep(3)
        exit(0)
    except SystemExit:
        print("-" * 50)
        print('\033[1mObrigado por entrar no nosso programa. Volte semore :)\033[m')
        print("-" * 50)
    except TypeError:
        print("\033[1;31mErro de tipo!\033[m")
    except ValueError:
        print("\033[1;31mErro de valor!\033[m")
    except IndentationError:
        print("\033[1;31mErro de indentacao!\033[m")
    except:
        print("\033[1;31mAulgo deu errado por favor tente reiniciar o programa!!\033[m")
        confg_database()

#####################################
# Lista do carrinho de compras
lista_compras: list = [[]]
# Preço da compra
preco_compra: list = []

# Menu compra
def compra() -> None:

    def finish_compra(dinheiro: float = 0, valor_da_compra: float = 0) -> None:
        print("-" * 50)
        print(f"""\033[1;36m
           Valor total da compra: {formatacao_real(valor_da_compra)}
           Valor pago: {formatacao_real(dinheiro)}
           Troco: {formatacao_real(dinheiro - valor_da_compra)}
        \033[m""")
        print("-" * 50)
        

    global lista_compras
    mercado2 = Mercado()
    # Menu de opções
    print('\033[1m=' * 50)
    print(
        "1 - Adicionar Produto ao carrinho\n"
        "2 - Remover Produto do carrinho\n"
        "3 - Finalizar Compra\n"
        "4 - Registrar Compra\n"
        "5 - Painel de Produtos\n"
        "7 - Ver Produtos do carrinho\n"
        "6 - Voltar ao menu Principal"
    )
    print('\033[1m=' * 50)
    opc_compra: str = input("\033[1;34mDigite um dos valores acima: \033[m")

    # Tratamento de erro opções inválidas
    while opc_compra not in ["1", "2", "3", "4", "5", "7", "8", "6"]:
        print("\033[1;31mO valor Digitado não e uma opcao valida\nPor favor digite novamente!!\033[m")

        # Opção do menu compra
        opc_compra: str = input("\033[1;34mDigite um dos valores acima: \033[m")
    
    if opc_compra == "1":
        while True:

            adicionar: str = input("\033[1;34mDigito o ID do Produto.\nPara adicionar ao carrinho >>> \033[m")
            try:
                int(adicionar)
            except ValueError:
                print("\033[1;31mErro. Voce digitou um valor nao numerico\nPor vafor digite novamente.\033[m")
            else:

                # Tratamento
                try:
                    # Verificando se há mais de um mesmo produto
                    if lista_compras.count(adicionar) == 0:
                        lista_compras.append(adicionar)
                    else:
                        lista_compras[0].append(adicionar)
                except:
                    print('\033[1;31mErro\033[m')
                else:
                    print('\033[1;34mO produto foi adicionado ao carrinho com sucesso!!\033[m')
                    print(f"\033[1m{lista_compras}\033[m")

                # Contionuar adicionando ou não
                sair: str = input("\033[1;mVoce deseja continuar adicionando [S/N]?: \033[m").upper()[0]

                if sair == "N":
                    compra()
        
    elif opc_compra == "2":
        
        delet: str = input("Digite o ID do produto para removelo: ")
        cont_elementos: int = lista_compras[0].count(delet) + 1
        print(cont_elementos)
    
        if cont_elementos == 0:
            print('O elemento nao está dentro do carrinho!')
            compra()
        elif cont_elementos == 1:
            try:
                lista_compras.remove(delet)
            except:
                print("Erro nao foi possivel remover!!")
                compra()
            else:
                print("O elemento foi removido com sucesso!")
        else:
            rem: str = input(f"Existem {cont_elementos} dentro do carrinho\nDigite a quantidade que deseja remover: ")
            if int(rem) > cont_elementos:
                print(f"So existem {cont_elementos} Dentro do carrinho so eles serao removidos.")

            try:
                for e in range(int(rem)):
                    lista_compras[0].remove(delet)
            except ValueError:
                lista_compras.remove(delet)
            except:
                print("Erro nao foi possivel remover!!")
                compra()
            else:
                print("Tudo foi removido com sucesso!")

        compra()

    elif opc_compra == "3":
        """
        Opção 3 gerará um boleto com as imformações necessarias atravès 
        da lista de compras.
        """

        # Permissão para gerar o boleto
        gerar_boleto: str = input("Deseja gerar o boleto [S/N]? ").upper()[0]

        while True:
            valor_pago: str = input("Digite a o valor pago: ")
            try:
                valor_pago = float(valor_pago)
            except:
                print('\033[1;31mErro. o valor digitado nao e numerico\nPor favor digite novamente!!\033[m')
            else:
                break

        # peagando os preços para calcular o valor total das compras
        ret_preco: list = mercado2.filter_por_ids('produtos_mercado', ids=[*
        lista_compras[1:], *lista_compras[0]], parametros=['preco'])

        # inserindo os preços na lista
        for l_preco in ret_preco:
            preco_compra.append(l_preco[0][0])
        
        #  se a permissão para gerar o boleto for aceita
        if gerar_boleto == "S":
            
            # verificando se a pasta para colocar os boletos existe
            # se não exiatir ele irá criar
            if os.path.exists(f"{os.getcwd()}/boletos") == False:
                os.mkdir(f"{os.getcwd()}/boletos")

            # abrindo a pasta para colocar o boleto que será gerado
            with open(f'boletos/boleto_{hoje()}.txt', "w", encoding="UTF-8", newline="") as arq:

                # pegando os valores do banco de dados
                ret_bol: list = mercado2.filter_por_ids("produtos_mercado", ids=[*lista_compras[1:]], parametros=["id", "nome_produto", "preco"])

                # gerando o boleto
                arq.write(f"{'=' * 50}")
                arq.write(f'\n{" " * 19}BOLETO')
                arq.write(f'\n{"=" * 50}\n')

                for lis in ret_bol:

                    # pegando a quantidade de produtos dentro da lista de compras
                    cont_por_produto: int = lista_compras[0].count(str(lis[0][0])) + 1

                    arq.write(f"quantidade: {cont_por_produto} nome: {lis[0][1]}, id: {lis[0][0]}, preco: {formatacao_real(lis[0][2])}\n")

                arq.write(f"{'-' * 50}")


                arq.write(f"\nValor Total: {formatacao_real(sum(preco_compra))}")
                arq.write(f"\nDinheiro: {formatacao_real(valor_pago)}")
                arq.write(f"\nTroco: {formatacao_real(valor_pago - sum(preco_compra))}")
                arq.write(f"\n{'-' * 50}")
                arq.write(f"\nData de Geramento: {hoje()}")
                arq.write(f"\nCPF: 000.000.000-00")
                arq.write(f"\n{'*' * 50}\nObrigado pela Preferencia volte sempre :).")

                arq.write(f"\n{'=' * 50}")
            
            print('\033[1;36mO Boleto foi criado com sucesso!\033[m')
            finish_compra(valor_pago, sum(preco_compra))

            # limpandos os valores do carrinho e os preços
            lista_compras.clear()
            preco_compra.clear()

            # menu compra
            compra()

        else:
            finish_compra(valor_pago, sum(preco_compra))
            # limpandos os valores do carrinho e os preços
            lista_compras.clear()
            preco_compra.clear()
            compra()


    elif opc_compra == "4":
        pass
    elif opc_compra == "5":
        mercado2.ver_painel_de_produtos()
        compra()
    elif opc_compra == "6":
        main()
    elif opc_compra == "7":
        try:
            ret: list = mercado2.filter_por_ids('produtos_mercado', ids=[*
            lista_compras[1:]], parametros=['nome_produto', 'id', 'preco', 'tipo_do_produto'])

            for lista in ret:
                quantidade_produto: int = lista_compras[0].count(str(lista[0][1])) + 1
                print('-' * 50)
                print(f"\033[1;34mNome do Produto\033[m = \033[1;35m{lista[0][0]}\033[m")
                print(f"\033[1;34mID Do Produto\033[m = \033[1;35m{lista[0][1]}\033[m")
                print(f"\033[1;34mPreço do Produto\033[m = \033[1;35m{lista[0][2]}\033[m")
                print(f"\033[1;34mTipo do Produto\033[m = \033[1;35m{lista[0][3]}\033[")
                print(f"\033[1;34mQuantidade do produto\033[m = \033[1;35m{quantidade_produto}\033[m")
                print('-' * 50)
        
        except:
            print("\033[1;31mErro, uma das causas pode ser de ID inesistente!!\033[m")
            compra()
    
        # menu compra
        compra()
    
        

#####################################
# classe marcado

class Mercado(BancoMercado):
    def __init__(self):
        super().__init__()

    @staticmethod
    def comprar():
        carrinho: List[str] = []
    
    def cadastrar_produto_no_banco(self):
        print('=' * 50)

        print("\033[1mO codigo do produto sera adicionado automaticamente no banco.\033[m")

        nome_do_produto: str = input("\033[1;35mDigite o nome do produto: \033[m")

        descricao: str = input("\033[1;35mDigite uma descricao para o produto: \033[m")

        print('-' * 50)
        print(
            '\033[1;35mTipo do produto:\033[m\n'
            '\033[1mValores disponiveis\n'
            '1- Alimentos,\n'
            '2- Aparelhos eletronocos,\n'
            '3- Roupas,\n'
            '4- Duraveis,\n'
            '5- Moveis,\n'
            '6- Concelar\033[m'
        )
        print('-' * 50)


        opc: str = input('\033[1;35m>>> \033[m')

        while opc not in ['1', '2', '3', '4', '5', '6']:

            opc: str = input('\033[1;31mVoce Digitou uma opcao invalida >>> \033[m')
            
        if opc == '1':
            opc = 'alimentos'
        elif opc == '2':
            opc = 'eletrônico'
        elif opc == '3':
            opc = 'roupas'
        elif opc == '4':
            opc = 'duráveis'
        elif opc == '5':
            opc = 'móveis'
        elif opc == '6':
            main()
        
        try:

            preco: float = float(input("\033[1;35mDigite o preco do produto: \033[m"))

        except TypeError:

            preco: float = float(input("\033[1;31mErro valor nao numerico\nDigite novamente o valor do produto: \033[m"))
    
        except:

            print('\033[1;31mErro o valor nao será inserido no banco\033[m')
            main()

        self.inserir_dados_na_tabela('produtos_mercado', args=['default' ,nome_do_produto, descricao, str(hoje()), str(hoje()), opc, preco])
        print('=' * 50)

        main()
    
    def excluir_produto_do_banco(self):

        print('-' * 50)
        print(
            '\033[1m1- ver produtos cadastrados no banco\n'
            '2- excluir do banco\n'
            '6- cancelar\033[m'
        )
        print('-' * 50)

        excluir: str = input("\033[1;35mDigite uma opcao acima: \033[m")

        while excluir not in ['1', '2', '6']:
            excluir: str = input("\033[1;31mA opcaco nao e valida\nDigite novamente: \033[m")

        if excluir == "1":

            lista = self.ver_no_banco('produtos_mercado', parametros=['id', 'nome_produto', 'descricao', 'preco', 'tipo_do_produto'])
            print('=' * 50)
            for elemento in lista:
                print('-' * 50)
                print(f'\033[1;36m{elemento[1].upper()}\033[m')

                print(
                    f'\033[1mID = \033[m\033[1;31m{elemento[0]}\n\033[m'
                    f'\033[1mDescrição = {elemento[2]}\n'
                    f'Preço = {elemento[3]}\n'
                    f'Tipo do produto = {elemento[4]}\033[m'
                    )

                print('-' * 50)
            print('=' * 50)

            self.excluir_produto_do_banco()

        elif excluir == '2':

            codigo: str = input("\033[1;35mDigite o ID do produto: \033[m")
            seguranca: str = input("\033[1;31mTem serteza que desaja excluir\no dado permanentemente do banco? [S/N]: \033[m").upper()[0]

            if seguranca == "N":
                main()

            self.remover_produto_do_banco(codigo, 'produtos_mercado')

        elif excluir == '6':
            main()
        main()

    def test(self, com_sql='SHOW DATABASES;'):
        self.test_acesso(com_sql)     

    def ver_painel_de_produtos(self):
        """
        Essa função se connecta ao banco de dados e retornar 
        os valores das colunas escolhidas
        """
        # Menu de opções
        print('\033[1m=' * 50)
        print(
            "1 - Nome do Produto\n"
            "2 - Preco do Produto\n"
            "3 - Data de Insercao do Produto\n"
            "4 - Descrição do Produto\n"
            "5 - Data de Modificacao do Produto\n"
            "7 - Tipo do Produto\n"
            "8 - ID do Produto"
            "6 - Cancelar"
        )
        print('=' * 50)
        print(
            "!!! ATENÇÃO AS ORDENS DOS VALORES COLOCADOS SERÃO AS MESMAS\n"
            "QUE APARECERÃO NO PROMPT.\n\033[m"
        )

        # lista das opcoes escolhidas
        opcoes: list = input("\033[1;35mDigites os valores que serao apresentados\nno painel\n!SEPARANDO OS POR ',' EX: 1,2,3,4 >>> \033[m").replace(" ", "").split(',')


        # Listas de elementos convertidos
        lista_opcoes: list = []

        # convertendo os números para os nomes das colunas no banco
        for elemento in opcoes:

            if elemento == "6":
                main()
            elif elemento == "1":
                lista_opcoes.append("nome_produto")
            elif elemento == "2":
                lista_opcoes.append("preco")
            elif elemento == "3":
                lista_opcoes.append("data_insercao")
            elif elemento == "4":
                lista_opcoes.append("descricao")
            elif elemento == "5":
                lista_opcoes.append("data_de_modificacao")
            elif elemento == "7":
                lista_opcoes.append("tipo_do_produto")
            elif elemento == "8":
                lista_opcoes.append("id")

        
        # tratando erros
        try:
            resultado: list = self.ver_no_banco('produtos_mercado', parametros=lista_opcoes)

            # Criando um painel para os resultados
            print('=' * 50)
            
            for elemento in resultado:
                for valor in opcoes:

                    print(f"\033[1;34m{lista_opcoes[opcoes.index(valor)]}\033[m \033[1m=\033[m \033[1;35m{elemento[opcoes.index(valor)]}\033[m")

                print('-' * 50)

            print('=' * 50)

        except:
            print("\033[1;31mError Nao foi possivel ver o painel\npor favor verifique se digitou uma opção invalida\033[m")
            main()

        else:
            main()


if __name__ == "__main__":

    # Gerando os arquivos padroẽs e suas propriedades
    conf = Config()

    # Verificando se as configurações estão padrão
    with open("settings/conf-database.json", "r", encoding="UTF-8", newline="") as arq:

        verifica: dict = jsonpickle.decode(arq.read())

        if verifica["enter"] == False:
            confg_database()
        else:
            main()
