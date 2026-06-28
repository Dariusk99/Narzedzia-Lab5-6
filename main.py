import argparse
import json
import yaml
import xmltodict

parser = argparse.ArgumentParser()

parser.add_argument("input")
parser.add_argument("output")

args = parser.parse_args()

print("Plik wejściowy:", args.input)
print("Plik wyjściowy:", args.output)

# Wczytaj JSON
def read_json(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)

        print("Wczytano plik JSON")
        return data

    except FileNotFoundError:
        print("Plik JSON nie istnieje")
        return None

    except json.JSONDecodeError:
        print("Niepoprawna składnia pliku JSON")
        return None

    except PermissionError:
        print("Brak uprawnień do pliku JSON")
        return None

# Zapis JSON
def save_json(path, data):
    try:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print("Zapisano dane do pliku JSON")
    except PermissionError:
        print("Brak uprawnień do zapisu pliku JSON")

# Wczytanie YAML
def read_yaml(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        print("Wczytano plik YAML")
        return data

    except FileNotFoundError:
        print("Plik YAML nie istnieje")
        return None

    except yaml.YAMLError:
        print("Niepoprawna składnia pliku YAML")
        return None

    except PermissionError:
        print("Brak uprawnień do pliku YAML")
        return None

# Zapis YAML
def save_yaml(path, data):
    try:
        with open(path, "w", encoding="utf-8") as file:
            yaml.safe_dump(data, file, allow_unicode=True, sort_keys=False)
        print("Zapisano dane do pliku YAML")

    except PermissionError:
        print("Brak uprawnień do zapisu pliku YAML")

# Wczytanie XML
def read_xml(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = xmltodict.parse(file.read())

        print("Wczytano plik XML")
        return data

    except FileNotFoundError:
        print("Plik XML nie istnieje")
        return None

    except xmltodict.expat.ExpatError:
        print("Niepoprawna składnia pliku XML")
        return None

    except PermissionError:
        print("Brak uprawnień do pliku XML")
        return None