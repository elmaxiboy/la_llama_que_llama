from flask import Flask, request, jsonify, render_template
from llama_cpp import Llama


app = Flask(__name__)


model = Llama(model_path="/home/max-escobar-viegas/llama.cpp/models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf")

@app.route("/", methods =["GET"])
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    response = model.create_chat_completion(
        messages=[
            {"role": "system", "content": "You are a helpful and concise assistant."},
            {"role": "user", "content": user_message}
        ]
    )
    content = response["choices"][0]["message"]["content"]
    return jsonify({"response": content})

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
