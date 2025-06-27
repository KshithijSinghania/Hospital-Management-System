import torch
import random
import json
from model import NeuralNet
from utils import bag_of_words, tokenize

# Load intents
with open("data/intents.json", "r") as json_data:
    intents = json.load(json_data)

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

bot_name = "MediBot"
print(f"{bot_name}: Hello! Type 'quit' to stop.\n")

while True:
    sentence = input("You: ")
    if sentence.lower() == "quit":
        print(f"{bot_name}: Take care! 👋")
        break

    sentence_tokens = tokenize(sentence)
    X = bag_of_words(sentence_tokens, all_words)
    X = torch.tensor(X, dtype=torch.float32).unsqueeze(0)

    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.6:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                response = random.choice(intent["responses"]).replace("<br>", "\n")
                print(f"{bot_name}: {response}")
    else:
        print(f"{bot_name}: I'm not sure I understand. Can you rephrase?")
