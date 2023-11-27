from io_terminal import imprime_lista
import texto as t

nome_ficheiro_lista_de_clientes = "lista_de_clientes.pk"

def cria_novo_cliente():
    """Pedir os dados de um novo cliente

    :return: dicionario com o novo cliente, {"nome": <<nome>>, "nif": <<nif>>, ...}
    """

    nome = input( f"{t.nome[t.LANG]}: ")
    morada = input( f"{t.morada[t.LANG]}: ")
    localidade = input( f"{t.localidade[t.LANG]}: ")
    c_postal = input( f"{t.c_postal[t.LANG]}: ")
    nif = int(input( f"{t.nif[t.LANG]}: "))
    tel = int(input( f"{t.tel[t.LANG]}: "))
    fax = input( f"{t.fax[t.LANG]}: ")
    email = input( f"{t.email[t.LANG]}: ")
    doc_ident = input( f"{t.doc_ident[t.LANG]}: ")
    emissor = input( f"{t.emissor[t.LANG]}: ")
    validade = input( f"{t.validade[t.LANG]}: ")
    cacp = input( f"{t.cacp[t.LANG]}: ")
    data = input( f"{t.data[t.LANG]} (YYYY-MM-DD): ")
    assinatura = input( f"{t.assinatura[t.LANG]}: ")

    cliente = {"Nome": nome,
               "Morada": morada,
               "Localidade": localidade,
               "Código Postal": c_postal,
               "NIF": nif,
               "Telefone ou Telemóvel": tel,
               "Fax": fax,
               "Email": email,
               "Nº do documento de identificação": doc_ident,
               "Emissor do documento de identificação": emissor,
               "Ano de validade do documento de identificação": validade,
               "Código de Acesso a Certidão Permanente, no caso de o cliente ser uma empresa": cacp,
               "Data em formato YYYY-MM-DD": data,
               "Assinatura": assinatura
               }
    pass
    return cliente

def imprime_lista_de_clientes(lista_de_clientes):
    """Imprime a lista de clientes
    
    :param lista_de_veiculos: Lista de clientes com o seu dicionario.
    :type lista_de_veiculos: list
    """
    imprime_lista(cabecalho=t.list_clientes[t.LANG], lista=lista_de_clientes)