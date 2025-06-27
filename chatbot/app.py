from flask import Flask, render_template, request, jsonify
import torch
import random
import json
from model import NeuralNet
from utils import bag_of_words, tokenize

app = Flask(__name__)
import nltk
nltk.download('punkt')


# Load intents
with open("data/intents.json", "r") as json_data:
    intents = json.load(json_data)

# Load hospitals
with open("data/medical_centers.json", "r") as f:
    hospitals_data = json.load(f)["intents"]

# Load model
FILE = "model.pth"
data = torch.load(FILE)
input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size)
model.load_state_dict(model_state)
model.eval()

# Search hospitals by keyword
def search_hospitals_by_area(query):
    matches = []
    for hospital in hospitals_data:
        name = hospital.get("tag", "")
        address = hospital.get("Address", "")
        if query.lower() in address.lower():
            matches.append(f"<b>{name}</b><br>{address}")
    return matches

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    msg = request.json["message"]
    print("🔹 User said:", msg)

    sentence = tokenize(msg)
    print("🔹 Tokenized:", sentence)

    X = bag_of_words(sentence, all_words)
    X = torch.tensor(X, dtype=torch.float32).unsqueeze(0)

    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]
    prob = torch.softmax(output, dim=1)[0][predicted.item()]
    print(f"🔹 Predicted tag: {tag} (Confidence: {prob:.2f})")

    if prob.item() > 0.6:
        for intent in intents["intents"]:
            if tag == intent["tag"]:

                # Location lookup logic
                if tag == "location_help":
                    print("🔍 Looking for hospitals in message...")
                    for word in sentence:
                        results = search_hospitals_by_area(word)
                        if results:
                            formatted = "<br><br>".join(results[:5])
                            print(f"✅ Found {len(results)} hospital(s) in {word}")
                            return jsonify({
                                "response": f"Here are some hospitals in <b>{word.title()}</b>:<br><br>{formatted}"
                            })
                    print("⚠️ No match found in hospital data")
                    return jsonify({
                        "response": "Please enter a location like 'Kilpauk' or 'Adyar'."
                    })

                # Normal intent
                response = random.choice(intent["responses"]).replace("<br>", "<br>")
                return jsonify({"response": response})

    print("⚠️ Low confidence or no match.")
    return jsonify({"response": "I'm not sure I understand. Can you rephrase?"})

if __name__ == "__main__":
    app.run(debug=True)
