import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith('.txt'):
            raise ValueError('Formato inválido')
        with open(path_file, 'r', encoding='utf-8') as file:
            return file.read().split('\n')

    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return None
    except ValueError as error:
        print(f"{error}", file=sys.stderr)
        return None
