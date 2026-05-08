# Deployment Guide

## Streamlit Cloud

1. Create a GitHub repository.
2. Upload this project.
3. Go to https://streamlit.io/cloud
4. Connect your GitHub account.
5. Select the repository.
6. Main file path:

```text
dashboards/streamlit/app.py
```

7. Deploy.

---

## Render Deployment

1. Create a new Web Service in Render.
2. Connect your GitHub repository.
3. Runtime: Python
4. Build Command:

```bash
pip install -r requirements.txt
```

5. Start Command:

```bash
streamlit run dashboards/streamlit/app.py --server.port=$PORT --server.address=0.0.0.0
```

---

## Docker

Build image:

```bash
docker build -t ecommerce-analytics-platform .
```

Run container:

```bash
docker run -p 8501:8501 ecommerce-analytics-platform
```
