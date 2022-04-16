import configparser
from typing import Dict


def read_config(config_file: str) -> Dict:
    config = configparser.ConfigParser()
    config.read(config_file)

    return {"output_file_prefix": config["DEFAULT"]["output_file_prefix"]}
