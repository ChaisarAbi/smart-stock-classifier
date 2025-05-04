## 📦 Inventory Classification App — ABC & XYZ Analysis

Welcome to the Inventory Classification App! This project combines **machine learning** and **inventory analytics** to classify products based on **ABC (value-based)** and **XYZ (demand variability)** analysis. Built with ❤️ using **Scikit-learn + Streamlit**.
![image](https://github.com/user-attachments/assets/457555ef-2012-4775-b59d-a10341a5e538)
![image](https://github.com/user-attachments/assets/33cdd733-b9dc-4bb6-a814-d6b9bf98cd71)
![image](https://github.com/user-attachments/assets/c0a63abd-db7c-4fe4-8e7d-8812b5f1da3a)



---

## 🚀 Project Highlights

* 🧠 **Dual ML Models**: Predicts ABC and XYZ classes using two Random Forest classifiers
* 📂 **File Upload Feature**: Upload your own inventory data and get instant classifications
* ⚙️ **Feature Engineered**: Uses sales, demand stats, and variability measures
* 🌐 **Deployed with Streamlit**: Simple and accessible user interface
* 📊 **High Accuracy**: Cross-validated accuracy of 99.6% for both models

---

## 🏗️ How It Works

1. Upload your inventory `.csv` file
2. The app preprocesses the input and applies the trained models
3. You get a new dataset with `ABC_Class` and `XYZ_Class` columns predicted

---

## 📁 Project Structure

```
📦 Inventory-op/
├── app/
│   └── app.py              ← Streamlit app interface
|   ├── abc_classifier.pkl  ← Trained ABC model
│   └── xyz_classifier.pkl  ← Trained XYZ model
├── data/
│   └── final_engineered_inventory.csv ← Processed training data
├── utils/
│   └── preprocessing.py    ← Feature engineering (to be automated soon!)
└── README.md               ← You’re here!
```

---

## 🧪 Model Training

* Trained on processed inventory data with columns like `Total_Annual_Units`, `Demand_CV`, and `Total_Sales_Value`
* Used `StratifiedKFold` for robust validation
* Models saved using `joblib`

---

## 🖥️ Requirements

```bash
pip install -r requirements.txt
```

Make sure you have `streamlit`, `pandas`, `scikit-learn`, and `joblib`.

---

## ▶️ Running the App

```bash
streamlit run app/app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.
or you can check here : https://smart-stock-classifier-fglk3gkvuntesbf5dfdq8c.streamlit.app/

---

## 🎯 Next Milestones

* [ ] Automate preprocessing for raw `.csv` uploads
* [ ] Add download option for results
* [ ] Add inventory health dashboard 📈

---

## 👋 A Note from the Creator

This is my first deployed machine learning app using Streamlit! Still learning, improving, and having fun with it. Feedback is welcome 😊
