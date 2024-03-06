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

1. Make sure you have this APIs installed:

- pip install pandas (in PowerShell)

 - pip install opencv-python pyzbar

- pip install reportLab

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
