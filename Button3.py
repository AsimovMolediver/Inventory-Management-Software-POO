import pandas as pd
from Class import AtualizadorItemLogger, Supplier, Logger

class Opt3:
     
    def opt3(self):
        
        print("""
            
        Welcome to Supplier Management!
            
        What do you want to do?
            
            1 - Add
            2 - Edit
            3 - Remove
            0 - Back
            
        """)
        nome = 'Suppliers.csv'

        s_df = pd.read_csv(nome)

        S = input('Enter the option: ')

        if S == '1':

            #nome = 'Suppliers.csv'

            #s_df = pd.read_csv(nome)

            print('\n')
            print(s_df)
            print('\n')

            supplier = input('Supplier: ')
            product = input('Product: ')
            contact =input('Contact: ')
            email = input('E-mail: ')
            CEP = input('CEP: ')
            CNPJ = input('CNPJ: ')

            s_df = Supplier.add_s(s_df, supplier, product, contact, email, CEP, CNPJ)

            s_df.to_csv("Suppliers.csv", index = False)

            print('\n')
            print('New Supplier added:')
            print('\n')
            print(s_df)

        elif S == '2':
            
            #nome = 'Suppliers.csv'

            #s_df = pd.read_csv(nome)

            print("Choose a column to update(Enter the class you want to edit):")
            print(s_df.columns)

            column = input('')
            print("\nAvailable items:")
            print(s_df.to_string(index=True))

            try:
                index = int(input('\nEnter the index of the item to update: '))
                if 0 <= index < len(s_df):
                    new_value = input(f'Enter the new value for {column}: ')
                    atualizador = AtualizadorItemLogger()
                    s_df = AtualizadorItemLogger.update_item(s_df, index, column, new_value)
                    s_df.to_csv('Suppliers.csv', index=False)
                    Logger.registrar_log('opt3_update', f"Index: {index}, Column: {column}, New Value: {new_value}")
                    print("Information updated successfully!")
                else:
                    print("Invalid index. Please enter a valid index.")
            except ValueError:
                    print("Invalid input. Please enter a valid index.")

        elif S == '3':    
            
            print("Choose a column to delete(Enter the class you want to edit):")
            print(s_df.columns)

            column = input('')
            print("\nAvailable Suppliers:")
            print(s_df.to_string(index=True))

            try:
                index = int(input('\nEnter the index of the supplier to delete: '))
                if 0 <= index < len(s_df):
                    Logger.registrar_log('opt3_remove', f"Index: {index}, Supplier: {s_df.at[index, 'Supplier']}")
                    s_df = s_df.drop(index, axis = 0)
                    s_df.to_csv('Suppliers.csv', index=False)
                    print('\n')
                    print(s_df)
                    print('\n')
                    print("Item updated successfully!")
                else:
                    print("Invalid index. Please enter a valid index.")
            except ValueError:
                    print("Invalid input. Please enter a valid index.")

        elif S == '0':
            
            print('OK!')