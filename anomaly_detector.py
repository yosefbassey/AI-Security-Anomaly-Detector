import pandas as pd
from sklearn.ensemble import IsolationForest 
import matplotlib.pyplot as plt

df = pd.read_csv("server_logs.csv")

print(f"Loaded data with shape: {df.shape}")

features = df [ ["login_duration", "failed_attempts"] ]

print("Features selected for the AI.")

model = IsolationForest(contamination = 0.02, random_state = 42)

model.fit(features)

print("\u2705 AI Training Complete...")

df ["anomaly_score"] = model.predict(features)

anomalies = df [df ["anomaly_score"] == -1]

print("\n \U0001F50D YOSEF'S DETECTION REPORT:")

print(f" \n \U0001F464 Total Users Scanned: {len(df)}")

print(f" \U0001F977 Anomalies Detected: {len(anomalies)}")

print("\n                   ---THE ILLEGAL ONES --- \n")

print(anomalies.head(25)) 

plt.figure (figsize = (10, 6))

scatter = plt.scatter ( 
    df ["login_duration"],
    df ["failed_attempts"],
    c = df ["anomaly_score"],
    cmap = "coolwarm_r",
    alpha = 0.6
    )

plt.title("AI Detection Map: Isolation Forest Results")

plt.xlabel("Login Duration (Minutes)")

plt.ylabel("Failed Password Attempts")

plt.colorbar(scatter, label = "Anomaly Score")

plt.show()
