import datetime

def hoje():
    """
    Essa função retornar a data do dia.
    """
    return datetime.date.today()


def formatacao_real(numero: float) -> str:
    """
    Essa função recebe um float e retorna ele com a formatação do real 
    representada no brasi.
    """

    return f"R$ {numero:,.2f}"

#def formatacao_cpf(string: str = "000.000.000-00"):
    """
    Essa função codifica uma string para ser um formato cpf e o retornar.
    """
    #for ele in string:
    #    print(ele)
    #    if ele == "-":
    #        string = string.replace(f"-", "")
    #        print('s')
    #    elif ele == ".":
    #        string = string.replace(".", "")
    #        print('s-2')
    #    elif ele == " ":
    #       string = string.replace(" ", "")

                
