import sys
import sqlite3
from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5.QtWidgets import QApplication, QTableView

# Create a custom model class that inherits from QAbstractTableModel
class SqliteModel(QAbstractTableModel):
    def __init__(self, db_name, table_name, parent=None):
        super().__init__(parent)
        # Connect to the database
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        # Set the table name
        self.table_name = table_name
        # Fetch the column names and the data from the table
        self.column_names = self.get_column_names()
        self.data = self.get_data()

    def get_column_names(self):
        # Execute a query to get the column names from the table
        query = f"PRAGMA table_info({self.table_name})"
        self.cursor.execute(query)
        # Return a list of column names
        return [row[1] for row in self.cursor.fetchall()]

    def get_data(self):
        # Execute a query to get all the data from the table
        query = f"SELECT * FROM {self.table_name}"
        self.cursor.execute(query)
        # Return a list of tuples representing the rows
        return self.cursor.fetchall()

    def rowCount(self, parent):
        # Return the number of rows in the data
        return len(self.data)

    def columnCount(self, parent):
        # Return the number of columns in the data
        return len(self.column_names)

    def data(self, index, role):
        # Return the data for the given index and role
        if role == Qt.DisplayRole:
            # Return the value of the cell as a string
            return str(self.data[index.row()][index.column()])
        else:
            # Return None for other roles
            return None

    def headerData(self, section, orientation, role):
        # Return the header data for the given section, orientation, and role
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                # Return the column name for the horizontal header
                return self.column_names[section]
            elif orientation == Qt.Vertical:
                # Return the row number for the vertical header
                return str(section + 1)
        else:
            # Return None for other roles
            return None

# Create a table view and set the model
app = QApplication(sys.argv)
view = QTableView()
model = SqliteModel("data/tasks.db", "tasks")
view.setModel(model)

# Show the view
view.show()

# Create the application

# Run the main loop
sys.exit(app.exec_())
