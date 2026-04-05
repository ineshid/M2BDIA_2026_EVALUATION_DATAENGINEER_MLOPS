import streamlit as st
import pandas as pd
from snowflake.snowpark.context import get_active_session
from snowflake.ml.registry import Registry

st.title("🏠 House Price Predictor")
st.write("Entrez les caractéristiques de la maison pour prédire son prix.")

session = get_active_session()
reg = Registry(session=session, database_name="HOUSE_PRICE_DB", schema_name="ML")
model = reg.get_model("HOUSE_PRICE_PREDICTOR").version("V1")

col1, col2 = st.columns(2)

with col1:
    area = st.number_input("Surface (sqft)", min_value=500, max_value=10000, value=3000)
    bedrooms = st.slider("Chambres", 1, 6, 3)
    bathrooms = st.slider("Salles de bain", 1, 4, 2)
    stories = st.slider("Étages", 1, 4, 2)
    parking = st.slider("Parking", 0, 3, 1)
    furnishing = st.selectbox("Ameublement", options=[0, 1, 2], format_func=lambda x: ["Non meublé", "Semi-meublé", "Meublé"][x])

with col2:
    mainroad = st.selectbox("Route principale", [0, 1], format_func=lambda x: "Non" if x == 0 else "Oui")
    guestroom = st.selectbox("Chambre d'amis", [0, 1], format_func=lambda x: "Non" if x == 0 else "Oui")
    basement = st.selectbox("Sous-sol", [0, 1], format_func=lambda x: "Non" if x == 0 else "Oui")
    hotwaterheating = st.selectbox("Eau chaude", [0, 1], format_func=lambda x: "Non" if x == 0 else "Oui")
    airconditioning = st.selectbox("Climatisation", [0, 1], format_func=lambda x: "Non" if x == 0 else "Oui")
    prefarea = st.selectbox("Zone préférentielle", [0, 1], format_func=lambda x: "Non" if x == 0 else "Oui")

if st.button("💰 Prédire le prix"):
    input_data = pd.DataFrame([{
        'AREA': area, 'BEDROOMS': bedrooms, 'BATHROOMS': bathrooms,
        'STORIES': stories, 'MAINROAD': mainroad, 'GUESTROOM': guestroom,
        'BASEMENT': basement, 'HOTWATERHEATING': hotwaterheating,
        'AIRCONDITIONING': airconditioning, 'PARKING': parking,
        'PREFAREA': prefarea, 'FURNISHINGSTATUS': furnishing
    }])
    
    prediction = model.run(input_data, function_name="predict")
    price = prediction['output_feature_0'].values[0]
    
    st.success(f"💰 Prix estimé : **{price:,.0f} $**")