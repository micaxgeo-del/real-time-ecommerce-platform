from pathlib import Path
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

BASE_DIR = Path(__file__).resolve().parents[2]

RAW_DIR = BASE_DIR / "data/raw"
PROCESSED_DIR = BASE_DIR / "data/processed"

RAW_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

np.random.seed(42)
random.seed(42)

n_events = 25000

start_date = datetime(2026, 1, 1)
end_date = datetime(2026, 4, 30)

days_range = (end_date - start_date).days

users = [f"user_{i:05d}" for i in range(1, 2501)]
products = [f"product_{i:04d}" for i in range(1, 401)]

categories = [
    "Electronics",
    "Home",
    "Fashion",
    "Beauty",
    "Sports",
    "Books",
    "Toys",
    "Grocery"
]

countries = [
    "Argentina",
    "Brazil",
    "Chile",
    "Mexico",
    "Colombia",
    "Uruguay"
]

devices = [
    "mobile",
    "desktop",
    "tablet"
]

event_types = [
    "page_view",
    "search",
    "add_to_cart",
    "checkout",
    "purchase"
]

product_catalog = pd.DataFrame({
    "product_id": products,
    "category": np.random.choice(categories, len(products)),
    "base_price": np.round(np.random.uniform(8, 350, len(products)), 2)
})

events = []

order_counter = 1

for i in range(n_events):

    event_time = start_date + timedelta(
        days=int(np.random.randint(0, days_range)),
        hours=int(np.random.randint(0, 24)),
        minutes=int(np.random.randint(0, 60)),
        seconds=int(np.random.randint(0, 60))
    )

    user_id = random.choice(users)

    product = product_catalog.sample(1).iloc[0]

    event_type = np.random.choice(
        event_types,
        p=[0.46, 0.20, 0.18, 0.08, 0.08]
    )

    quantity = int(np.random.choice([1, 1, 1, 2, 3]))

    revenue = 0.0
    order_id = ""

    if event_type == "purchase":
        revenue = round(
            float(product["base_price"]) *
            quantity *
            np.random.uniform(0.85, 1.15),
            2
        )

        order_id = f"order_{order_counter:06d}"
        order_counter += 1

    events.append({
        "event_id": f"evt_{i+1:08d}",
        "event_timestamp": event_time.isoformat(),
        "event_date": event_time.date().isoformat(),
        "user_id": user_id,
        "session_id": f"{user_id}_sess_{np.random.randint(1, 600):04d}",
        "event_type": event_type,
        "product_id": product["product_id"],
        "category": product["category"],
        "quantity": quantity,
        "revenue": revenue,
        "order_id": order_id,
        "country": np.random.choice(countries),
        "device_type": np.random.choice(
            devices,
            p=[0.62, 0.30, 0.08]
        ),
        "traffic_source": np.random.choice(
            ["organic", "paid_search", "social", "email", "direct"],
            p=[0.32, 0.25, 0.18, 0.12, 0.13]
        )
    })

events_df = pd.DataFrame(events)

events_df.to_csv(
    RAW_DIR / "ecommerce_events_raw.csv",
    index=False
)

daily = events_df.groupby("event_date").agg(
    revenue=("revenue", "sum"),
    orders=("order_id", lambda x: (x != "").sum()),
    active_users=("user_id", "nunique"),
    sessions=("session_id", "nunique")
).reset_index()

category = events_df.groupby("category").agg(
    revenue=("revenue", "sum"),
    orders=("order_id", lambda x: (x != "").sum())
).reset_index()

funnel = events_df.groupby("event_type").agg(
    users=("user_id", "nunique")
).reset_index()

events_df.to_csv(
    PROCESSED_DIR / "analytics_events.csv",
    index=False
)

daily.to_csv(
    PROCESSED_DIR / "daily_kpis.csv",
    index=False
)

category.to_csv(
    PROCESSED_DIR / "category_kpis.csv",
    index=False
)

funnel.to_csv(
    PROCESSED_DIR / "funnel_metrics.csv",
    index=False
)

print("ETL pipeline completed successfully.")