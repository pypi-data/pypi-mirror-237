import yaml
def load_yaml(path):
    with open(path, "r") as stream:
        try:
            content = yaml.load(stream, Loader=yaml.FullLoader)
            return content
        except yaml.YAMLError as exc:
            print(exc)