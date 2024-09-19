# projects_add_gui.py

import sys
import pandas as pd
import os
from PyQt5 import QtWidgets
from projects_add_ui import Ui_MainWindow

class ProjectsApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(ProjectsApp, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Path to the projects Excel file
        self.projects_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'projects.xlsx')

        # Connect the submit button to the function
        self.submitButton.clicked.connect(self.add_project)

    def add_project(self):
        # Retrieve data from the input fields
        project_name = self.projectNameLineEdit.text()
        components = self.componentsLineEdit.text()
        connection = self.connectionTextEdit.toPlainText()

        if not project_name or not components or not connection:
            QtWidgets.QMessageBox.warning(self, "Input Error", "All fields must be filled out!")
            return

        # Load existing data or create a new DataFrame if the file does not exist
        if os.path.exists(self.projects_file_path):
            projects_df = pd.read_excel(self.projects_file_path, engine='openpyxl')
        else:
            projects_df = pd.DataFrame(columns=['Project Name', 'Components', 'Connection'])

        # Add the new project to the DataFrame
        new_entry = pd.DataFrame([[project_name, components, connection]], columns=['Project Name', 'Components', 'Connection'])
        updated_df = pd.concat([projects_df, new_entry], ignore_index=True)

        # Save the updated DataFrame to the Excel file
        updated_df.to_excel(self.projects_file_path, index=False, engine='openpyxl')
        QtWidgets.QMessageBox.information(self, "Success", "Project added successfully!")

        # Clear input fields
        self.projectNameLineEdit.clear()
        self.componentsLineEdit.clear()
        self.connectionTextEdit.clear()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ProjectsApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
