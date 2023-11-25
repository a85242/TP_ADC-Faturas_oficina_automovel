"""
Textos impressos do programa em cada idioma (português, espanhol e inglês).
"""
import json


try:
    with open('lang.json','x') as langjson:
        LANG = "pt"
        langjson.write('{"LANG": "pt"}')

except FileExistsError:
    try:
        langfile = open('lang.json')
        data = json.load(langfile)
        LANG = data["LANG"]

    except:
        LANG = "pt"

    finally:
        langfile.close()

_idiomasDisponiveis = {
    "pt": "português",
    "es": "español",
    "en": "english", 
}

def mudar_lingua():
    """
    Muda a língua do programa para o utilizador e é gravada num json
    """
    global LANG

    for lingua in _idiomasDisponiveis:
        print(f'{lingua} - {_idiomasDisponiveis[lingua]}')
    
    escolha_novalingua = {
        "pt": " Escolha a nova língua: ",
        "es": " Escoja el nuevo idioma: ",
        "en": " Choose the new language: ",
    }
    while True:
        nova_lingua = input(escolha_novalingua[LANG]).lower()
        if nova_lingua in _idiomasDisponiveis:
            break
    
    LANG = nova_lingua

    lingua_mudada = {
        "pt": "\nLíngua mudada para português.\n",
        "es": "\nIdioma cambiado a español.\n",
        "en": "\nLanguage changed to english.\n",
    }
    print(lingua_mudada[LANG])

    lang_newsave = {"LANG": LANG}
    with open('lang.json', 'w') as langjson:
        json.dump(lang_newsave, langjson)


# clientes.py

nome = {
    "pt": "Nome",
    "es": "Nombre",
    "en": "Name",
}
morada = {
    "pt": "Morada",
    "es": "Domicilio",
    "en": "Address",
}
localidade = {
    "pt": "Localidade",
    "es": "Localidad",
    "en": "Locality",
}
c_postal = {
    "pt": "Código postal",
    "es": "Código postal",
    "en": "Postal code",
}
nif = {
    "pt": "NIF",
    "es": "NIF",
    "en": "NIF",
}
tel = {
    "pt": "Telefone ou telemóvel",
    "es": "Teléfono",
    "en": "Phone",
}
fax = {
    "pt": "Fax",
    "es": "Fax",
    "en": "Fax",
}
email = {
    "pt": "Email",
    "es": "Email",
    "en": "Email",
}
doc_ident = {
    "pt": "Nº do documento de identificação",
    "es": "Nº del documento de identificación",
    "en": "Identification document number",
}
emissor = {
    "pt": "Emissor do documento de identificação",
    "es": "Emisor del documento de identificación",
    "en": "Issuer of the identification document",
}
validade = {
    "pt": "Ano de validade do documento de identificação",
    "es": "Año de validez del documento de identificación",
    "en": "Year of validity of the identification document",
}
cacp = {
    "pt": "Código de Acesso a Certidão Permanente, no caso de o cliente ser uma empresa",
    "es": "Código de Acceso al Certificado Permanente, si el cliente es una empresa",
    "en": "Código de Acesso a Certidão Permanente, if the client is a company",
}
data = {
    "pt": "Data",
    "es": "Fecha",
    "en": "Date",
}
assinatura = {
    "pt": "Assinatura",
    "es": "Firma",
    "en": "Signature",
}

# faturas.py

qualid_cliente = {
    "pt": "Qual o id do cliente?",
    "es": "¿Cuál es la id del cliente?",
    "en": "What is the client id?",
}
qualid_veiculo = {
    "pt": "Qual o id do veículo?",
    "es": "¿Cuál es la id del vehículo?",
    "en": "What is the vehicle id?",
}
desc_fatura = {
    "pt": "Descrição da fatura: ",
    "es": "Descripción de la factura: ",
    "en": "Invoice description: ",
}

# io_ficheiros.py

guarda_ficheiros = {
    "pt": "Os dados nos ficheiros serão sobrepostos. Continuar (s/N)? ",
    "es": "Los datos de los archivos se sobrescribirán. Continuar (s/N)? ",
    "en": "The data in the files will be overwritten. 's' to continue (save) or 'N' to cancel: ",
}
grav_cancelada = {
    "pt": "Gravação cancelada.",
    "es": "Guardado cancelado.",
    "en": "Saving canceled.",
}

# io_terminal.py

textoa = {
    "pt": "id inexistente. Tente de novo. Valores admitidos 0 - {}",
    "es": "id inexistente. Intente de nuevo. Valores aceptados 0 - {}",
    "en": "non-existent id. Try again. Allowed values 0 - {}",
}

pausa = {
    "pt": "Pressione ENTER para continuar...",
    "es": "Presione ENTER para continuar...",
    "en": "Press ENTER to continue...",
}

lista_vazia = {
    "pt": "Lista vazia",
    "es": "Lista vacía",
    "en": "List empty",
}

# main.py

novo_cliente = {
    "pt": "novo cliente",
    "es": "nuevo cliente",
    "en": "new client",
}
novo_veiculo = {
    "pt": "novo veículo",
    "es": "nuevo vehículo",
    "en": "new vehicle",
}
nova_fatura = {
    "pt": "nova fatura",
    "es": "nueva factura",
    "en": "new invoice",
}
list_clientes = {
    "pt": "listagem de clientes",
    "es": "listado de clientes",
    "en": "list of clients",
}
list_veiculos = {
    "pt": "listagem de veículos",
    "es": "listado de vehículos",
    "en": "list of vehicles",
}
list_faturas = {
    "pt": "listagem das faturas",
    "es": "listado de facturas",
    "en": "list of invoices",
}
guarda_tudo = {
    "pt": "guarda tudo",
    "es": "guardar todo",
    "en": "save everything",
}
carrega_tudo = {
    "pt": "carrega tudo",
    "es": "cargar todo",
    "en": "load everything",
}
sair = {
    "pt": "sair",
    "es": "salir",
    "en": "quit",
}
mudarlg = {
    "pt": "mudar língua",
    "es": "cambiar idioma",
    "en": "change language",
}

opcao = {
    "pt": "opção: ",
    "es": "opción: ",
    "en": "option: ",
}
nao_ha_nada = {
    "pt": "Não há clientes ou veículos registados.",
    "es": "No hay clientes ni vehículos registrados.",
    "en": "There are no customers or vehicles registered.",
}

# veiculos.py

marca = {
    "pt": "Marca",
    "es": "Marca",
    "en": "Brand",
} 
matricula = {
    "pt": "Matrícula",
    "es": "Matrícula",
    "en": "Registration plate",
}
data = {
    "pt": "Data de aquisição",
    "es": "Fecha de adquisición",
    "en": "Date of acquisition",
}
modelo = {
    "pt": "Modelo",
    "es": "Modelo",
    "en": "Model",
}
homologacao = {
    "pt": "Nº de homologação",
    "es": "Nº de homologación",
    "en": "Number of homologation",
}
categoria = {
    "pt": "Categoria",
    "es": "Categoría",
    "en": "Category",
}
tipo = {
    "pt": "Tipo",
    "es": "Tipo",
    "en": "Type",
}
cor = {
    "pt": "Cor",
    "es": "Color",
    "en": "Color",
}
combustivel = {
    "pt": "Tipo de combustível",
    "es": "Tipo de combustible",
    "en": "Fuel type",
}
matricula_ant = {
    "pt": "Matrícula anterior",
    "es": "Matrícula anterior",
    "en": "Previous registration plate",
}
data_ant = {
    "pt": "Data de aquisição da matrícula anterior",
    "es": "Fecha de adquisición de la atrícula anterior",
    "en": "Date of acquisition of the previous registration plate",
}
pais = {
    "pt": "País de origem do veículo",
    "es": "País de origen del vehículo",
    "en": "Country of origin of the vehicle",
}
anot_esp = {
    "pt": "Anotações especiais",
    "es": "Observaciones especiales",
    "en": "Special notes",
}



# faltariam traduzir
reboque = {
    "pt": "Reboque",
    "es": "Reboque",
    "en": "Reboque",
}
n_quadro = {
    "pt": "Nº quadro",
    "es": "Nº quadro",
    "en": "Nº quadro",
}
n_motor = {
    "pt": "Nº de motor",
    "es": "Nº de motor",
    "en": "Nº de motor",
}
n_cilindros = {
    "pt": "Nº de cilindros",
    "es": "Nº de cilindros",
    "en": "Nº de cilindros",
}
cilindrada = {
    "pt": "Cilindrada",
    "es": "Cilindrada",
    "en": "Cilindrada",
}
pneus_frente = {
    "pt": "Pneumáticos frente",
    "es": "Pneumáticos frente",
    "en": "Pneumáticos frente",
}
retaguarda_pneus = {
    "pt": "Pneus da retaguarda",
    "es": "Pneus da retaguarda",
    "en": "Pneus da retaguarda",
}
peso_max_admis = {
    "pt": "Peso máximo admissíveis da frente",
    "es": "Peso máximo admissíveis da frente",
    "en": "Peso máximo admissíveis da frente",
}
retaguarda_pma = {
    "pt": "Peso máximo admissível da retaguarda",
    "es": "Peso máximo admissível da retaguarda",
    "en": "Peso máximo admissível da retaguarda",
}
rebocavel = {
    "pt": "Veículo Rebocável",
    "es": "Veículo Rebocável",
    "en": "Veículo Rebocável",
}
c_trav = {
    "pt": "Veículo com travão",
    "es": "Veículo com travão",
    "en": "Veículo com travão",
}
s_trav = {
    "pt": "Veículo sem travão",
    "es": "Veículo sem travão",
    "en": "Veículo sem travão",
}
poder_elevacao = {
    "pt": "Poder de Elevação",
    "es": "Poder de Elevação",
    "en": "Poder de Elevação",
}
tipo_caixa = {
    "pt": "Tipo da caixa",
    "es": "Tipo da caixa",
    "en": "Tipo da caixa",
}
comprim_max_caixa = {
    "pt": "Comprimento máximo da caixa",
    "es": "Comprimento máximo da caixa",
    "en": "Comprimento máximo da caixa",
}
larg_caixa = {
    "pt": "Largura da caixa",
    "es": "Largura da caixa",
    "en": "Largura da caixa",
}
distancia_eixos = {
    "pt": "Distância entre eixos",
    "es": "Distância entre eixos",
    "en": "Distância entre eixos",
}
peso_bruto = {
    "pt": "Peso bruto total",
    "es": "Peso bruto total",
    "en": "Peso bruto total",
}
tara = {
    "pt": "Tara",
    "es": "Tara",
    "en": "Tara",
}
portas = {
    "pt": "Nº total de Portas",
    "es": "Nº total de Portas",
    "en": "Nº total de Portas",
}
direita = {
    "pt": "Nº portas direitas",
    "es": "Nº portas direitas",
    "en": "Nº portas direitas",
}
esquerda = {
    "pt": "Nº portas esquerdas",
    "es": "Nº portas esquerdas",
    "en": "Nº portas esquerdas",
}
retaguarda_portas = {
    "pt": "Nº portas retaguarda",
    "es": "Nº portas retaguarda",
    "en": "Nº portas retaguarda",
}
lotacao = {
    "pt": "Lotação",
    "es": "Lotação",
    "en": "Lotação",
}
