import os


def main(args: list[str] = []):
    # Accetto solo 1 parametro
    if len(args) != 1:
        raise Exception(
            "Fornire il path dello script che si vuole trasformare in Service!"
        )

    relative_script_path = args[0]
    abs_script_path = os.path.abspath(relative_script_path)

    print(abs_script_path)
