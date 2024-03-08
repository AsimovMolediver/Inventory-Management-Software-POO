## Inventory Management System

This is a simple product management system developed in Python using the pandas library. It allows for the addition, updating, and viewing of products in a DataFrame.

## Functions Implemented
Product Catalog Management: Adding, updating, and categorizing inventory items;

Stock Level Tracking: Real-time tracking of inventory levels;

Reorder Alerts: Automated alerts for low stock and reorder points;

Supplier Management: Managing information about suppliers;

Purchase Order Creation: Generating and managing purchase orders;

Barcode Scanning: Integration of barcode scanning for inventory management;

Inventory Valuation: Calculating the total value of the inventory on hand;

Sales and Purchase History: Tracking and analyzing sales and purchase data;

Inventory Reports: Generating detailed reports on inventory status and movements.

## Requirements

- Python 3.x
- pandas
- pyzbar
- reportLab

## Installation

To create and manage virtual environments in Python, we'll use the venv module. Here's a simplified guide in English that you can include in your README:

1. Creating a Virtual Environment:

Choose a directory where you want to create the virtual environment.
Run the venv module as a script with the directory path:

python -m venv venv

This command creates a directory named venv if it doesn't exist already. It also creates subdirectories within it containing a copy of the Python interpreter, the standard library, and various support files.

Activating the Virtual Environment:

On Windows:

venv\Scripts\activate

On Unix or MacOS:

source venv/bin/activate

Activating the virtual environment sets up your shell to use the Python interpreter and other tools from within the virtual environment.

Deactivating the Virtual Environment:
To deactivate the virtual environment, simply type:

deactivate

2. Installing Required Packages:

To install the necessary packages for testing the program, use:

pip install -r requirements.txt

This command installs all the packages listed in the requirements.txt file.

If you prefer manual installation, you can install each package individually:

pip install pandas 
pip install opencv-python pyzbar
pip install reportLab


After installing the required packages, you can execute the code by running Main.py.

Feel free to adjust and customize this guide according to your specific needs.

## Usage

1. Run the 'main.py' script.

Choose the desired option from the menu:

1 - Add

2 - Update Item

3 - Supplier Management

4 - Inventory Valuation

5 - Purchase order

6 - Barcode reader

7 - Sales and History

0 - exit

Follow the on-screen instructions to input or update information.

## Particularities

The type of barcode used in this application was the QR code, due to its ease of being read by a low-quality camera. Some QR code examples are already in the file folder. An example of how to enter your data to generate a QR code: Tira,Lisa,Aviador,Branca,22,10,0.2

The PDF is generated each time requested, it already contains the date and time, so it already counts as history, the sales history is implemented in the code.

The stock level scan and the reorder alert were implemented together, so every time a movement is made the system will re-search all available stock, display it above the main menu and alert you to the need for a new reorder.




## Contributing
Feel free to contribute to the development of this project. Open an issue to report problems or suggest improvements through pull requests.
