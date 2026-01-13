import pandas as pd 
import random 

data = {
    "login_duration": [random.randint(1, 60) for _ in range(1000)],
    "failed_attempts": [random.randint(0, 1) for _ in range(1000)],
    "is_hacker": [0] * 1000
}

for _ in range (20): 
    data["login_duration"].append(random.randint(100, 500))
    data["failed_attempts"].append(random.randint(5, 20))
    data["is_hacker"].append(1)

df = pd.DataFrame (data)

df.to_csv("server_logs.csv", index=False)

print("\u2705 Data generated...")

