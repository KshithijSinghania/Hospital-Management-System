from flask import Flask, render_template, request, jsonify
import torch
import random
import json
from model import NeuralNet
from utils import bag_of_words, tokenize
from collections import Counter
import nltk

app = Flask(__name__)
nltk.download('punkt')

# Load intents
with open("chatbot/data/intents.json", "r", encoding="utf-8") as f:
    intents = json.load(f)

# Load symptom-to-disease map
with open("chatbot/data/symptom_disease_map.json", "r", encoding="utf-8") as f:
    symptom_map = json.load(f)

# Load model
data = torch.load("chatbot/model.pth")
input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size)
model.load_state_dict(model_state)
model.eval()

# In-memory symptom collection
session_state = {
    "symptoms": [],
    "collecting": True
}

# Symptom follow-up options
common_symptoms = [
    "fever", "fatigue", "sore throat", "cough", "headache", "chest pain", "nausea",
    "vomiting", "diarrhea", "shortness of breath", "joint pain", "rash", "back pain", "abdominal pain"
]

# Reasoning logic using symptom map and pattern match
def predict_disease(symptoms, raw_message):
    raw_message = raw_message.lower()
    score = Counter()

    # From symptom map
    for key in symptom_map:
        if key in raw_message:
            for disease in symptom_map[key]:
                score[disease] += 1

    # From intents' training patterns
    for intent in intents["intents"]:
        for pattern in intent.get("patterns", []):
            if pattern.lower() in raw_message:
                score[intent["tag"]] += 1

    return score.most_common(3)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    msg = request.json["message"]
    print("🔹 User said:", msg)

    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = torch.tensor(X, dtype=torch.float32).unsqueeze(0)

    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]
    prob = torch.softmax(output, dim=1)[0][predicted.item()]
    print(f"🔹 Predicted tag: {tag} (Confidence: {prob:.2f})")

    # ✅ Check for any symptom match in user message (not just tag!)
    for key in symptom_map:
        if key.lower() in msg.lower():
            if key not in session_state["symptoms"]:
                session_state["symptoms"].append(key)
                print("🧠 Collected symptoms so far:", session_state["symptoms"])
                break

    # 🤖 Ask follow-up if only one symptom so far
    if len(session_state["symptoms"]) == 1:
        remaining = [s for s in common_symptoms if s not in [sym.lower() for sym in session_state["symptoms"]]]
        followup = random.sample(remaining, 3)
        return jsonify({
            "response": f"Got it. Do you also have {', '.join(followup)}?"
        })

    # 🧠 If 2 or more symptoms, start reasoning
    elif len(session_state["symptoms"]) >= 2:
        top = predict_disease(session_state["symptoms"], msg)
        top = [(d, s) for d, s in top if s >= 1]

        if top:
            result = "Based on your symptoms, you may have:<br><br>"
            for dis, sc in top:
                result += f"• <b>{dis}</b><br>"
            result += "<br>Please see a doctor.<br>"
            return jsonify({"response": result})
        else:
            return jsonify({"response": "Can you describe any other symptoms you're having?"})

    # 🎯 Fallback to normal intent-based reply
    if prob.item() > 0.6:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                return jsonify({"response": random.choice(intent["responses"])})

    return jsonify({"response": "I'm not sure I understand. Can you rephrase or share more symptoms?"})

if __name__ == "__main__":
    app.run(debug=True)
