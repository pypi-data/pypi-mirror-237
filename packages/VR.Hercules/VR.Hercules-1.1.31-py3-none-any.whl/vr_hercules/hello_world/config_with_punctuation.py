from pathlib import Path

from vr_hercules.hello_world.config import Config
from vr_hercules.hello_world.parse_punctuation import parse_punctuation
from vr_hercules.parser.config_parsing import parse_config
from vr_hercules.paths import CONFIG_PATH


class ConfigPunctuation(Config):
    punctuation: str


# Parse built-in fields
config_file_path: Path = \
    CONFIG_PATH / 'config_with_punctuation_exclamation_mark.yaml'
ConfigPunctuation: type = parse_config(  # type: ignore # noqa
    config_file_path=config_file_path,
)

# Parse custom fields
parse_punctuation(ConfigPunctuation)
