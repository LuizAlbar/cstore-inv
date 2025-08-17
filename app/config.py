import os
from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix = "cstore",
    preload = os.path.join(HERE, "default.toml"),
    settings_files = [
        os.path.join(HERE, "../.secrets.toml"),
        os.path.join(HERE, "../settins.toml")
    ],
    environments = ["development", "production", "testing"],
    env_switcher = "cstore_env",
    load_dotenv = False

)