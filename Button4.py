import pandas as pd
from Class import Logger

nome = 'Products.csv'
p_df = pd.read_csv(nome)

nome = 'Calculo.csv'
c_df = pd.read_csv(nome)

nome = 'Total.csv'
t_df = pd.read_csv(nome)


class Opt4:

    def opt4(self):
        while True:

            nome_produto = input("\nShow? (Y or N): ")
                
            if nome_produto == 'N':
                break

            else:
                try:
                    # Assume que o usuário insere um índice válido
                    index = int(input('\nEnter a number (just for register):'))

                    # Calcula os valores
                    c_df['Valores'] = p_df['Quantidade'] * p_df['Preço']
                    total_value = c_df['Valores'].sum()

                    # Registra a ação no log
                    Logger.registrar_log('opt4', f"Index: {index}, Total Value: {total_value}")

                    # Atualiza o DataFrame de Total
                    t_df = pd.DataFrame({'Total': [total_value]})
                    t_df.to_csv('Total.csv', index=False)

                    print('\n')
                    print(f'The total value in inventory is: {total_value}')
                    print('\n')
                except ValueError:
                    print("Invalid input. Please enter a valid index.")
