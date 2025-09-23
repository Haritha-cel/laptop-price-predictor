# 💻 Laptop Price Predictor

This project is a **Machine Learning-based web app** that predicts laptop prices based on user-selected specifications such as brand, processor, RAM, GPU, and display size.  
It uses **Streamlit** for the frontend and a trained **scikit-learn pipeline** for prediction.  

---

## 🚀 Features
- Interactive **Streamlit web app**  
- User inputs via dropdown menus (Brand, Processor, RAM, etc.)  
- Real-time **price prediction** using a trained ML model  
- Clean and minimal **UI with Streamlit**  

---

## 🛠 Tools & Technologies
- **Python 3** (primary language)  
- **Libraries**: pandas, numpy, scikit-learn, joblib, streamlit  
- **Data Visualization**: matplotlib, seaborn (for analysis)  
- **Dataset Source**: [Kaggle – Laptop Dataset](https://www.kaggle.com/datasets/pradeepjangirml007/laptop-data-set?resource=download)  
- **Jupyter Notebook** for analysis and model training  

---

## ⚡ Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/laptop-price-predictor.git
   cd laptop-price-predictor
```
2. Create a virtual environment (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Linux/Mac
   .venv\Scripts\activate      # On Windows
```
3. Install dependencies:
```bash
   pip install -r requirements.txt
```
4. Run the Streamlit app:
```bash
   streamlit run app.py
```
## Web app
```bash
   https://laptop-price-predictor-fwl46fwbefyyujsivspxrd.streamlit.app/
```