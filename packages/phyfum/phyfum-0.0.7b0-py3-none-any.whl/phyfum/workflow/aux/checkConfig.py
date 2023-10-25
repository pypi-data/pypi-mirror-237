import yaml


def readDefaults(yaml_path: str) -> dict:
    with open(yaml_path, 'r') as f:
        config = yaml.safe_load(f)
    default_values = {key: value["default"] for key, value in config.get("properties", {}).items() if "default" in value}
    return default_values


def makeConfig(config: dict, defaults: dict) -> dict:
    """
    Remove Nones from config and add missing variables from the defaults
    """
    config = {key: value for key, value in config.items() if value}

    # Merge 'config' with 'defaults' to add missing variables
    return {**defaults, **config}
