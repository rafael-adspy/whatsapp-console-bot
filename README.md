 WhatsApp Console Bot - Berseba Materiais

💬 **Bot de console em Python para Berseba Materiais de Construção**  
Este projeto é um bot de teste que simula atendimento via WhatsApp, com menu interativo, orçamento de produtos e consulta de preços usando planilha Excel.

---

## Funcionalidades

- Recebe cumprimentos e responde automaticamente com mensagem de boas-vindas
- Menu interativo com opções:
  1. Orçamento de materiais
  2. Consultar preço de produto
  3. Prazo de entrega
  4. Falar com um atendente
  5. Endereço da loja
- Sistema de orçamento:
  - Consulta produtos em planilha Excel
  - Calcula subtotal e total do orçamento
  - Permite adicionar múltiplos produtos
- Exibe resumo final do orçamento no console

---

## Como usar

1. Clone o repositório:

```bash
git clone https://github.com/rafael-adspy/whatsapp-console-bot.git

Instale as dependências:

pip install pandas openpyxl

Coloque a planilha produtos.xlsx na mesma pasta do arquivo Python ou altere o caminho no código:

CAMINHO_PRODUTOS = r"caminho/para/seu/produtos.xlsx"

Execute o bot:

python chat-bot01.py

Interaja no console seguindo o menu de opções.

Estrutura do projeto
whatsapp-console-bot/

* chat-bot01.py        # Código principal do bot

* produtos.xlsx        # Planilha de produtos

* README.md            # Este arquivo
Observações

Este bot é de console, não envia mensagens reais pelo WhatsApp.

A lógica do bot pode ser usada futuramente em integração com WhatsApp Cloud API ou plataformas como n8n, permitindo envio e recebimento de mensagens reais.

Feche o Excel antes de rodar o script para evitar erros de permissão.

Tecnologias utilizadas

Python 3.10+

Pandas

Openpyxl (para ler arquivos Excel)
