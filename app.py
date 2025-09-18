import streamlit as st
import pandas as pd
import joblib

# Load trained pipeline
model = joblib.load("laptop_price_model.pkl")

# Columns used in training 
columns = [
    'Brand', 'Processor_Brand', 'Processor_Name', 'RAM_TYPE',
    'RAM_Expandable', 'GPU_Brand', 'Display_type', 'Display',
    'RAM', 'SSD', 'Ghz', 'Adapter'
]

st.set_page_config(page_title="Laptop Price Predictor", page_icon="💻", layout="centered")

st.title("💻 Laptop Price Predictor")
st.markdown("### Select laptop details to estimate the price")

# --- Input form ---
with st.form("laptop_form"):
    col1, col2 = st.columns(2)

    with col1:
        brand = st.selectbox("🏷️ Brand", ["ASUS", "Acer", "Apple", "Dell", "HP", "Lenovo", "MSI", "Microsoft"])
        processor_brand = st.selectbox("🔧 Processor Brand", ["Intel", "AMD", "Apple", "Other"])
        gpu_brand = st.selectbox("🎮 GPU Brand", ["NVIDIA", "AMD", "Intel", "Other"])
        display_type = st.selectbox("🖥️ Display Type", ["LCD","LED","OLED","Other"])

    with col2:
        display = st.selectbox("📏 Display Size (inches)", [11.6,12.0,13.3,14.0,15.6,16.0,17.3])
        ram = st.selectbox("💾 RAM (GB)", [2,3,4,6,8,12,16,24,32,64])
        ssd = st.selectbox("💽 SSD (GB)", [64,128,256,512,1024,2048,4098])
        ghz = st.selectbox("⚡ Processor Speed (GHz)", [2.0,2.9,3.3,4.2,4.7,5.5])
        adapter = st.selectbox("🔌 Adapter Power (W)", [45,65,90,100])

    submitted = st.form_submit_button("🔮 Predict Price")

# --- Prediction ---
if submitted:
    user_input = {
        'Brand': brand,
        'Processor_Brand': processor_brand,
        'GPU_Brand': gpu_brand,
        'Display_type': display_type,
        'Display': display,
        'RAM': ram,
        'SSD': ssd,
        'Ghz': ghz,
        'Adapter': adapter
    }

    input_df = pd.DataFrame([user_input], columns=columns)
    prediction = model.predict(input_df)[0]

    st.success(f"💰 Predicted Laptop Price: **Indian Rs. {prediction:,.2f}**")
    st.balloons()

