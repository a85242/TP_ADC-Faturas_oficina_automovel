from datetime import date

from io_terminal import imprime_lista, pergunta_id

nome_ficheiro_lista_de_faturas = "lista_de_faturas.pk"


def cria_nova_fatura(lista_de_clientes, lista_de_veiculos):
    """Pede ao utilizador para introduzir os dados de uma nova fatura

    :return: dicionario com uma fatura, na forma
        {"cliente": <<id_cliente>>, "veiculo": <<id_veiculo>>, "data": <<data>>, ...}
    """

    id_cliente = pergunta_id(questao="Qual o id do cliente?", lista=lista_de_clientes, mostra_lista=True)
    id_veiculo = pergunta_id(questao="Qual o id do veiculo?", lista=lista_de_veiculos, mostra_lista=True)
    desc = input("Descrição da fatura: ")

    fatura = {"cliente": id_cliente,
              "veiculo": id_veiculo,
              "data": date.today(),
              "desc": desc}

    return fatura


def imprime_lista_de_faturas(lista_de_faturas):
    """Imprime a :attr:`lista_de_faturas` na forma de uma tabela com um cabeçalho

    Recebe a lista de faturas na forma [{"cliente": valor1, "veiculo": valor2, "data": valor3,
    "desc": valor4, ...}, {"cliente": valor1, "veiculo": valor2, "data": valor3,
    "desc": valor4, ...}, ...] e imprime no terminal uma tabela na forma

    ==  =========  =========  ======  ======
    id   cliente    veiculo    data    desc
    ==  =========  =========  ======  ======
    0   valor1     valor2     valor3  valor4
    1   ...        ...        ...     ...
    ==  =========  =========  ======  ======

    :param lista_de_faturas: Lista de faturas a ser impressa
    """

    imprime_lista("listagem das faturas", lista_de_faturas)