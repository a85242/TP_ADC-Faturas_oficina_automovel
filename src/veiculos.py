from io_terminal import imprime_lista
import texto as t

nome_ficheiro_lista_de_veiculos = "lista_de_veiculos.pk"

def cria_novo_veiculo():
    """Pede ao utilizador para introduzir um novo veiculo

    :return: dicionario com um veiculo na forma
        {"marca": <<marca>>, "matricula": <<matricula>>, ...}
    """

    marca = input(f"{t.marca[t.LANG]}: ")
    matricula = input(f"{t.matricula[t.LANG]}: ").upper()
    reboque = bool(input(f"{t.reboque[t.LANG]}: "))
    data = input(f"{t.data[t.LANG]}: (YYYY-MM-DD)")
    modelo = input(f"{t.modelo[t.LANG]}: ")
    homologacao = int(input(f"{t.homologacao[t.LANG]}: "))
    categoria = input(f"{t.categoria[t.LANG]}: ")
    tipo = input(f"{t.tipo[t.LANG]}: ")
    cor = input(f"{t.cor[t.LANG]}: ")
    n_quadro = int(input(f"{t.n_quadro[t.LANG]}: "))
    n_motor = int(input(f"{t.n_motor[t.LANG]}: "))
    combustivel = input(f"{t.combustivel[t.LANG]}: ")
    n_cilindros = int(input(f"{t.n_cilindros[t.LANG]}: "))
    cilindrada = input(f"{t.cilindrada[t.LANG]}: ")
    pneus_frente = input(f"{t.pneus_frente[t.LANG]}: ")
    retaguarda_pneus = input(f"{t.retaguarda_pneus[t.LANG]}: ")
    peso_max_admis = input(f"{t.peso_max_admis[t.LANG]}: ")
    retaguarda_pma = input(f"{t.retaguarda_pma[t.LANG]}: ")
    rebocavel = bool(input(f"{t.rebocavel[t.LANG]}: "))
    c_trav = bool(input(f"{t.c_trav[t.LANG]}: "))
    s_trav = bool(input(f"{t.s_trav[t.LANG]}: "))
    poder_elevacao = input(f"{t.poder_elevacao[t.LANG]}: ")
    tipo_caixa = input(f"{t.tipo_caixa[t.LANG]}: ")
    comprim_max_caixa = input(f"{t.comprim_max_caixa[t.LANG]}: ")
    larg_caixa = input(f"{t.larg_caixa[t.LANG]}: ")
    distancia_eixos = input(f"{t.distancia_eixos[t.LANG]}: ")
    peso_bruto = input(f"{t.peso_bruto[t.LANG]}: ")
    tara = input(f"{t.tara[t.LANG]}: ")
    portas = input(f"{t.portas[t.LANG]}: ")
    direita = input(f"{t.direita[t.LANG]}: ")
    esquerda = input(f"{t.esquerda[t.LANG]}: ")
    retaguarda_portas = input(f"{t.retaguarda_portas[t.LANG]}: ")
    lotacao = int(input(f"{t.lotacao[t.LANG]}: "))
    matricula_ant = input(f"{t.matricula_ant[t.LANG]}: ").upper()
    data_ant = input(f"{t.data_ant[t.LANG]}: (YYYY-MM-DD)")
    pais = input(f"{t.pais[t.LANG]}: ")
    anot_esp = input(f"{t.anot_esp[t.LANG]}: ")

    veiculo = {"marca": marca,
               "matricula": matricula,
               "reboque": reboque,
               "data de aquisição do veículo atual": data,
               "modelo": modelo,
               "Nº de homologação": homologacao,
               "Categoria": categoria,
               "Tipo": tipo,
               "Cor": cor,
               "Nº Quadro": n_quadro,
               "Nº de Motor": n_motor,
               "Tipo de combustível": combustivel,
               "Nº de cilindros": n_cilindros,
               "Cilindrada": cilindrada,
               "Pneumáticos frente": pneus_frente,
               "Pneus da retaguarda": retaguarda_pneus,
               "Peso máximo admissíveis da frente": peso_max_admis,
               "Peso máximo admissível da retaguarda": retaguarda_pma,
               "Veículo Rebocável?": rebocavel,
               "Veículo com travão?": c_trav,
               "Veículo sem travão?": s_trav,
               "Poder de Elevação": poder_elevacao,
               "Tipo da caixa": tipo_caixa,
               "Comprimento máximo da caixa": comprim_max_caixa,
               "Largura da caixa": larg_caixa,
               "Distância entre eixos": distancia_eixos,
               "Peso bruto total": peso_bruto,
               "Tara": tara,
               "Nº total de Portas": portas,
               "Nº portas direitas": direita,
               "Nº portas esquerdas": esquerda,
               "Nº portas retaguarda": retaguarda_portas,
               "Lotação": lotacao,
               "Matrícula anterior": matricula_ant,
               "Data da matrícula anterior": data_ant,
               "País de Origem do veículo": pais,
               "Anotações especiais": anot_esp
               }

    return veiculo

def imprime_lista_de_veiculos(lista_de_veiculos):
    """Imprime a lista de veículos
    
    :param lista_de_veiculos: Lista de veículos com o seu dicionario.
    :type lista_de_veiculos: list
    """

    imprime_lista(cabecalho=t.list_veiculos[t.LANG], lista=lista_de_veiculos)

