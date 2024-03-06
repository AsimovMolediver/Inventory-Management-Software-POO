import pandas as pd
import csv
from datetime import datetime
from pyzbar.pyzbar import decode

class Produto:

    def __init__(self, nome, tipo, modelo, cor, tamanho, quantidade, preco, qtd_ideal, qtd_min):
        self.nome = nome
        self.tipo = tipo
        self.modelo = modelo
        self.cor = cor
        self.tamanho = tamanho
        self.quantidade = quantidade
        self.preco = preco
        self.qtd_ideal = qtd_ideal
        self.qtd_min = qtd_min

    @staticmethod
    def add_item(df, product, type, model, color, size, quantity, price, ideal, min):
        new_row = pd.DataFrame({'Produto': [product], 'Tipo': [type], 'Modelo': [model], 'Cor': [color], 
                                'Tamanho': [size], 'Quantidade': [quantity], 'Preço': [price], 'Qtd.Ideal':[ideal],'Qtd.Min': [min]})
        return pd.concat([df, new_row], ignore_index=True)
    
    @staticmethod
    def add_item_and_update_s(p_df, product, type, model, color, size, quantity, price, ideal, min):
        last_index = p_df.index[-1] if not p_df.empty else 0
        p_df = Produto.add_item(p_df, product, type, model, color, size, quantity, price, ideal, min)
        Logger.registrar_log('add_item_and_update_s', last_index + 1)
        return p_df

class AtualizadorItem:

    @staticmethod
    def adicionar_item(df, novo_item):
        return pd.concat([df, novo_item], ignore_index=True)

    @staticmethod
    def update_item(p_df, index, column, new_value):

        old_value = p_df.at[index, column]

        p_df.at[index, column] = new_value

        Logger.registrar_log('update_item', f"Index: {index}, Column: {column}, Old Value: {old_value}, New Value: {new_value}")

        return p_df
    
class Supplier:

    def __init__(self, supplier, product, contact, email, CEP, CNPJ):

        self.supplier = supplier
        self.product = product
        self.contact = contact
        self.email = email
        self.CEP = CEP
        self.CNPJ = CNPJ

    @staticmethod
    def add_s(s_df, supplier, product, contact, email, CEP, CNPJ):
        new_roll = pd.DataFrame({'Supplier':[supplier], 'Produto': [product], 'Contato': [contact], 'E-Mail': [email], 'CEP': [CEP], 'CNPJ': [CNPJ]})
        Logger.registrar_log('add_s', f"Supplier: {supplier}, Product: {product}")
        return pd.concat([s_df, new_roll], ignore_index=False)
        
    @staticmethod
    def listar_s(s_df, product):
        if product in s_df['Produto'].values:
         print(f"Fornecedor de : {s_df['Produto'].values}")

class Logger:

    def registrar_log(funcao, linha_modificada):
        data_hora_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = {'DataHora': data_hora_atual, 'Funcao': funcao, 'LinhaModificada': linha_modificada}
        with open('log.csv', 'a', newline='') as log_file:
            log_writer = csv.DictWriter(log_file, fieldnames=['DataHora', 'Funcao', 'LinhaModificada'])
            log_file == 0
            if log_file.tell() == 0:
                log_writer.writeheader()
            log_writer.writerow(log_entry)

    def registrar_log7(**linha_modificada):

        Logger.registrar_log('VENDA',linha_modificada)
        print("\n")

    def imprimir_csv():
        nome = 'log.csv'
        try:
            df = pd.read_csv(nome, encoding='utf-8')
        except UnicodeDecodeError:
            # Se ocorrer um erro, tente outro encoding
            df = pd.read_csv(nome, encoding='latin-1')
    
        print(df)   

class Load:
        
        data_hora_atual = datetime.now().strftime('%Y%m%d_%H%M%S')

        # Função para carregar fornecedores do CSV
        def carregar_fornecedores_csv():
            try:
                s_df = pd.read_csv('Suppliers.csv')
                return s_df
            except FileNotFoundError:
                print("Arquivo CSV 'Suppliers.csv' não encontrado. Certifique-se de que o arquivo está na mesma pasta que o script.")
                return None

        # Função para exibir a lista de fornecedores e permitir a escolha
        def selecionar_fornecedor(s_df):
            print("Selecione um fornecedor:")
            print(s_df)
            
            try:
                fornecedor_index = int(input("Digite o número do fornecedor desejado: "))
                return s_df.iloc[fornecedor_index].to_dict()
            except (ValueError, IndexError):
                print("Opção inválida. Certifique-se de selecionar um número válido.")
                return None


class Stock:

    def stock_lvl():

        nome = 'Products.csv'

        p_df = pd.read_csv(nome)

        condicao_critica = p_df['Quantidade'] < p_df['Qtd.Min']
        
        tudo_certo = True

        if any(condicao_critica):
            
            tudo_certo = False
            print('\n')
            print("Alert: Some products have less than the minimum quantity in stock! Please do a purchase order!")
            print('\n')
            print(p_df[condicao_critica][['Produto','Tipo','Modelo', 'Quantidade', 'Qtd.Min']])
            print("----")


        elif tudo_certo:

            print('\n')
            print('Everything is right. No products below critical or ideal values.')

class barcode:

    def read_code128(frame):

        barcodes = decode(frame)

        for barcode in barcodes:
            if barcode.type == 'QRCODE':
                code128_data = barcode.data.decode('utf-8')
            return code128_data
        return None

    def return_code_data(code128_data):
        return code128_data


