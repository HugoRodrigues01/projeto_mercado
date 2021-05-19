

def converte_elementos(elementos: list = [], elemento: bool = False) -> str:
    """
    Essa função contém três parâmetros:
    elementos -> os elementos são os valores para iserir na tabela
        ou para pegar os elementos da tabela.
    elemento -> se essa opção for igual á False significa que 
        o tipo é para pegar elementos dentro do bando
        se não é para inserir dentro do mesmo.
    """
    valor_comvertido: str = ""
    for ele in elementos:
       
        if elemento == False:
            valor_comvertido += f'`{ele}`'
        else:
            if type(ele) == str and ele != "default":
                valor_comvertido += f'"{ele}"'
            else:
                valor_comvertido += str(ele)

        if ele == elementos[-1]:
            break
        else:
            valor_comvertido += ','
    return valor_comvertido

