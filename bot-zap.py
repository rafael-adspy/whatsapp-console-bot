import pandas as pd
from time import sleep

total = 0

# ⚠️ ATENÇÃO: altere o caminho abaixo para o local do seu arquivo produtos.xlsx
CAMINHO_PRODUTOS = r"C:\Users\seu_usuario\caminho\para\produtos.xlsx"

# Lendo a planilha
tabela = pd.read_excel(CAMINHO_PRODUTOS)
tabela.columns = tabela.columns.str.strip()

while True:
    msg = input('Cliente: ').lower().strip()
    if msg in ('oi', 'bom dia', 'boa tarde', 'boa noite', 'opa', 'tudo bom', 'vocês', 'você', 'boa', 'ola', 'olá',
               'vcs'):
        print('digitando...')
        sleep(4)
        print('''🏗️ *Bem-vindo à Berseba Materiais de Construção!*

        Olá! 👋
        Obrigado por entrar em contato conosco. Será um prazer atendê-lo!

        Escolha uma das opções abaixo digitando o número correspondente:

        1️⃣ Orçamento de materiais
        2️⃣ Consultar preço de produto
        3️⃣ Prazo de entrega
        4️⃣ Falar com um atendente
        5️⃣ Endereço da loja

        📩 Assim que recebermos sua opção, iremos continuar o atendimento o mais rápido possível.''')

        op = input('Digite uma opção: ')

        if op == '1':
            total = 0
            itens_orcamento = []
            print("===== BERSEBA MATERIAIS DE CONSTRUÇÃO =====")
            print("Sistema de Orçamento\n")
            print("""
            🏗️ *PROMOÇÕES BERSEBA MATERIAIS*

            📦 Areia Lavada → R$110.00  
            🪨 Pedra 1 → R$140.00  
            🧱 Cimentos → a partir de R$29.90  
            🪵 Tábuas 30cm → R$25.90  

            📲 Digite o nome do produto para orçamento.
            💬 Ou digite *4* para falar com um atendente.
            """)
            while True:
                op_orcamento = input('Digite o nome do produto (ou sair): ').lower().strip()
                if op_orcamento == 'sair':
                    print('digitando...')
                    sleep(3)

                    print(f'{"RESUMO-DO-ORÇAMENTO":=^50}')
                    for item in itens_orcamento:
                        nome, quantidade, preco, subtotal = item
                        print(f'{nome:<25} {quantidade} x {preco} = {subtotal}')

                    print('~' * 40)
                    print(f'O Total do Orçamento é {total:.2f}')
                    print('~' * 40)

                    print('Voltando ao menu anterior')
                    break

                resultado = tabela[tabela["Nome"].str.lower().str.contains(op_orcamento, na=False)]

                if resultado.empty:
                    print('Produto nao encontrado')
                    continue

                print("\nProdutos encontrados:")

                for i, produto in enumerate(resultado["Nome"]):
                    print(f"{i + 1} - {produto}")

                try:
                    escolha = int(input("Escolha o número do produto: "))
                    if escolha < 1 or escolha > len(resultado):
                        print('Número Invalido')
                        continue

                    produto_escolhido = resultado.iloc[escolha - 1]
                except ValueError:
                    print('Digite Apenas Números')
                    continue

                nome = produto_escolhido["Nome"]
                if escolha < 1 or escolha > len(resultado):
                    print("Número inválido.")
                    continue

                preco = float(produto_escolhido["Preço"])
                try:
                    quantidade = int(input("Digite a quantidade: "))

                except ValueError:
                    print('Digite apenas números')
                    continue

                subtotal = preco * quantidade
                total += subtotal
                itens_orcamento.append((nome, quantidade, preco, subtotal))

                print(f'{nome} x {quantidade} = R${subtotal:.2f}')
                print(f'O TOTAL DO ORÇAMENTO É R${total:.2f}')
        elif op == '2':
            print()

        elif op == '3':
            print(f'''{"Observação – Prazo de Entrega":=^80}

            O prazo estimado para entrega é de até 3 (três) dias úteis,
            podendo sofrer alterações em casos de condições climáticas adversas,
            como chuvas intensas, que podem impactar a logística de transporte,
            uma vez que algumas ruas podem apresentar alagamentos, tornando
            inviável ou inseguro o trânsito de veículos de entrega.

            Não havendo interferência desses fatores, a Berseba Materiais de
            Construção empenha-se em antecipar as entregas sempre que possível,
            buscando oferecer maior agilidade, segurança no transporte e
            satisfação aos nossos clientes.
            ''')