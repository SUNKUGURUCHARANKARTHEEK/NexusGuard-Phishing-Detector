# 🛡️ NexusGuard – AI Spam Message Detector

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine_Learning-orange?logo=scikitlearn)
![License](https://img.shields.io/badge/License-MIT-green)

NexusGuard is an AI-powered **Spam Message Detection** web application developed using **Python**, **Machine Learning**, and **Streamlit**. It analyzes SMS or text messages and predicts whether they are **Spam** or **Ham (Legitimate)** using a trained **Multinomial Naive Bayes** model with **TF-IDF Vectorization**.

The project demonstrates the practical application of Artificial Intelligence in cybersecurity and communication by helping users identify suspicious or unwanted messages in real time.

---

## 🚀 Features

- 📩 Detects Spam and Legitimate (Ham) messages
- 🤖 Machine Learning-powered text classification
- ⚡ Real-time message analysis
- 📊 Prediction confidence visualization
- 📜 Session-based scan history
- 🎨 Modern cyber-themed Streamlit interface
- 📱 Responsive and user-friendly dashboard
- 🔍 Live message statistics

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Plotly
- TF-IDF Vectorizer
- Multinomial Naive Bayes

---

## 🧠 Machine Learning Model

### Algorithm

- Multinomial Naive Bayes

### Feature Extraction

- TF-IDF Vectorization

### Dataset

- SMS Spam Collection Dataset (`spam.csv`)

---

## 📁 Project Structure

```text
NexusGuard-Spam-Detector/
│
├── app.py                  # Streamlit application
├── train_model.py          # Model training script
├── spam.csv                # SMS Spam Collection dataset
├── model.pkl               # Trained Machine Learning model
├── vectorizer.pkl          # TF-IDF Vectorizer
├── requirements.txt        # Project dependencies
├── README.md
└── screenshots/
    ├── home.png
    ├── spam_result.png
    └── ham_result.png
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/SUNKUGURUCHARANKARTHEEK/NexusGuard-Spam-Detector.git
```

### Navigate to the Project Folder

```bash
cd NexusGuard-Spam-Detector
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Train the Model (Optional)

Run this only if you want to retrain the model.

```bash
python train_model.py
```

### Start the Streamlit Application

```bash
streamlit run app.py
```

---

## 🔍 How It Works

```text
             User Inputs Message
                     │
                     ▼
             Text Preprocessing
                     │
                     ▼
            TF-IDF Vectorization
                     │
                     ▼
      Multinomial Naive Bayes Model
                     │
                     ▼
         Spam ◄────────────► Ham
                     │
                     ▼
     Prediction + Confidence Score
```

---

## 📊 Model Information

| Model | Multinomial Naive Bayes |
|--------|--------------------------|
| Feature Extraction | TF-IDF Vectorizer |
| Dataset | SMS Spam Collection |
| Language | Python |
| Framework | Streamlit |

---

## 📸 Screenshots

Add screenshots inside the **screenshots/** folder.

```text
screenshots/
├── home.png
├── spam_result.png
└── ham_result.png
```

Example:

```markdown
![Home](screenshots/home.png)

![Spam Detection](screenshots/spam_result.png)

![Ham Detection](screenshots/ham_result.png)
```

---

## 📦 Requirements

Install all required packages using:

```bash
pip install -r requirements.txt
```

---

## 💡 Future Enhancements

- 🌐 Real-time phishing URL detection
- 📧 Email spam classification
- 🧠 Deep Learning models (LSTM/BERT)
- 🌍 Multi-language support
- 📄 Export scan history
- 🌙 Dark/Light theme toggle
- 🔌 REST API integration
- 📱 Mobile-friendly interface improvements

---

## 🤝 Contributing

Contributions are welcome!

1. Fork this repository.

2. Create a new branch.

```bash
git checkout -b feature/your-feature
```

3. Commit your changes.

```bash
git commit -m "Add your feature"
```

4. Push your branch.

```bash
git push origin feature/your-feature
```

5. Open a Pull Request.

---

## 👨‍💻 Author

### **Sunku Gurucharan Kartheek**

Computer Science Student | Machine Learning Enthusiast | Python Developer

🔗 **GitHub:**  
https://github.com/SUNKUGURUCHARANKARTHEEK

Feel free to explore my repositories, contribute to projects, or connect for collaboration.

---

## 📬 Contact

For suggestions, issues, or collaborations:

GitHub:
https://github.com/SUNKUGURUCHARANKARTHEEK

---

## 📄 License

This project is licensed under the **MIT License**.

---

## ⭐ Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub.

Your support motivates future improvements and more open-source AI projects.

---

### 🚀 Built with Python, Machine Learning, and Streamlit to make communication safer through AI.
