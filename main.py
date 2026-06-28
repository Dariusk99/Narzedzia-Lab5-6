import argparse

parser = argparse.ArgumentParser()

parser.add_argument("input")
parser.add_argument("output")

args = parser.parse_args()

print("Plik wejściowy:", args.input)
print("Plik wyjściowy:", args.output)