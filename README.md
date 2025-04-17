# WhatsPlus

# WhatsPlus - Integração de Atendimento via WhatsApp com Django e Twilio

Este projeto tem como objetivo implementar uma **automação de atendimento via WhatsApp** utilizando o backend em **Django**, a API de mensagens do **Twilio** e o **Ngrok** para testar localmente. O sistema responde automaticamente a perguntas frequentes de clientes, realizando uma integração simples entre as tecnologias.

---

## Tecnologias Usadas

- **Python 3.x**
- **Django 5.2**
- **Twilio API** (para integração com o WhatsApp)
- **Ngrok** (para criar um túnel e expor localmente o servidor Django ao público)
- **JSON** (para comunicação de dados entre o servidor e o Twilio)

---

## Funcionalidades

- **Webhook do WhatsApp**: Recebe as mensagens enviadas via WhatsApp e responde automaticamente utilizando a integração com a API do Twilio.
- **FAQ Dinâmico**: Implementação de um sistema de **FAQ** simples que pode ser facilmente expandido com novas perguntas e respostas.
- **Integração via Twilio**: Capacidade de enviar e receber mensagens via WhatsApp através da API Twilio.
- **Ambiente de Testes com Ngrok**: Exposição do servidor Django local através de um túnel, permitindo testar o webhook no ambiente de produção de forma simples.

---

## Pré-requisitos

Antes de rodar o projeto, certifique-se de que você tem as seguintes dependências instaladas:

1. Python 3.x
2. Django 5.2
3. Conta no Twilio (para obter **SID da conta** e **Token de autenticação**)
4. Ngrok (para criar o túnel)

### Instalando Dependências

Clone o repositório e crie um ambiente virtual:

```bash
git clone https://github.com/SeuUsuario/WhatsPlus.git
cd WhatsPlus
python -m venv .venv
```

Ative o ambiente virtual:

```bash
# No Windows
.venv\Scriptsctivate

# No Linux/Mac
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Rodando o Projeto

1. Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```
TWILIO_ACCOUNT_SID=<seu_account_sid>
TWILIO_AUTH_TOKEN=<seu_auth_token>
```

2. Inicie o servidor Django:

```bash
python manage.py runserver
```

3. Abra um novo terminal e inicie o Ngrok:

```bash
ngrok http 8000
```

4. Copie o **URL** gerado pelo Ngrok e coloque-o como **Webhook URL** na sua configuração do Twilio.

5. Pronto! O servidor está rodando localmente, e o Twilio irá direcionar as mensagens do WhatsApp para o seu servidor.

---

## Observações

- O Twilio só consegue enviar mensagens para o WhatsApp de números que estão verificados na sua conta. Lembre-se de adicionar e verificar números ao configurar sua conta do Twilio.
- O Ngrok é utilizado apenas para testes locais, em um ambiente de produção, é necessário configurar um servidor real.

---

## Contribuindo

Se você tem sugestões ou encontrou algum bug, sinta-se à vontade para abrir uma **issue** ou fazer um **pull request**.

---

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).
