# Loan-Approval-Prediction
This Machine Learning project predict the possibilities of loan approved or declined.





```markdown
# 🏦 Loan Approval Prediction

This project is a machine learning-based web application that predicts whether a loan should be approved or not based on applicant details like income, credit history, employment status, and more.

## 🚀 Project Overview

The model is trained using a **Random Forest Classifier** and deployed through a Flask backend with an HTML frontend interface. The dataset used is a collection of past loan applications with labeled approvals.

## 📂 Project Structure

```

Loan-Approval-Prediction/
│
├── Loan\_Approval.ipynb         # Model training & evaluation
├── loan.csv                    # Dataset
├── loan\_model.pkl              # Trained Random Forest model
├── loan\_features.pkl           # Feature encoder/transformer
├── loan\_approval.py            # Model helper script
├── app.py                      # Flask backend
├── templates/
│   └── index.html              # Frontend form UI
├── feature\_importance.png      # Visual representation of feature importances
└── README.md                   # Project documentation (you are here)

````

## 📊 Features Used for Prediction

- Gender
- Marital Status
- Dependents
- Education
- Self-Employed Status
- Applicant Income
- Coapplicant Income
- Loan Amount
- Loan Term
- Credit History
- Property Area (Urban=0, Rural=1, Semi-Urban=2)

## 🧠 Model Details

- **Algorithm**: Random Forest Classifier
- **Accuracy**: High precision on validation data
- **Important Feature**: `Credit_History` is the most influential predictor

## 🌐 How to Run the App Locally

### 1. Clone the Repo
```bash
git clone https://github.com/SamStephen007/Loan-Approval-Prediction.git
cd Loan-Approval-Prediction
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Flask App

```bash
python app.py
```

### 4. Open in Browser

Navigate to:
`http://127.0.0.1:5000/`

## 📸 Demo Screenshot

> *(You can add a screenshot of the web app here)*

## 🔄 Future Improvements

* Add database integration for storing application records
* Improve UI using Bootstrap or React
* Add detailed error messages for invalid inputs

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

## 📝 License

This project is open source and free to use under the [MIT License](LICENSE).

---

````

---

### ✅ Next Steps:
1. Save this as a file named `README.md` in your project folder.
2. Then commit and push:
```bash
git add README.md
git commit -m "Added project README"
git push origin main
````
