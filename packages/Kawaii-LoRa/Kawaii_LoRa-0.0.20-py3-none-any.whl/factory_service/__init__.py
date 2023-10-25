import os
import sys
import tempfile


def main() -> int:
    try:
        # Accetto solo 2 parametri:
        #   0. Nome del file che python eseguire
        #   1. Il mio parametro, ovvero il file che dovrà essere convertito in Service
        if len(sys.argv) != 2:
            raise Exception(
                "Fornire il path dello script che si vuole trasformare in Service!"
            )

        relative_script_path = sys.argv[1]
        full_name_script_path = os.path.basename(relative_script_path)
        # name_script_path = ful
        abs_script_path = os.path.abspath(relative_script_path)

        print(relative_script_path)
        print(full_name_script_path)
        print(abs_script_path)

        # Creo un file momentaneo
        with tempfile.TemporaryFile() as temp_file:
            pass
    except Exception as ex:
        print(ex)
        return -1

    return 0
