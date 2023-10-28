# The first definition is for the structure and type hints.
# The second definition is for loading the vr_hercules values.
from vr_hercules.hello_world.paths import CONFIG_FILE_PATH
from vr_hercules.parser.config_parsing import parse_config


class Config:
    greeting: str
    greetee: str


Config: type = parse_config(  # type: ignore # noqa
    config_file_path=CONFIG_FILE_PATH,
)
