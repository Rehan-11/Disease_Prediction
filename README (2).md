
# 🩺 Disease Prediction from Symptoms

A **Machine Learning–powered web application** that predicts possible diseases based on user-selected symptoms. Built using **Streamlit**, **scikit-learn**, and a trained classification model, this app provides an interactive and easy-to-use interface for symptom-based disease prediction.

---

## 🚀 Features

- 🔍 Select multiple symptoms from a predefined list  
- 🤖 Predicts disease using a trained ML model  
- 🧠 Uses MultiLabel Binarization for symptom encoding  
- ⚡ Fast, lightweight, and interactive Streamlit UI  
- 🖥️ Easy to run locally  

---

## 🛠️ Tech Stack

- **Frontend / UI:** Streamlit  
- **Machine Learning:** scikit-learn  
- **Model Serialization:** joblib  
- **Language:** Python  
- **Data Processing:** NumPy  

---

## 📂 Project Structure

```
├── app.py
├── disease_model.pkl
├── symptom_encoder.pkl
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/disease-prediction-app.git
cd disease-prediction-app
```

### 2️⃣ Create Virtual Environment (Optional)
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open your browser at:
```
http://localhost:8501
```

---

## 🧠 How It Works

1. User selects symptoms  
2. Symptoms are encoded using MultiLabelBinarizer  
3. Encoded data is passed to the ML model  
4. Predicted disease is displayed instantly  

---

## ⚠️ Disclaimer

This application is for **educational purposes only** and should not be used as a substitute for professional medical advice.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👤 Author

Your Name  
  
LinkedIn: https://www.linkedin.com/in/rehan-parekh/
