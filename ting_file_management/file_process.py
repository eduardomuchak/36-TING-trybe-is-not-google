import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, instance: Queue):
    if path_file in instance.values():
        return

    data = txt_importer(path_file)

    data_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data
    }

    instance.enqueue(data_dict)
    print(data_dict)


def remove(instance: Queue):
    if not instance.__len__():
        print("Não há elementos")
        return

    data = instance.dequeue()
    print(f"Arquivo {data['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance: Queue, position):
    try:
        print(instance.search(position))
    except IndexError:
        print("Posição inválida", file=sys.stderr)
