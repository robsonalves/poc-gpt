# Importa as bibliotecas necessárias do Flask e OpenAI
from flask import Flask, render_template, request, redirect, url_for
import openai

# Cria uma instância da aplicação Flask
app = Flask(__name__)

# Define a chave da API da OpenAI (substitua 'A_SUA_CHAVE_DA_API' pela sua chave real)
api_key = 'API-KEY'
# Inicializa o cliente da OpenAI com a chave da API
client = openai.OpenAI(api_key=api_key)

# Inicializa a conversa com uma mensagem de sistema
conversation = [{"role": "system", "content": "You are a helpful assistant."}]

# Define a função do chatbot
def chatbot(prompt):
    """
    Função que envia uma mensagem para a API da OpenAI e retorna a resposta do chatbot.
    """
    # Adiciona a mensagem do utilizador à conversa
    conversation.append({"role": "user", "content": prompt})
    
    # Faz a chamada à API da OpenAI com a conversa atualizada
    response = client.chat.completions.create(
        model="gpt-4",
        messages=conversation
    )
    
    # Obtém a resposta do assistente e adiciona à conversa
    message_content = response.choices[0].message.content.strip()
    conversation.append({"role": "assistant", "content": message_content})
    return message_content

# Define a rota principal
@app.route("/", methods=["GET", "POST"])
def home():
    """
    Função principal que gere as solicitações GET e POST.
    """
    global conversation
    if request.method == "POST":
        action = request.form.get("action")
        if action == "send":
            # Obtém a mensagem do utilizador do formulário
            user_input = request.form["user_input"]
            chatbot(user_input)
        elif action == "clear":
            # Limpa a conversa reiniciando-a
            conversation = [{"role": "system", "content": "You are a helpful assistant."}]
        return redirect(url_for('home'))
    return render_template("index.html", conversation=conversation)

# Executa a aplicação Flask
if __name__ == "__main__":
    app.run(debug=True)