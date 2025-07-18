# Anime-Rec: MLOps-Driven Anime Recommendation System

## Overview
Anime-Rec is a robust, production-ready Anime Recommendation System built using modern MLOps practices. It leverages collaborative and content-based filtering, deep learning, and cloud-native deployment to deliver personalized anime recommendations. The project is designed for scalability, reproducibility, and maintainability, integrating CI/CD, DVC, and GCP for seamless model training, deployment, and monitoring.

---

## Features
- **Hybrid Recommendation Engine**: Combines user-based and content-based filtering for top-10 anime recommendations.
- **Deep Learning Model**: Custom Keras model for user-anime interaction prediction.
- **MLOps Pipeline**: Automated data ingestion, processing, training, and deployment using DVC, Jenkins, and Docker.
- **Cloud Integration**: Data and model artifacts managed via Google Cloud Storage and deployed on GCP Kubernetes.
- **Web Application**: Flask-based UI for user interaction and recommendations.
- **Experiment Tracking**: Integrated with Comet-ML for experiment management.

---

## Project Structure
```
Anime-Rec/
├── application.py           # Flask web app entry point
├── deployment.yaml          # Kubernetes deployment & service
├── Dockerfile               # Containerization for app & training
├── Jenkinsfile              # CI/CD pipeline for build, test, deploy
├── requirements.txt         # Python dependencies
├── setup.py                 # Python package setup
├── tester.py                # Quick test script for recommendations
├── artifacts/               # DVC-managed data & model artifacts
├── config/                  # YAML configs & path management
├── custom_jenkins/          # Custom Jenkins Dockerfile
├── logs/                    # App & pipeline logs
├── notebook/                # Data exploration & model dev (Jupyter)
├── pipeline/                # Training & prediction pipelines
├── src/                     # Core modules: model, data, logging, exceptions
├── static/                  # CSS for web UI
├── templates/               # HTML for web UI
├── utils/                   # Helper functions & utilities
```

---

## How It Works
### 1. Data Ingestion
- Downloads anime datasets from GCP bucket (see `config/config.yaml`).
- Handles large files efficiently (e.g., only 1M rows for `animelist.csv`).

### 2. Data Processing
- Cleans, encodes, and splits data for training/testing.
- Encodes users/anime for model input.

### 3. Model Training
- Custom Keras model (`BaseModel`) for user-anime recommendations.
- Tracked with Comet-ML for metrics and experiment management.
- Artifacts saved via DVC for reproducibility.

### 4. Hybrid Recommendation
- `hybrid_recommendation(user_id)` combines collaborative and content-based results.
- Returns top-10 anime recommendations for a given user.

### 5. Web Application
- Flask app (`application.py`) with a simple UI (`templates/index.html`, `static/style.css`).
- Enter User ID to get recommendations.

### 6. MLOps & Deployment
- **Docker**: Containerizes app and training pipeline.
- **Jenkins**: Automates build, test, DVC pull, and deployment.
- **Kubernetes**: Deploys scalable app via `deployment.yaml`.
- **DVC**: Manages data/model versioning and cloud sync.

---

## Key Files & Modules
- `application.py`: Flask app, handles user input and displays recommendations.
- `pipeline/prediction_pipeline.py`: Hybrid recommendation logic.
- `pipeline/training_pipeline.py`: Data processing and model training orchestration.
- `src/base_model.py`: Keras model definition.
- `src/model_training.py`: Model training, experiment tracking.
- `src/data_ingestion.py`: GCP data download.
- `src/data_processing.py`: Data cleaning, encoding, splitting.
- `config/config.yaml`: Data and model configuration.
- `requirements.txt`: All dependencies (TensorFlow, scikit-learn, DVC, Flask, etc).
- `Dockerfile`, `Jenkinsfile`, `deployment.yaml`: MLOps and deployment automation.

---

## Setup & Usage
### Prerequisites
- Python 3.8+
- Docker
- DVC
- GCP credentials (for data/model storage)
- Jenkins (for CI/CD)

### Local Development
1. **Clone the repo**
   ```bash
   git clone https://github.com/AbulFaizBangi/Anime-Rec.git
   cd Anime-Rec
   ```
2. **Install dependencies**
   ```bash
   pip install -e .
   ```
3. **Pull data/model artifacts**
   ```bash
   dvc pull
   ```
4. **Run the app**
   ```bash
   python application.py
   ```
5. **Access the UI**
   Open [http://localhost:5000](http://localhost:5000) in your browser.

### Training the Model
```bash
python pipeline/training_pipeline.py
```

### Deployment (GCP/Kubernetes)
- Build Docker image and push to GCR.
- Deploy using `deployment.yaml`.
- Jenkins automates CI/CD pipeline.

---

## Notebooks
- `notebook/anime.ipynb`: Data exploration, EDA, model prototyping.

---

## DVC Artifacts
- `artifacts/raw/`: Raw data from GCP
- `artifacts/processed/`: Cleaned, encoded data
- `artifacts/model/`: Trained model files
- `artifacts/weights/`: Model weights
- `artifacts/model_checkpoint/`: Checkpoints for training

---

## Logging & Monitoring
- Logs stored in `logs/` directory.
- Experiment tracking via Comet-ML.

---

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## License
This project is licensed under the MIT License.

---

## Author
**Abul Faiz Bangi**

---

## Acknowledgements
- [MyAnimeList Datasets](https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database)
- [TensorFlow](https://www.tensorflow.org/)
- [DVC](https://dvc.org/)
- [Comet-ML](https://www.comet.com/)
- [Google Cloud Platform](https://cloud.google.com/)
- [Flask](https://flask.palletsprojects.com/)
