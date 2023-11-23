def cria_novo_veiculo():
    """Pede ao utilizador para introduzir um novo veiculo

    :return: dicionario com um veiculo na forma
        {"marca": <<marca>>, "matricula": <<matricula>>, ...}
    """

    marca = input("marca? ")
    matricula = input("matricula? ").upper()
    reboque = bool(input("reboque? "))
    data = input("data? (YYYY-MM-DD)")
    modelo = input("Modelo? ")
    homologacao = int(input("Homologação nº? "))
    categoria = input("Categoria? ")
    tipo = input("Tipo? ")
    Cor = input("Cor? ")
    n_quadro = int(input("Nº quadro? "))
    n_motor = int(input("Nº de motor? "))
    combustivel = input("Combustível? ")
    n_cilindros = int(input("Nº de cilindros? "))
    cilindrada = input("Cilindrada? ")
    pneus_frente = input("Pneumáticos: Frente? ")
    retaguarda_pneus = input("Retaguarda pneus? ")
    peso_max_admis = input("Peso máximo admissíveis: Frente? ")
    retaguarda_pma = input("Retaguarda peso máximo admissível? ")
    rebocavel = bool(input("Rebocável? "))
    c_trav = bool(input("Com travão? "))
    s_trav = bool(input("Sem travão? "))
    poder_elevacao = input("Poder de elevação? ")
    tipo_caixa = input("Tipo da caixa? ")
    comprim_max_caixa = input("Comprimento máximo da caixa? ")
    larg_caixa = input("Largura da caixa? ")
    distancia_eixos = input("Distância entre eixos? ")
    peso_bruto = input("Peso bruto total? ")
    tara = input("Tara? ")
    portas = input("nº total de portas? ")
    direita = input("Portas Direitas? ")
    esquerda = input("Portas Esquerdas? ")
    retaguarda_portas = input("Porta Retaguarda? ")
    lotacao = int(input("Lotação? "))
    matricula_ant = input("Matrícula anterior? ").upper()
    data_ant = input("Data anterior? (YYYY-MM-DD)")
    pais = input("País de Origem? ")
    anot_esp = input("Anotações especiais? ")

    veiculo = {"marca": marca,
               "matricula": matricula,
               "reboque": reboque,
               "data de aquisição do veículo atual": data,
               "modelo": modelo,
               "Nº de homologação": homologacao,
               "Categoria": categoria,
               "Tipo": tipo,
               "Cor": Cor,
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
