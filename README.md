# 🏠 House Price Prediction - MLOps Pipeline

## Description

Projet d'évaluation Data Engineering & MLOps - Pipeline end-to-end de prédiction 
de prix immobilier avec Snowflake, Snowpark et Streamlit.

## Auteurs

- Ines Hideche
- Camille Thauvin

---

## Architecture du pipeline

1. **Ingestion** : Chargement des données JSON depuis S3 (`s3://logbrain-datalake/datasets/house_price/`) vers Snowflake
2. **Exploration** : Analyse statistique, matrice de corrélation, distribution des prix
3. **Préparation** : Encodage des variables catégorielles, normalisation (StandardScaler), split 80/20
4. **Modélisation** : Comparaison de 4 algorithmes
5. **Optimisation** : RandomizedSearchCV sur Random Forest
6. **Model Registry** : Enregistrement dans Snowflake Model Registry
7. **Inférence** : Prédictions stockées dans une table Snowflake
8. **Application** : Streamlit pour la prédiction en temps réel

---

## Dataset

1090 lignes, 13 colonnes. Aucune valeur manquante.

| Colonne | Description |
|---|---|
| PRICE | Prix de vente (variable cible) |
| AREA | Surface en m² |
| BEDROOMS | Nombre de chambres |
| BATHROOMS | Nombre de salles de bain |
| STORIES | Nombre d'étages |
| MAINROAD | Accès route principale (oui/non) |
| GUESTROOM | Chambre d'amis (oui/non) |
| BASEMENT | Sous-sol (oui/non) |
| HOTWATERHEATING | Chauffage eau chaude (oui/non) |
| AIRCONDITIONING | Climatisation (oui/non) |
| PARKING | Nombre de places de parking |
| PREFAREA | Zone privilégiée (oui/non) |
| FURNISHINGSTATUS | État ameublement (meublé/semi/non) |

---

## Comparaison des modèles

| Modèle | RMSE | MAE | R² |
|---|---|---|---|
| **XGBoost** | 27 517 | 12 757 | **0.9151** |
| Random Forest | 32 498 | 19 567 | 0.8816 |
| Gradient Boosting | 43 127 | 31 792 | 0.7914 |
| Linear Regression | 53 985 | 40 253 | 0.6732 |

> Note : ce problème est une régression (prédiction d'une valeur continue). 
> Les métriques utilisées sont RMSE, MAE et R² — adaptées à la régression, 
> contrairement à Accuracy/Precision/Recall qui s'appliquent à la classification.

---

## Optimisation par hyperparamètres

RandomizedSearchCV appliqué sur Random Forest (20 itérations, cv=3).

**Meilleurs hyperparamètres trouvés :**

| Hyperparamètre | Valeur |
|---|---|
| n_estimators | 200 |
| min_samples_split | 2 |
| min_samples_leaf | 1 |
| max_features | log2 |
| max_depth | None |

**Résultats du modèle optimisé :**

| Métrique | Valeur |
|---|---|
| RMSE | 28 139 |
| MAE | 18 226 |
| R² | **0.9112** |

---

## Meilleur modèle

Le modèle sélectionné est le **Random Forest optimisé** (R² = 0.9112), enregistré 
dans le Snowflake Model Registry sous le nom `HOUSE_PRICE_PREDICTOR V1`.

XGBoost obtient un R² légèrement supérieur (0.9151) sans optimisation, mais le 
Random Forest optimisé offre de meilleures garanties de stabilité et de 
généralisation grâce à la validation croisée.

---

## Stack technique

- Snowflake / Snowpark
- scikit-learn / XGBoost
- snowflake-ml-python
- Streamlit

## Structure du repo

- `INESINESHIDECHE 2026-04-01 12:45:19/` → Notebook Snowflake (pipeline ML complet)
- `streamlit_app/` → Application Streamlit
