# 🏠 House Price Prediction - MLOps Pipeline

## Description
Projet d'évaluation Data Engineering & MLOps - Pipeline end-to-end de prédiction de prix immobilier avec Snowflake, Snowpark et Streamlit.

## Architecture
- **Ingestion** : Chargement des données JSON depuis S3 vers Snowflake
- **Transformation** : Nettoyage et préparation des données (1091 lignes)
- **Modélisation** : Comparaison de 4 algorithmes (Linear Regression, Random Forest, Gradient Boosting, XGBoost)
- **Meilleur modèle** : Random Forest - R2 = 0.9112
- **Model Registry** : Enregistrement dans Snowflake Model Registry (HOUSE_PRICE_PREDICTOR V1)
- **Application** : Streamlit pour la prédiction en temps réel

## Stack technique
- Snowflake / Snowpark
- scikit-learn / XGBoost
- snowflake-ml-python
- Streamlit

## Structure du repo
- `INESINESHIDECHE 2026-04-01 12:45:19/` → Notebook Snowflake
- `YDFPGGMT4IKRW2VB/` → Application Streamlit

## Auteur
Ines Hideche 
Camille Thauvin
