import argparse
import json

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