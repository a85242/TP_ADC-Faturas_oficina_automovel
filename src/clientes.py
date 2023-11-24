from io_terminal import imprime_lista

nome_ficheiro_lista_de_clientes = "lista_de_clientes.pk"

# TODO: Copie para aqui o código de cada uma das funções nos
# ficheiros com o nome clientes-*.py e faça um commit de cada vez
# Quando este ficheiro estiver completo com todas as suas funções,
# deve ser o unico ficheiro clientes.py existente, deve apagar
# todos os outros ficheiros clientes-*.py, e inclusive estes comentários

# ...

def cria_novo_cliente():
    """Pedir os dados de um novo cliente

    :return: dicionario com o novo cliente, {"nome": <<nome>>, "nif": <<nif>>, ...}
    """
    # TODO: pedir os dados do cliente e não esquecer de os devolver
    # ...
    nome = input("Nome? ")
    morada = input("Morada? ")
    localidade = input("Localidade?")
    c_postal = input("Código Postal? ")
    nif = int(input("NIF? "))
    tel = int(input("Telefone / Telemóvel? "))
    fax = input("Fax? ")
    email = input("Email? ")
    doc_ident = input("Documento Identificação Nº? ")
    emissor = input("Emissor? ")
    validade = input("Validade (Ano)? ")
    cacp = input("Código de Acesso a Certidão Permanente (só empresas)? ")
    data = input("Data (YYYY-MM-DD)? ")
    assinatura = input("Assinatura? ")

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