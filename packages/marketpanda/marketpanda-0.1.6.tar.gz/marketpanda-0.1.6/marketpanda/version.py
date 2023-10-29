# read toml file and extract version number


def get_version():
    with open("pyproject.toml", "r") as f:
        for line in f.readlines():
            if "version" in line:
                return line.split("=")[1].strip().replace('"', "")
    
    return "0.0.0"
