import argparse
import json
import yaml
import xmltodict
import dicttoxml
import sys

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

# Zapis XML
def save_xml(path, data):
    try:
        xml_data = dicttoxml.dicttoxml(data, custom_root="root", attr_type=False)

        with open(path, "wb") as file:
            file.write(xml_data)

        print("Zapisano dane do pliku XML")

    except PermissionError:
        print("Brak uprawnień do zapisu pliku XML")

# Metoda konwersji
def convert_file(input_path, output_path):
    print("Plik wejściowy:", input_path)
    print("Plik wyjściowy:", output_path)

    if input_path.endswith(".json"):
        data = read_json(input_path)

    elif input_path.endswith(".yml") or input_path.endswith(".yaml"):
        data = read_yaml(input_path)

    elif input_path.endswith(".xml"):
        data = read_xml(input_path)

    else:
        print("Nieobsługiwany format pliku wejściowego")
        return

    if data is not None:
        if output_path.endswith(".json"):
            save_json(output_path, data)

        elif output_path.endswith(".yml") or output_path.endswith(".yaml"):
            save_yaml(output_path, data)

        elif output_path.endswith(".xml"):
            save_xml(output_path, data)

        else:
            print("Nieobsługiwany format pliku wyjściowego")

# Metoda parsowania
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("output")
    return parser.parse_args()

def main():
    args = parse_arguments()
    convert_file(args.input, args.output)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        from ui import run_ui
        run_ui(convert_file)
    else:
        main()