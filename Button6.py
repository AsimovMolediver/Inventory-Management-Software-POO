import pandas as pd
import cv2
from pyzbar.pyzbar import decode
from Class import Logger, barcode

p_df = pd.read_csv('Products.csv')
p_df = pd.DataFrame(p_df)

class Opt6:

    def opt6(self):

        global p_df
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


