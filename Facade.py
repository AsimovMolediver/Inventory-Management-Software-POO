import pandas as pd
from Class import Produto, AtualizadorItem, Supplier, Logger, Load, Stock, barcode
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from datetime import date, datetime
import cv2
from pyzbar.pyzbar import decode

class facade:

    def opt1():
        # Novo Item!

        def print_df(df):
            print(df)

        p_df = pd.read_csv('Products.csv')

        s_df = pd.read_csv('Suppliers.csv')

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

    def opt2():

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
                    p_df = AtualizadorItem.update_item(p_df, index, column, new_value)
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

    def opt3():
     
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
                    s_df = AtualizadorItem.update_item(s_df, index, column, new_value)
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
    
    def opt4():

        p_df = pd.read_csv('Products.csv')

        c_df = pd.read_csv('Calculo.csv')

        t_df = pd.read_csv('Total.csv')


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

    def opt5():

        data_hora_atual = datetime.now().strftime('%Y%m%d_%H%M%S')

        s_df = Load.carregar_fornecedores_csv()

        # Verificar se os fornecedores foram carregados com sucesso
        if s_df is not None:
            # Chamar a função para selecionar um fornecedor
            dados_fornecedor = Load.selecionar_fornecedor(s_df)

            if dados_fornecedor is not None:
                # Chamar a função para criar a ordem de compra
                output_pdf = f'OC_{data_hora_atual}.pdf'
                criar_template_ordem_compra(output_pdf, dados_fornecedor)
        else:
            print("Erro ao carregar dados dos fornecedores. Certifique-se de que o arquivo CSV está correto.")


        def criar_template_ordem_compra(output_pdf, dados_fornecedor):
            # Configurar o PDF usando reportlab
            pdf = SimpleDocTemplate(output_pdf, pagesize=letter, rightMargin=20, leftMargin=20, topMargin=30, bottomMargin=20)
            styles = getSampleStyleSheet()

            # Lista para armazenar os elementos do PDF
            elementos = []

            # Adicionar informações do fornecedor
            elementos.append(Paragraph("<u>Dados do Fornecedor</u>", styles['Heading1']))
            elementos.append(Spacer(1, 12))

            for chave, valor in dados_fornecedor.items():
                info_fornecedor = f"<b>{chave}:</b> {valor}"
                paragrafo = Paragraph(info_fornecedor, styles['BodyText'])
                elementos.append(paragrafo)
                elementos.append(Spacer(1, 6))

            # Adicionar tabela com detalhes dos itens
            elementos.append(Spacer(1, 12))
            elementos.append(Paragraph("<u>Detalhes dos Itens</u>", styles['Heading1']))
            elementos.append(Spacer(1, 6))

            cabecalho = ["Nome do Produto", "Tipo", "Quantidade", "Preço Unitário", "Subtotal"]
            dados_tabela = [cabecalho]

            valor_total = 0

            while True:
                nome_produto = input("Nome do Produto (ou 'exit' para encerrar): ")
                if nome_produto.lower() == 'exit':
                    break

                tipo = input("Tipo: ")
                quantidade = int(input("Quantidade: "))
                preco_unitario = float(input("Preço Unitário: "))

                subtotal = quantidade * preco_unitario
                valor_total += subtotal
                Logger.registrar_log('criar_template_ordem_compra', f"Output PDF: {output_pdf}, Fornecedor: {dados_fornecedor['Supplier']}, Valor Total: {valor_total}")
                dados_tabela.append([nome_produto, tipo, quantidade, f'R${preco_unitario:.2f}', f'R${subtotal:.2f}'])

            tabela = Table(dados_tabela, style=[
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ])

            elementos.append(tabela)
            elementos.append(Spacer(1, 12))

            # Adicionar o valor total
            elementos.append(Paragraph(f"<b>Valor Total:</b> R${valor_total:.2f}", styles['Heading2']))

            # Adicionar a data de emissão
            elementos.append(Spacer(1, 12))
            data_atual = date.today().strftime('%d/%m/%Y')
            elementos.append(Paragraph(f"<b>Data de Emissão:</b> {data_atual}", styles['BodyText']))

            

            pdf.build(elementos)

            print(f"Template de ordem de compra salvo como {output_pdf}")


    def opt6():
            
        global p_df
        p_df = pd.read_csv('Products.csv')
        p_df = pd.DataFrame(p_df)

        cap = cv2.VideoCapture(0)

        print("Câmera aberta! Centralize o código de barras (Tipo QRCode) e certifique-se de estar visível. Com a câmera aberta, pressione q para sair.")
        
        while True:
            _, frame = cap.read()

            # Adicionar uma borda ao redor da área desejada
            border_thickness = 2
            border_color = (0, 255, 0)  # Cor no formato BGR (verde)
            frame_with_border = cv2.copyMakeBorder(frame, border_thickness, border_thickness, border_thickness, border_thickness, cv2.BORDER_CONSTANT, value=border_color)

            # Chamar a função para ler o código de barras Code 128
            code128_data = barcode.read_code128(frame)

            # Exibir o frame com a borda
            cv2.imshow('Câmera', frame_with_border)

            # Armazenar o valor do código de barras
            if code128_data:
                print(f'\nCódigo QR detectado: {code128_data}\n')
                lista = [item.strip() for item in code128_data.split(",")]
                new_df = pd.DataFrame([{'Produto': lista[0], 'Tipo': lista[1], 'Modelo': lista[2], 'Cor': lista[3], 
                                        'Tamanho': lista[4], 'Quantidade': int(lista[5]), 'Preço': float(lista[6])}])
                existing_index = p_df[(p_df['Produto'] == lista[0]) & (p_df['Tipo'] == lista[1]) & (p_df['Modelo'] == lista[2])].index
                cv2.destroyAllWindows()

                if not existing_index.empty:
                    print("Item already exists. Let's just add the value")
                    soma = int(new_df.at[0, 'Quantidade'])
                    p_df.at[existing_index[0], 'Quantidade'] += soma
                    p_df.to_csv('Products.csv', index=False)
                    linha_modificada = existing_index[0]
                    Logger.registrar_log('INSERT', linha_modificada)
                    break
                else:
                    print("NEW ITEM!!")
                    p_df = pd.concat([p_df, new_df], ignore_index=True)
                    p_df.to_csv('Products.csv', index=False)
                    linha_modificada = len(p_df) - 1
                    Logger.registrar_log('INSERT', linha_modificada)
                    break

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Liberar os recursos
        print(p_df)
        cap.release()
        cv2.destroyAllWindows()
    

    def opt7():
            nome = 'Products.csv'
            p_df = pd.read_csv(nome)

            def history_df_exists():
                try:
                    pd.read_csv('History.csv')
                    return True
                except FileNotFoundError:
                    return False

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
                        new_value = input(f'Enter the quantity of the item you sell: ')
                        # Salvar a data e hora atual
                        current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        # Atualizar o DataFrame
                        p_df = AtualizadorItem.update_item(p_df, index, column, new_value)
                        # Salvar a linha modificada em outro arquivo CSV
                        modified_row = p_df.iloc[index].copy()
                        modified_row['DataHoraModificacao'] = current_datetime
                        h_df = pd.DataFrame([modified_row])
                        h_df.to_csv('History.csv', mode='a', header=not history_df_exists(), index=False)
                        p_df.to_csv('Products.csv', index=False)
                        log_info = {'action': 'SALE', 'index': index, 'datetime': current_datetime, **modified_row.to_dict()}
                        Logger.registrar_log7(**log_info)
                        print("Sale registered successfully!!")
                    else:
                        print("Invalid index. Please enter a valid index.")
                except ValueError:
                    print("Invalid input. Please enter a valid index.")
            
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





