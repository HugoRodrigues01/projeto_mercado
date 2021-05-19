
########################
# importes
import pymysql
import jsonpickle
from models.configuracao import Config
from utils.helper_banco import converte_elementos

########################
class BancoMercado:

    def __init__(self):
        
        # Gerando as configurações
        Config()
        # Abrindo o arquivo de configuração para os dados do bando
        with open("settings/conf-database.json", "r", encoding="UTF-8") as arq:
            self.__confg: dict = jsonpickle.decode(arq.read())

        # Atributos do banco
        self.__nome_banco: str = self.__confg["conf_assece"]["database_name"]
        self.__localhost: str = self.__confg["conf_assece"]["local"]
        self.__user: str = self.__confg["conf_assece"]["user"]
        self.__senha: str = self.__confg["conf_assece"]["password"]

        # criando o banco e tabelas se elas não existirem
        self.criar_banco()
        self.ciar_tabelas()

        # coneção do banco universal
        self.banco = pymysql.connect(
            host=self.localhost,
            user=self.user,
            passwd=self.senha,
            database=self.nome_banco
        )

        # cursor universal
        self.cursor = self.banco.cursor()
       
    @property
    def localhost(self):
        return self.__localhost
    
    @property
    def nome_banco(self):
        return self.__nome_banco
    
    @property
    def user(self):
        return self.__user
    
    @property
    def senha(self):
        return self.__senha
    

    def criar_banco(self) -> None:
     
        banco = pymysql.connect(
            host= self.__localhost,
            user= self.__user,
            passwd= self.__senha
        )
       
       
        cursor = banco.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{self.__nome_banco}`;")
        banco.commit()
    
    def ciar_tabelas(self, tabela_produtos: str='produtos_mercado') -> None:
        """
        O banco tera duas entidades, sendo elas a entidade usúarios e produtos,
        logo seŕa um relacionamento de muintos para muintos, então se criara uma 
        terceira chamada "relacao_user_produto"
        """

        # assesando o banco
        banco_criar_tabela = pymysql.connect(
            host=self.__localhost,
            user=self.__user,
            passwd=self.__senha,
            database=self.__nome_banco
        )
        # criando o cursor
        cursor_criar_tabela = banco_criar_tabela.cursor()

        com_sql = f"""CREATE TABLE IF NOT EXISTS `{tabela_produtos}` (
            `id` INT(11) NOT NULL AUTO_INCREMENT,
            `nome_produto` VARCHAR(100) NOT NULL DEFAULT('empty'),
            `descricao` VARCHAR(300) NOT NULL DEFAULT('empty'),`data_de_modificacao` DATE NOT NULL,
            `data_insercao` DATE NOT NULL,
            `tipo_do_produto` ENUM('eletrônico', 'alimentos', 'roupas', 'duráveis','móveis') NOT NULL,
            `preco` FLOAT NOT NULL DEFAULT(0.0),
            PRIMARY KEY(`id`))CHARSET=UTF8;
            """
        com_sql2 = f"""CREATE TABLE IF NOT EXISTS usuarios (
            `id` INT(11) NOT NULL AUTO_INCREMENT,
            `nome_loja` VARCHAR(50) NOT NULL DEFAULT('empty'),
            `data_modificacao` DATE NOT NULL,
            `data_insersao` DATE NOT NULL,
            `senha` VARCHAR(16) NOT NULL,
            PRIMARY KEY(`id`)
            )CHARSET=UTF8;
           """
        com_sql3 = f"""
         CREATE TABLE IF NOT EXISTS `relacao_user_produto`(
            `id` INT(11) NOT NULL AUTO_INCREMENT,
            `id_user` INT(11) NOT NULL,
            `id_produto` INT(11) NOT NULL,
            `data_modificacao` DATE NOT NULL,
            `data_insersao` DATE NOT NULL,
            PRIMARY KEY(`id`),
            FOREIGN KEY(`id_user`) REFERENCES `{tabela_produtos}` (`id`),
            FOREIGN KEY(`id_produto`) REFERENCES `{tabela_produtos}` (`id`)
            )CHARSET=UTF8;"""
        
        # executando o comando sql
        cursor_criar_tabela.execute(com_sql)
    
    def inserir_dados_na_tabela(self, nome_tabela: str, args: list = []) -> None:

        valores: str = converte_elementos(args, elemento=True)
       
        com_sql_add = f"""
        INSERT INTO `{nome_tabela}` VALUES ({valores});
        """
        try:
            self.cursor.execute(com_sql_add)
            self.banco.commit()
        except pymysql.err.DataError:
            print('\033[1;31mDeu Erro voce digitou um ENUM errado!\033[m')
        else:
            print('\033[1;35mDeu certo foi inserido!\033[m')
    
    def remover_produto_do_banco(self, id: int, nome_tabela: str) -> None:
        """
        Essa função remove um registro do banco
        id -> recebe o id do registro a ser excluido.
        nome_tabela -> nome da tabela desejada para e exclusão.
        """
        try:
            com_sql_delete = f"DELETE FROM `{nome_tabela}` WHERE `id` = {id};"
            self.cursor.execute(com_sql_delete)
            self.banco.commit()
        except:
            print('-' * 50)
            print("\033[1;31mErro nao foi possivel excluir tente novamente!\nProvavelmente o valor nao existe.\033[m")  
            print("-" * 50) 
        else:
            print('\033[1;32mDeu certo o dado foi excluido com sucesso!\033[m')
        
    def ver_no_banco(self, nome_tabela: str, parametros: list = []) -> list:
        """
        Recebe dois parâmetros, nome_tabela(nome da tabela do banco que você deseja ver),parametros (recebe os parâmetros que serão filtrados) é retornar uma
        lista contendo tuplas com os valores dos parmetros que você escolheu.
        """

        valores: str = converte_elementos(elementos=parametros)
        
        # executando o comando sql no banco
        try:
        
            com_sql_ver = f"""SELECT {valores} FROM `{nome_tabela}`;"""
            self.cursor.execute(com_sql_ver)
        except:
           print('\033[1;31merro\033[m')

        # retornando os valores pedidos
        return list(self.cursor)

    def filter_por_ids(self, nome_tabela: str, ids: list = [], parametros: list = []) -> list:
        
        valores: str = converte_elementos(elementos=parametros)
    
        list_ret: list = []
        for iden in ids:
            com_sql = (f"""
            SELECT {valores} FROM `{nome_tabela}` WHERE `id` = {iden};
            """)
          
            self.cursor.execute(com_sql)
            
            list_ret.append(list(self.cursor))
         
        return list_ret

    def filtrar_por_data(self, data: str):
        pass

    def filtrar_por_preco(self):
        pass

    def filtrar_por_tipo(self):
        pass 

    def atualisar_campo(self):
        pass       

    def test_acesso(self, com_sql: str):

        # condo o acesso ao banco
        banco_test = pymysql.connect(
            host=self.localhost,
            user=self.user,
            passwd=self.senha,
            database=self.nome_banco
        )

        # Criando o cursor
        cursor_test = banco_test.cursor()

        # executando o comando test
        cursor_test.execute(com_sql)
        banco_test.commit()