import pandas as pd
from Class import AtualizadorItemLogger, Logger


class Opt2:
     
    def opt2(self):

        nome = 'Products.csv'

        p_df = pd.read_csv(nome)


        print("""
        Welcome to update menu!
            
        What do you want to do?
            
            1 - Edit
            2 - Remove
            0 - Back
    """)

        S = input('')

        if S == '1':
            print("Choose a column to update(Enter the class you want to edit):")
            print(p_df.columns)

            column = input('')
            print("\nAvailable items:")
            print(p_df.to_string(index=True))

            try:
                index = int(input('\nEnter the index of the item to update: '))
                if 0 <= index < len(p_df):
                    new_value = input(f'Enter the new value for {column}: ')
                    atualizador = AtualizadorItemLogger()
                    p_df = atualizador.update_item(p_df, index, column, new_value)
                    p_df.to_csv('Products.csv', index=False)
                    print("Item updated successfully!")
                else:
                    print("Invalid index. Please enter a valid index.")
            except ValueError:
                    print("Invalid input. Please enter a valid index.")
        
        elif S == '2':

            print("Choose a column to delete(Enter the class you want to edit):")
            print(p_df.columns)

            column = input('')
            print("\nAvailable Items:")
            print(p_df.to_string(index=True))

            try:
                index = int(input('\nEnter the index of the item to delete: '))
                if 0 <= index < len(p_df):

                    item_info = p_df.loc[index].to_dict()
                    Logger.registrar_log('remove_item', f"Index: {index}, Item Info: {item_info}")
                    p_df = p_df.drop(index, axis = 0)
                    p_df.to_csv('Products.csv', index=False)
                    print('\n')
                    print(p_df)
                    print('\n')
                    print("Item updated successfully!")
                else:
                    print("Invalid index. Please enter a valid index.")
            except ValueError:
                    print("Invalid input. Please enter a valid index.")
