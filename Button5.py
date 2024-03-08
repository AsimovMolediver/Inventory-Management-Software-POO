from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from datetime import date, datetime
from Class import Logger, Load

class Opt5:

    def opt5(self):

        data_hora_atual = datetime.now().strftime('%Y%m%d_%H%M%S')

        s_df = Load.carregar_fornecedores_csv()

        # Verificar se os fornecedores foram carregados com sucesso
        if s_df is not None:
            # Chamar a função para selecionar um fornecedor
            dados_fornecedor = Load.selecionar_fornecedor(s_df)

            if dados_fornecedor is not None:
                # Chamar a função para criar a ordem de compra
                output_pdf = f'OC_{data_hora_atual}.pdf'
                self.criar_template_ordem_compra(output_pdf, dados_fornecedor)
        else:
            print("Erro ao carregar dados dos fornecedores. Certifique-se de que o arquivo CSV está correto.")


    def criar_template_ordem_compra(self,output_pdf, dados_fornecedor):
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
