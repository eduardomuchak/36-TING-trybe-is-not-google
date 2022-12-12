from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, instance: Queue):
    if instance.values(path_file):
        return
    data = txt_importer(path_file)

    data_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data
    }

    instance.enqueue(data_dict)
    print(path_file)


def remove(instance):
    data = instance.dequeue()
    if data:
        print(f"Arquivo {data['nome_do_arquivo']} removido com sucesso")
    else:
        print("Não há elementos")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
