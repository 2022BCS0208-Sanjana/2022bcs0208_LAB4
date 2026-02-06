import json

with open("metrics.json") as f:
    metrics = json.load(f)

print("Model Evaluation Metrics")
print(metrics)
