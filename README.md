# 🌐 Network Forensics Project

A machine learning-based **Network Traffic Analyzer** that detects anomalies and attacks in network data using a **Random Forest Classifier**.  
It also includes a **Streamlit-based web app** for real-time analysis.

---

## 🚀 Features
- Detects attack vs normal traffic
- Generates forensic reports automatically
- Streamlit-based interactive dashboard
- Supports custom dataset uploads for testing

---

## 🧠 Model Details
- **Algorithm:** Random Forest Classifier  
- **Accuracy:** ~88.64%  
- **Dataset:** `dataset.csv`

---

## 🧩 Project Structure
Network_Forensics_Project/
├── main.py # Trains the model and generates reports
├── app.py # Streamlit dashboard for analysis
├── data/ # Training & test data
├── forensic_report/ # Auto-generated forensic report
├── model.pkl # Saved trained model
├── feature_columns.pkl # Saved feature names
├── requirements.txt # Dependencies
└── README.md # Project documentation

yaml
Copy code

---

## 💻 How to Run

### 1️⃣ Clone this repository
```bash
git clone https://github.com/<your-username>/Network_Forensics_Project.git
cd Network_Forensics_Project
2️⃣ Create a virtual environment
bash
Copy code
python -m venv venv
venv\Scripts\activate     # On Windows
# or
source venv/bin/activate  # On Mac/Linux
3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Train the model
bash
Copy code
python main.py
5️⃣ Run the Streamlit app
bash
Copy code
streamlit run app.py
📈 Example Output
Model Accuracy: 88.64%

Forensic Report: forensic_report/report.txt

Web App: http://localhost:8501

🧑‍💻 Author
Harsh Vaishnav
🎓 Computer Engineering | AI & ML Enthusiast

yaml
Copy code

---

## 🌍 STEP 4: Initialize Git and Upload to GitHub

Open your terminal in your project folder and run these commands one by one:

```bash
git init
git add .
git commit -m "Initial commit - Network Forensics Project"
git branch -M main
git remote add origin https://github.com/<your-username>/Network_Forensics_Project.git
git push -u origin main