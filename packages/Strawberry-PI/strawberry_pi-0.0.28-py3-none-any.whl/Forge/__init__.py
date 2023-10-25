import os
import sys
import time


# -------------------------------------------------------------------------------------------- #
# Contenuto che dovrà essere scritto nel service file
CONTENT = """[Unit]
Description={name} service
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 {path}
Restart=always
RuntimeMaxSec=infinity

[Install]
WantedBy=multi-user.target"""


# -------------------------------------------------------------------------------------------- #
def main() -> int:
    try:
        # Accetto solo 2 parametri:
        #   0. Nome del file che python eseguire
        #   1. Il mio parametro, ovvero il file che dovrà essere convertito in Service
        if len(sys.argv) != 2:
            raise Exception(
                "Fornire il path dello script che si vuole trasformare in Service!"
            )

        # Path Relativo -> MyProject/MyScript.py
        relative_script_path = sys.argv[1]
        # Path Absolute -> /home/<User>/Desktop/MyProject/MyScript.py
        abs_script_path = os.path.abspath(relative_script_path)
        # Path Dir -> /home/<User>/Desktop/MyProject
        dir_path = os.path.dirname(abs_script_path)
        # Full Name -> MyScript.py
        full_name_script_path = os.path.basename(relative_script_path)
        # Name -> MyScript
        name_script_path = ".".join(full_name_script_path.split(".")[:-1])

        # Check if Script is a File
        if not os.path.isfile(abs_script_path):
            raise Exception("Il path fornito non è uno script python!")

        # Creo un file momentaneo
        temp_file_path = os.path.join(dir_path, f"{name_script_path}.service")
        try:
            with open(temp_file_path, "w") as tmp_file:
                tmp_file.write(
                    CONTENT.format(name=name_script_path, path=abs_script_path)
                )
        finally:
            # Elimino il temp_file
            time.sleep(10)
            if os.path.exists(temp_file_path):
                os.remove(temp_file_path)

    except Exception as ex:
        print(ex)  # TODO: LOGGER console.error(), console.log(), console.debug()
        return -1

    return 0
