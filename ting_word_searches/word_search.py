def exists_word(word, instance):
    result = []

    # Itera sobre cada arquivo na fila
    for file in instance.items:
        lines_with_word = []

        for line_number, line in enumerate(file["linhas_do_arquivo"], start=1):
            # Verifica se a palavra (case insensitive) está na linha
            if word.lower() in line.lower():
                lines_with_word.append({"linha": line_number})

        # Se a palavra foi encontrada, adiciona as informações à lista
        if lines_with_word:
            result.append({
                'palavra': word,
                'arquivo': file['nome_do_arquivo'],
                'ocorrencias': lines_with_word
            })

    return result


def search_by_word(word, instance):
    result = []

    # Itera sobre cada arquivo na fila
    for file in instance.items:
        occ = []

        for line_number, line in enumerate(file["linhas_do_arquivo"], start=1):
            # Verifica se a palavra (case insensitive) está na linha
            if word.lower() in line.lower():
                occ.append({
                    'linha': line_number,
                    'conteudo': line
                })

        # Se a palavra foi encontrada, adiciona as informações à lista
        if occ:
            result.append({
                'palavra': word,
                'arquivo': file['nome_do_arquivo'],
                'ocorrencias': occ
            })

    return result
