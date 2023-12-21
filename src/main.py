from clientes import cria_novo_cliente, imprime_lista_de_clientes
from faturas import cria_nova_fatura, imprime_lista_de_faturas
from io_ficheiros import (carrega_as_listas_dos_ficheiros,
                          guarda_as_listas_em_ficheiros)
from io_terminal import pause
from veiculos import cria_novo_veiculo, imprime_lista_de_veiculos
import texto as t

def menu():
    """Menu principal da aplicação"""

    lista_de_veiculos = []
    lista_de_clientes = []
    lista_de_faturas = []

    while True:
        print("""
        *********************************************************************
        :    (-: OFICINA BARATINHA - RESISTIMOS A QUALQUER ORÇAMENTO :-)    :
        *********************************************************************
        :                                                                   :\n""",
'       : nc - {: <20}'.format(t.novo_cliente[t.LANG]),'lc - {: <34}'.format(t.list_clientes[t.LANG]),":\n",
'       : nv - {: <20}'.format(t.novo_veiculo[t.LANG]),'lv - {: <34}'.format(t.list_veiculos[t.LANG]),":\n",
'       : nf - {: <20}'.format(t.nova_fatura[t.LANG]),'lf - {: <34}'.format(t.list_faturas[t.LANG]),":\n",
'       : ...                                                               :\n',
'       : g - {: <20} '.format(t.guarda_tudo[t.LANG]),' c - {: <34}'.format(t.carrega_tudo[t.LANG]),":\n",
'       : x - {: <20} '.format(t.sair[t.LANG]),' l - {: <34}'.format(t.mudarlg[t.LANG]),":\n",
"""       :                                                                   :
        *********************************************************************
        """)

        op = input(t.opcao[t.LANG]).lower()

        if op == "x":
            exit()

        elif op == "l":
            t.mudar_lingua()

        elif op == "g":
            guarda_as_listas_em_ficheiros(lista_de_veiculos, lista_de_clientes, lista_de_faturas)

        elif op == "c":
            lista_de_veiculos, lista_de_clientes, lista_de_faturas = carrega_as_listas_dos_ficheiros()

        elif op == "nc":
            novo_cliente = cria_novo_cliente()
            if novo_cliente is not None:
                lista_de_clientes.append(novo_cliente)

        elif op == "nv":
            novo_veiculo = cria_novo_veiculo()
            if novo_veiculo is not None:
                lista_de_veiculos.append(novo_veiculo)

        elif op == "nf":
            if len(lista_de_clientes) == 0 or len(lista_de_veiculos) == 0:
                print(t.nao_ha_nada[t.LANG])
                continue

            nova_fatura = cria_nova_fatura(lista_de_clientes, lista_de_veiculos)
            lista_de_faturas.append(nova_fatura)

        elif op == "lc":
            imprime_lista_de_clientes(lista_de_clientes)
            pause()

        elif op == "lv":
            imprime_lista_de_veiculos(lista_de_veiculos)
            pause()

        elif op == "lf":
            imprime_lista_de_faturas(lista_de_faturas)
            pause()


if __name__ == "__main__":
    menu()
