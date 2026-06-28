import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog, QVBoxLayout

class ConverterUI(QWidget):
    def __init__(self, convert_function):
        super().__init__()

        self.convert_function = convert_function
        self.input_path = ""
        self.output_path = ""

        self.setWindowTitle("Konwerter")
        self.setGeometry(600, 300, 500, 250)

        layout = QVBoxLayout()

        self.input_label = QLabel("Nie wybrano pliku wejściowego")
        self.output_label = QLabel("Nie wybrano pliku wyjściowego")
        self.status_label = QLabel("Status: gotowy")

        input_button = QPushButton("Wybierz plik wejściowy")
        output_button = QPushButton("Wybierz plik wyjściowy")
        convert_button = QPushButton("Konwertuj")

        input_button.clicked.connect(self.choose_input_file)
        output_button.clicked.connect(self.choose_output_file)
        convert_button.clicked.connect(self.convert_file)

        layout.addWidget(self.input_label)
        layout.addWidget(input_button)
        layout.addWidget(self.output_label)
        layout.addWidget(output_button)
        layout.addWidget(convert_button)
        layout.addWidget(self.status_label)

        self.setLayout(layout)

    # Dialog input file
    def choose_input_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Wybierz plik wejściowy", "", "Pliki (*.json *.yml *.yaml *.xml)")

        if file_path:
            self.input_path = file_path
            self.input_label.setText("Wejście: " + file_path)

    # Dialog output file
    def choose_output_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Wybierz plik wyjściowy", "", "JSON (*.json);;YAML (*.yml *.yaml);;XML (*.xml)")

        if file_path:
            self.output_path = file_path
            self.output_label.setText("Wyjście: " + file_path)

    # Konwertuj plik
    def convert_file(self):
        if not self.input_path:
            self.status_label.setText("Wybierz plik wejściowy!")
            return

        if not self.output_path:
            self.status_label.setText("Wybierz plik wyjściowy!")
            return

        try:
            self.convert_function(self.input_path, self.output_path)
            self.status_label.setText("Konwersja powiodła się")

        except Exception as error:
            self.status_label.setText(f"Error: {error}")

def run_ui(convert_function):
    app = QApplication(sys.argv)
    window = ConverterUI(convert_function)
    window.show()
    sys.exit(app.exec_())