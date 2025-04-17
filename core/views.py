import unicodedata
from django.http import JsonResponse, HttpResponse
from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt
from core.faq import FAQ

# Configuração da conta Twilio
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

# Função para enviar mensagem via WhatsApp
def send_whatsapp_message(to, body):
    message = client.messages.create(
        body=body,
        from_='whatsapp:+14155238886',
        to=to
    )
    return message.sid

# Função para normalizar o texto (remover acentos, espaços e caixa alta)
def normalize_text(text):
    text = text.lower().strip()
    text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8')
    return text

# Página inicial
def home(request):
    return HttpResponse("Bem-vindo ao WhatsPlus!")

# Webhook que trata as mensagens recebidas
@csrf_exempt
def whatsapp_webhook(request):
    if request.method == "POST":
        # O Twilio envia como application/x-www-form-urlencoded
        message = request.POST.get('Body', '')
        sender = request.POST.get('From')

        normalized_message = normalize_text(message)

        # Tenta encontrar resposta no FAQ
        resposta = FAQ.get(normalized_message, "Desculpe, não entendi sua pergunta. Pode tentar de outra forma?")

        # Envia a resposta via Twilio
        send_whatsapp_message(sender, resposta)

        return JsonResponse({"status": "success", "response": resposta})

    return JsonResponse({"status": "error", "message": "Método não permitido"}, status=405)
