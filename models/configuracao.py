######################
# imports

import os
import jsonpickle
#######################

class Config:

    def __init__(self):
        self.gerar_arquivos_de_configuracao()

        # abrindo o arquivo json em modo de leitura
        with open("settings/conf-database.json", "r", encoding="UTF-8") as arq_r:
            # lendo o arquivo json e transformando em dict
            self.__arquivo_confg = jsonpickle.decode(arq_r.read())
            
        
        self.__host: str = self.__arquivo_confg["conf_assece"]["local"]
        self.__user: str = self.__arquivo_confg["conf_assece"]["user"]
        self.__passwd: str = self.__arquivo_confg["conf_assece"]["password"]
        self.__nome_banco: str = self.__arquivo_confg["conf_assece"]["database_name"]

    @property
    def host(self):
        return self.__host
    
    @property
    def user(self):
        return self.__user
    
    @property
    def passwd(self):
        return self.__passwd

    @property
    def nome_banco(self):
        return self.__nome_banco
    
    @host.setter
    def host(self, novo_host: str):
        self.__host = novo_host
    
    @user.setter
    def user(self, novo_user: str):
        self.__user = novo_user
    
    @passwd.setter
    def passwd(self, novo_passwd):
        self.__passwd = novo_passwd
    
    @nome_banco.setter
    def nome_banco(self, novo_nome_banco):
        self.__nome_banco = novo_nome_banco

    def gerar_arquivos_de_configuracao(self) -> None:
        try:
            # abrindo o arquivo somente se não existir
            with open("settings/conf-database.json", "x", encoding='UTF-8', newline='') as arq:
                
            # Arquivo de configuração do banco de dados
                confg: dict = {
                    "conf_assece": {
                        "database_name": "mercado",
                        "local": "localhost",
                        "user": "root",
                        "password" : ""
                    },
                    "enter": False
                }
                escrever = jsonpickle.encode(confg)
                arq.write(escrever)
        except FileExistsError:
            pass

    def atualizar_configuracao(self) -> None:
        """
        Entrara nas configurações do banco e modificara suas propriedades
        de acordo com o que voce escolher.
        """

        # abrindo o arquivo json em mode de Leitura
        with open("settings/conf-database.json", "r", encoding="UTF-8") as arq_r:


            # convertendo o dicionario alterado para arquivo json
            escrever: str = jsonpickle.decode(arq_r.read())

            # alterando as informações dos parâmetros self
            escrever["conf_assece"]["database_name"] = self.nome_banco
            escrever["conf_assece"]["local"] = self.host
            escrever["conf_assece"]["user"] = self.user
            escrever["conf_assece"]["password"] = self.passwd
            escrever["enter"] = True

            # atualizando o arquivo de configurações
            with open('settings/conf-database.json', 'w', encoding="UTF-8", newline='') as arq_w:
                write = jsonpickle.encode(escrever)
                arq_w.write(write)
    
    def configuracao_padrao(self) -> None:
        os.remove("settings/conf-database.json")
        self.gerar_arquivos_de_configuracao()
