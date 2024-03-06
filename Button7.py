import pandas as pd 
from datetime import datetime
from Class import AtualizadorItem, Logger

def history_df_exists():
        try:
            pd.read_csv('History.csv')
            return True
        except FileNotFoundError:
            return False

class Opt7:

    def history_df_exists():
        try:
            pd.read_csv('History.csv')
            return True
        except FileNotFoundError:
            return False

    def opt7(self):
        nome = 'Products.csv'
        p_df = pd.read_csv(nome)

        print("""
    ******************
    Sales and History
    ******************
            
    1 - Sale
    2 - History
    0 - Exit
        """)
    
        ent = input('')

        if ent == '1':
            print('\nNew Sale!\n')
            print('Please, select the item that was sold and its quantity so we can update the inventory.\n')
            print(p_df.columns)

            column = 'Quantidade'
            print("\nAvailable items:")
            print(p_df.to_string(index=True))

            try:
                index = int(input('\nEnter the index of the item you sell to update: '))

                if 0 <= index < len(p_df):
                    quantity_sold = int(input('Enter the quantity of the item you sell: '))
                    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    # Verificar se há quantidade suficiente disponível para venda
                    current_quantity = p_df.at[index, 'Quantidade']

                    if current_quantity >= quantity_sold:
                        # Subtrair a quantidade vendida da quantidade atual
                        new_quantity = current_quantity - quantity_sold
            
                        # Atualizar o DataFrame com a nova quantidade
                        p_df.at[index, 'Quantidade'] = new_quantity

                        # Salvar a linha modificada em outro arquivo CSV
                        modified_row = p_df.iloc[index].copy()
                        modified_row['DataHoraModificacao'] = current_datetime
                        h_df = pd.DataFrame([modified_row])
                        h_df.to_csv('History.csv', mode='a', header=not history_df_exists(), index=False)
                        p_df.to_csv('Products.csv', index=False)

                        # Registrar a venda no log
                        log_info = {'action': 'SALE', 'index': index, 'datetime': current_datetime, 'quantity_sold': quantity_sold}
                        Logger.registrar_log7(**log_info)

                        print("Sale registered successfully!!")
                    else:
                        print("Insufficient quantity available for sale.")
                else:
                    print("Invalid index. Please enter a valid index.")
            except ValueError:
                print("Invalid input. Please enter a valid index and quantity.")


        
        elif ent == '2':

            nome = 'History.csv'
            h_df = pd.read_csv(nome)

            print("""\n

            To track purchase orders, simply check the date and time in the PDF files generated.

            Here is the Sales History:

            \n""")
                
            print(h_df)
            
        while True:

                nome_produto = input("\nExit? (Y or N): ")
                
                if nome_produto == 'Y':
                    break

                else:

                    nome = 'History.csv'
                    h_df = pd.read_csv(nome)

                    print("""\n

                    To track purchase orders, simply check the date and time in the PDF files generated.

                    Here is the Sales History:

                    \n""")
                
                    print(h_df)


