from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    list = []

    for index in range(len(instance)):
        file = instance.search(index)
        data = [
            {"linha": index + 1}
            for index, line in enumerate(file["linhas_do_arquivo"])
            if word.lower() in line.lower()
        ]

        dict = {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": data
                }

        if dict["ocorrencias"] == []:
            return []

        if dict:
            list.append(dict)

    return list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
