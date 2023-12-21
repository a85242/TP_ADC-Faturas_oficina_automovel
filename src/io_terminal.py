from tabulate import tabulate
from copy import deepcopy
import texto as t

def pergunta_id(questao, lista, mostra_lista=False):
    """Recebe a :attr:`questao` e guarda-a como id.
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
        lcopia = deepcopy(lista)

        listadividida = [[{}]]
        
        lenheaders = 0
        while len(lcopia[0]) > 0:
            key = list(lcopia[0].keys()).pop(0)
            listadividida[-1][-1][key] = lcopia[0].pop(key)
            lenheaders += len(key)
            if lenheaders > 60:
                listadividida.append([{}])
                lenheaders = 0
        else:
            lcopia.pop(0)
            for elemento in lcopia:
                for l in listadividida:
                    l.append({})
                    while len(elemento) > 0:
                        key = list(elemento.keys()).pop(0)
                        if key in l[0]:
                            l[-1][key] = elemento.pop(key)
                        else:
                            break
                    
        for l in listadividida:
            # cabecalho da tabela
            lista_a_imprimir = [["id"] + list(l[0].keys())]
            # dados
            lista_a_imprimir.extend([[id] + list(d.values()) for id, d in enumerate(l)])

            print(tabulate(lista_a_imprimir, headers="firstrow", tablefmt='psql'))
