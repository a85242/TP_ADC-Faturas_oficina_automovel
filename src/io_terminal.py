from tabulate import tabulate
import texto as t

def pergunta_id(questao, lista, mostra_lista=False):
    """Recebe a :attr:`questao` e guarda a como id.
    Imprime a :attr:`lista` na forma de uma tabela com um cabeçalho

    :param questao: guarda qual é o id do utilizador
    :param lista: guarda o dado na tabela
    :param mostra_lista: apresenta os dados numa tabela
    :return: apresenta a tabela 
    """

    if mostra_lista:
        imprime_lista(cabecalho="", lista=lista)

    while True:
        id = int(input(questao))
        if 0 <= id < len(lista):
            return id
        else:
            print(t.id_inexistente[t.LANG].format(len(lista)))

def pause():
    """Faz uma pausa no programa e espera que o utilizador pressione ENTER"""

    input(t.pausa[t.LANG])

def imprime_lista(cabecalho, lista):
    """Imprime a :attr:`lista` na forma de uma tabela com um cabeçalho

    Recebe uma lista na forma [{"atrib1": valor1, "atrib2": valor2, ...},
    {"atrib1": valor1, "atrib2": valor2, ...}, ...] e imprime no terminal uma tabela
    na forma

    ==  ======  ======
    id  atrib1  atrib2
    ==  ======  ======
    0   valor1  valor2
    1   ...      ...
    ==  ======  ======

    :param cabecalho: Cabecalho para a listagem
    :param lista: Lista a ser impressa
    """

    print(cabecalho)

    if (len(lista) == 0):
        print(t.lista_vazia[t.LANG])
    else:
        # cabecalho da tabela
        lista_a_imprimir = [["id"] + list(lista[0].keys())]
        # dados
        lista_a_imprimir.extend([[id] + list(d.values()) for id, d in enumerate(lista)])

        print(tabulate(lista_a_imprimir, headers="firstrow", tablefmt='psql'))
