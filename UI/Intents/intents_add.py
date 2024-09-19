import sys
import pandas as pd
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from intents_add_ui import Ui_MainWindow  # Import the generated UI class

# Determine the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the intents Excel file
intents_file_path = os.path.join(script_dir, 'intents.xlsx')

# Load existing data or create a new DataFrame if the file does not exist
if os.path.exists(intents_file_path):
    intents_df = pd.read_excel(intents_file_path, engine='openpyxl')
else:
    # Create a new DataFrame with appropriate columns if file doesn't exist
    intents_df = pd.DataFrame(columns=['Intent', 'Pattern', 'Response'])

class IntentAddWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(IntentAddWindow, self).__init__()
        self.setupUi(self)
        self.submitButton.clicked.connect(self.add_intent)
        
    def add_intent(self):
        intent_name = self.intentNameLineEdit.text()
        pattern = self.patternLineEdit.text()
        response = self.responseLineEdit.text()

        if not intent_name or not pattern or not response:
            QMessageBox.warning(self, "Input Error", "All fields must be filled out!")
            return

        global intents_df
        new_entry = pd.DataFrame([[intent_name, pattern, response]], columns=['Intent', 'Pattern', 'Response'])
        intents_df = pd.concat([intents_df, new_entry], ignore_index=True)

        # Save the updated DataFrame to the Excel file
        try:
            intents_df.to_excel(intents_file_path, index=False, engine='openpyxl')
            QMessageBox.information(self, "Success", "New intent added successfully!")
        except PermissionError:
            QMessageBox.critical(self, "Error", f"Permission denied. Ensure the file '{intents_file_path}' is not open elsewhere.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = IntentAddWindow()
    mainWin.show()
    sys.exit(app.exec_())
