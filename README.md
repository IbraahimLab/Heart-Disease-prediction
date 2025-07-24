# Heart Disease Prediction Project

## 🌟 Solving the Challenge of Early Heart Disease Detection

Heart disease is a major health concern worldwide. This project tackles this challenge by providing an easy-to-use tool that helps predict the risk of heart disease. By using a machine learning model, this application can give early insights based on a patient's health information, helping both medical professionals and individuals understand potential risks better.

## ✨ Features

  * **User-Friendly Interface**: A simple web application (built with Streamlit) where you can easily enter patient details.
  * **Smart Prediction Model**: Uses a powerful machine learning model (Random Forest) to predict heart disease risk.
  * **API for Integration**: A web API (built with FastAPI) that allows other applications to send patient data and get predictions.

## 🛠️ How It Works (A Peek Under the Hood)

This project is made up of a few key parts that work together:

### 📊 The Data (`heart.csv`)

[cite\_start]The project uses a dataset called `heart.csv` [cite: 5] to learn about heart disease. This file contains various health details about patients, such as:

  * [cite\_start]**Age**: How old the patient is. [cite: 3]
  * [cite\_start]**Sex**: Whether the patient is male (1) or female (0). [cite: 3]
  * [cite\_start]**Chest Pain Type (cp)**: Different kinds of chest pain. [cite: 3]
  * [cite\_start]**Resting Blood Pressure (trestbps)**: Blood pressure when resting. [cite: 3]
  * [cite\_start]**Serum Cholesterol (chol)**: Cholesterol levels in the blood. [cite: 3]
  * [cite\_start]**Fasting Blood Sugar (fbs)**: Blood sugar levels after not eating. [cite: 3]
  * [cite\_start]**Resting ECG (restecg)**: Results from an electrocardiogram. [cite: 3]
  * [cite\_start]**Max Heart Rate Achieved (thalach)**: The highest heart rate reached during exercise. [cite: 3]
  * [cite\_start]**Exercise-Induced Angina (exang)**: Whether chest pain occurs during exercise. [cite: 3]
  * [cite\_start]**ST Depression (oldpeak)**: A measure related to heart strain during exercise. [cite: 3]
  * [cite\_start]**Slope**: The slope of the ST segment during peak exercise. [cite: 3]
  * [cite\_start]**Number of Major Vessels (ca)**: How many major blood vessels are visible. [cite: 3]
  * [cite\_start]**Thalassemia (thal)**: A blood disorder. [cite: 3]
  * [cite\_start]**Target**: This is the main thing we want to predict: 0 means no heart disease, 1 means heart disease. [cite: 3]

### 🧠 Training the Brain (`heart-disease-prediction-model.ipynb`)

[cite\_start]In the `heart-disease-prediction-model.ipynb` file[cite: 3], the machine learning model is trained. Here's what happens:

1.  [cite\_start]**Data Loading**: The `heart.csv` data is loaded. [cite: 3]
2.  **Preparation**: The data is prepared for the model (this usually involves cleaning and organizing it).
3.  **Model Selection**: A Random Forest Classifier is chosen as the prediction model.
4.  **Training**: The model "learns" from the data to find patterns that indicate heart disease.
5.  **Saving the Model**: Once trained, the model is saved as `random_forest_model.pkl` so it can be used later without retraining.

### 🌐 The API (`api.py`)

[cite\_start]The `api.py` file [cite: 1] sets up a "backend" service using FastAPI. This service acts like a middleman:

  * [cite\_start]It loads the trained machine learning model (`random_forest_model.pkl`). [cite: 1]
  * [cite\_start]It has a special address (`/predict`) where the web application (or any other program) can send patient data. [cite: 1]
  * [cite\_start]When it receives data, it feeds it to the loaded model, gets a prediction (0 or 1), and sends it back. [cite: 1]

### 🖥️ The User Interface (`app.py`)

[cite\_start]The `app.py` file [cite: 2] creates the easy-to-use web interface using Streamlit:

  * [cite\_start]It's designed to be simple and clear, titled "💓 Heart Disease Prediction App". [cite: 2]
  * [cite\_start]You can enter all the patient's details like age, sex, chest pain type, and more using simple input fields and dropdowns. [cite: 2]
  * [cite\_start]When you click "Predict", this app sends your entered data to the API (`api.py`). [cite: 2]
  * It then receives the prediction from the API and shows you the result right on the screen.

## 🚀 Getting Started

To run this project, you'll need to set up your computer with the right tools.

### Prerequisites

You'll need Python installed. The specific libraries required are listed in `requirements.txt`.
[cite\_start]*Note*: The provided `requirements.txt` file is currently empty[cite: 4]. Based on the other files, you will likely need to include:

  * `pandas`
  * `numpy`
  * `scikit-learn`
  * `fastapi`
  * `uvicorn`
  * `streamlit`
  * `joblib` (for loading the model)
  * `matplotlib` (for visualizations in notebook)
  * `seaborn` (for visualizations in notebook)
  * `ipykernel` (for Jupyter notebook)

### Installation

1.  **Clone the repository** (if applicable, or download the files).
2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### How to Run

1.  **Run the FastAPI backend**:
    Open your terminal or command prompt, go to the project folder, and run:

    ```bash
    uvicorn api:app --reload
    ```

    This will start the API, usually at `http://127.0.0.1:8000`.

2.  **Run the Streamlit frontend**:
    Open another terminal or command prompt, go to the project folder, and run:

    ```bash
    streamlit run app.py
    ```

    This will open the web application in your browser.

## 🤝 Usage

1.  **Launch the Streamlit App**: Once `streamlit run app.py` is executed, your web browser will automatically open to the Heart Disease Prediction App.
2.  **Enter Patient Details**: Fill in the fields on the left sidebar with the relevant patient information. [cite\_start]There are helpful explanations for each feature if you need them. [cite: 2]
3.  **Get Prediction**: Click the "Predict" button. The application will send the data to the API, get the prediction, and display whether heart disease is predicted or not.

## 📂 Project Structure

  * [cite\_start]`heart.csv`: The dataset used for training the model. [cite: 5]
  * [cite\_start]`heart-disease-prediction-model.ipynb`: The Jupyter Notebook where the machine learning model is developed and trained. [cite: 3]
  * `random_forest_model.pkl`: The saved machine learning model ready for predictions.
  * [cite\_start]`api.py`: The FastAPI application that provides the prediction service. [cite: 1]
  * [cite\_start]`app.py`: The Streamlit web application, which is the user interface. [cite: 2]
  * [cite\_start]`requirements.txt`: Lists all the necessary Python libraries for the project. [cite: 4]
  * `README.md`: This file, explaining the project.
