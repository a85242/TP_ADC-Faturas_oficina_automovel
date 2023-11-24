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

    io_terminal.imprime_lista("listagem das faturas", lista_de_faturas)