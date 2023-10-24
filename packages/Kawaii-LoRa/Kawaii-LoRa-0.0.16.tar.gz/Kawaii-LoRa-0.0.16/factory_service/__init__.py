import os


def main(args: list[str] = []):
    # Accetto solo 1 parametro
    if len(args) != 1:
        raise Exception(
            "Fornire il path dello script che si vuole trasformare in Service!"
        )

    script_path = args[0]
    print(script_path)
