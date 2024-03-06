from Class import Stock
from Class import Logger
from Fachada import facade

select = facade()

while True:

    Stock.stock_lvl()

    print("""
    Welcome!

    Please, select your option:

    1 - Add
    2 - Update Item
    3 - Supplier Management
    4 - Inventory Valuation
    5 - Purchase order
    6 - Barcode reader
    7 - Sales and History
    8 - Inventory Reports
    0 - exit
    """)

    action = input('')

    if action == '1':
        
        select.b1()

    elif action =='2':

        select.b2()

    elif action == '3':

        select.b3()

    elif action == '4':

        select.b4()

    elif action == '5':

        select.b5()
    
    elif action == '6':

        select.b6()
    
    elif action == '7':

        select.b7()
    
    elif action == '8':

        Logger.imprimir_csv()
        
    elif action == '0':
        break




    