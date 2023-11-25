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

# TODO