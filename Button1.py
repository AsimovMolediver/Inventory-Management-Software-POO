import pandas as pd
from Class import Produto, Supplier

def print_df(df):
    print(df)

class Opt1:

    def print_df(df):
        print(df)

    def opt1(self):
        # Novo Item!

        nome = 'Products.csv'

        p_df = pd.read_csv(nome)

        nome = 'Suppliers.csv'

        s_df = pd.read_csv(nome)

        print('\nThe actual itens:\n')
        print_df(p_df)
        print("\n")

        print("Please enter in this sequence atributes product (with no accent):")

        product = input('Product: ')
        type = input('Type: ')
        model = input('Model: ')
        color = input('Color: ')
        size = input('Size: ')
        quantity = input('Quantity: ')
        price = input('Preço: ')
        ideal = input('Qtd.Ideal: ')
        min = input('Qtd.Min: ')

        # Se não tiver quantidade vai ficar sendo zero
        quantity = 0 if not quantity else quantity

        # Chama o método para adicionar os itens
        p_df = Produto.add_item_and_update_s(p_df, product, type, model, color, size, quantity, price, ideal, min)

        print("Item added successfully!")
        print_df(p_df)
        print("\n")

        p_df.to_csv("Products.csv", index=False)

        print('Actual suppliers:')
        print("\n")
        print_df(s_df)
        print("\n")

        sup = input('Would you like to add a new supplier to this item? Y/N: ')

        if sup == 'Y':
            supplier = input('Supplier: ')
            contact = input('Contact: ')
            email = input('E-mail: ')
            CEP = input('CEp: ')
            CNPJ = input('CNPJ: ')
            s_df = Supplier.add_s(s_df, supplier, product, contact, email, CEP, CNPJ)
            s_df.to_csv('Suppliers.csv', index=False)

            print('New Supplier! To update the informations select the option 3.')
            print('\n')
            print(s_df)
            print('\n')

        elif sup == 'N':
            print('Ok!')
            print('\n')
