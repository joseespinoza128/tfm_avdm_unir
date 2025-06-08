# TFM
Trabajo de fin de master - Máster Universitario en Análisis y Visualización de Datos Masivos/ Visual Analytics and Big Data 

# Predicciones de gastos operativos
Este proyecto tiene como objetivo desarrollar un prototipo funcional para predecir **gastos operativos** utilizando técnicas de **aprendizaje automático**. Se trata de un trabajo aplicado sobre datos contables provenientes de un sistema ERP, con el fin de asistir en la toma de decisiones financieras.

## Objetivos

- Analizar los datos contables históricos mediante técnicas de análisis exploratorio (EDA).
- Entrenar y comparar varios modelos de regresión para predecir el valor de gasto operativo.
- Implementar una API REST con FastAPI que reciba nuevos datos y devuelva predicciones en tiempo real.
- Evaluar el desempeño de los modelos usando métricas como MAE, RMSE y R².

## Modelos utilizados

- Regresión lineal
- Árboles de decisión
- Random Forest
- XGBoost
- Redes neuronales

## Contenido del proyecto

- `proyecto.ipynb`: Análisis exploratorio de datos, ingeniería de características y entrenamiento de modelos.
- `modelo_random_forest_pipeline.joblib`: Modelo de Random Forest entrenado y serializado con pipeline.
- `modelo_xgboost_pipeline.joblib`: Modelo de XGBoost entrenado y serializado con pipeline.
- `main.py`: Código de la API en FastAPI que expone un endpoint `/predecir/` para obtener predicciones.

## Tecnologías y herramientas

- Python 3.10
- Jupyter Notebook
- Pandas, NumPy, Matplotlib, Seaborn
- Scikit-learn
- XGBoost
- Tensorflow
- Keras
- FastAPI
- Joblib

## Licencia

Este proyecto se presenta como parte de un Trabajo Fin de Máster con fines académicos.