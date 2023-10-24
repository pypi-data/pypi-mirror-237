import os
import sys


def main() -> int:
    try:
        # Accetto solo 1 parametro
        if len(sys.argv) != 2:
            raise Exception(
                "Fornire il path dello script che si vuole trasformare in Service!"
            )

        relative_script_path = sys.argv[1]
        abs_script_path = os.path.abspath(relative_script_path)

        print(abs_script_path)
    except Exception as ex:
        print(ex)
        return 1

    return 0
