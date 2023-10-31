# Medicine Stock Management :hospital:

This is a simple medicine stock management application developed using Python, SQLite3, and Tkinter. This application is designed to help users manage their medicine inventory, including adding, updating, and deleting medicines, as well as tracking stock levels.

## Features :dart: 

- **Add New Medicine**: Easily add new medicines to your inventory with information such as name, quantity, expiration date, and more.

- **Update Medicine Details**: Update the information of existing medicines, including quantity, expiration date, and other relevant details.

- **Delete Medicine**: Remove medicines from your stock when they are no longer available or needed.

- **View Medicine List**: Display the list of all medicines in your inventory, including essential details.


## Prerequisites :thought_balloon:

Before running the application, make sure you have the following prerequisites installed:

- Python 3.x: You can download Python from [python.org](https://www.python.org/downloads/).

## Setup :desktop_computer:

1. Clone the repository or download the project as a ZIP file and extract it to your local machine.

2. Open your terminal or command prompt and navigate to the project directory.

3. Create a virtual environment (recommended) to manage dependencies. Run the following commands:

   ```bash
   # Create a virtual environment
   python -m venv venv

   # Activate the virtual environment
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

   # Install required packages
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python main.py
   ```

## Usage :books:

1. **Add a New Medicine**:
   - Click the "Add Medicine" button.
   - Fill in the details of the medicine.
   - Click "Save" to add the medicine to your inventory.

2. **Update Medicine Details**:
   - Select a medicine from the list.
   - Click the "Edit" button.
   - Modify the details.
   - Click "Save" to update the medicine.

3. **Delete Medicine**:
   - Select a medicine from the list.
   - Click the "Delete" button to remove it from your inventory.

5. **View Medicine List**:
   - The main screen displays a list of all medicines in your inventory with relevant details.


## Database

The application uses SQLite3 as its database. The database file (`products.db`) is automatically created in the project directory when you run the application. You can back up this file to safeguard your data.

## Contributing :star_struck:

Contributions to the project are welcome. If you find issues or have ideas for improvements, please submit an issue or create a pull request.


## Output

This is how the project will be once it is finished
![OUTPUT](https://github.com/HariAr2/Medicine-stock-Management/blob/main/Project/ss.png)



## Acknowledgments :medal_sports:

This project is developed by Hari Aravindh and is inspired by the need for an efficient and user-friendly solution for managing medicine stock. It is a simple yet powerful tool for anyone who needs to keep track of their medicine inventory.
