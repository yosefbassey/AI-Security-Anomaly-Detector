#  AI Security Anomaly Detector

## Project Overview
This project is a **Behavioral Analysis Tool** designed to detect potential security threats (hackers) within server logs. Instead of relying on static rules, it utilizes **Unsupervised Machine Learning** (Isolation Forest) to identify anomalies based on user behavior patterns.

## (How it Works)
The system operates on the principle that "Attackers behave differently from normal users."
1.  **Data Generation:** We simulate a dataset of 1,020 users (1,000 normal users + 20 malicious actors).
2.  **Feature Selection:** The AI analyzes two key behavioral dimensions:
    * `login_duration`: How long the user stays online.
    * `failed_attempts`: How many times they failed the password.
3.  **The Algorithm:** Using the **Isolation Forest** algorithm, the model isolates data points that deviate from the dense cluster of "normal" behavior.
4.  **Visualization:** A Matplotlib scatter plot renders the decision boundary, highlighting safe users in **Blue** and detected anomalies in **Red**.

## Technologies Used
* **Python 3.x**: The core logic.
* **Pandas**: For data manipulation and CSV handling.
* **Scikit-Learn**: For the Isolation Forest model.
* **Matplotlib**: For visualizing the detection map.

## How to Run the Experiment

### 1. Install Dependencies
You will need the standard data science libraries:
```bash
pip install pandas scikit-learn matplotlib