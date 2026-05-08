"""
Executive Ecommerce Analytics Dashboard

Run:
    streamlit run dashboards/streamlit/app.py
"""

from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data/processed"

st.set_page_config(page_title="Real-Time Ecommerce Analytics Platform", page_icon="📊", layout="wide")

st.markdown("""
<style>
.stApp { background: linear-gradient(180deg, #0b1020 0%, #111827 55%, #0f172a 100%); color: #e5e7eb; }
[data-testid="stSidebar"] { background-color: #111827; }
h1, h2, h3 { color: #f8fafc; }
.block-container { padding-top: 2rem; }
[data-testid="stMetric"] { background-color: #172033; border: 1px solid #263244; padding: 18px; border-radius: 16px; }
[data-testid="stMetricLabel"] { color: #cbd5e1; }
[data-testid="stMetricValue"] { color: #f8fafc; }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    events = pd.read_csv(DATA_DIR / "analytics_events.csv")
    events["event_timestamp"] = pd.to_datetime(events["event_timestamp"])
    events["event_date"] = pd.to_datetime(events["event_date"])
    events["order_id"] = events["order_id"].fillna("")
    return events

events = load_data()

st.markdown("# Real-Time Ecommerce Analytics Platform")
st.markdown("#### Executive analytics dashboard for revenue, customer behavior, conversion and operational data monitoring.")

st.sidebar.title("Dashboard Filters")

min_date = events["event_date"].min().date()
max_date = events["event_date"].max().date()

date_range = st.sidebar.date_input("Date range", value=(min_date, max_date), min_value=min_date, max_value=max_date)
countries = st.sidebar.multiselect("Country", sorted(events["country"].dropna().unique()), default=sorted(events["country"].dropna().unique()))
devices = st.sidebar.multiselect("Device", sorted(events["device_type"].dropna().unique()), default=sorted(events["device_type"].dropna().unique()))
categories = st.sidebar.multiselect("Category", sorted(events["category"].dropna().unique()), default=sorted(events["category"].dropna().unique()))
sources = st.sidebar.multiselect("Traffic Source", sorted(events["traffic_source"].dropna().unique()), default=sorted(events["traffic_source"].dropna().unique()))

if isinstance(date_range, tuple) and len(date_range) == 2:
    start_date, end_date = date_range
else:
    start_date, end_date = min_date, max_date

filtered = events[
    (events["event_date"].dt.date >= start_date) &
    (events["event_date"].dt.date <= end_date) &
    (events["country"].isin(countries)) &
    (events["device_type"].isin(devices)) &
    (events["category"].isin(categories)) &
    (events["traffic_source"].isin(sources))
].copy()

total_revenue = filtered["revenue"].sum()
orders = filtered.loc[filtered["event_type"] == "purchase", "order_id"].replace("", pd.NA).dropna().nunique()
active_users = filtered["user_id"].nunique()
sessions = filtered["session_id"].nunique()
events_count = filtered["event_id"].nunique()
aov = total_revenue / orders if orders else 0
conversion_rate = orders / active_users if active_users else 0
cart_users = filtered.loc[filtered["event_type"] == "add_to_cart", "user_id"].nunique()
purchase_users = filtered.loc[filtered["event_type"] == "purchase", "user_id"].nunique()
cart_abandonment = 1 - (purchase_users / cart_users) if cart_users else 0

st.markdown("## Executive Overview")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Revenue", f"${total_revenue:,.0f}")
c2.metric("Orders", f"{orders:,}")
c3.metric("Conversion Rate", f"{conversion_rate:.2%}")
c4.metric("Average Order Value", f"${aov:,.2f}")

c5, c6, c7, c8 = st.columns(4)
c5.metric("Active Users", f"{active_users:,}")
c6.metric("Sessions", f"{sessions:,}")
c7.metric("Events", f"{events_count:,}")
c8.metric("Cart Abandonment", f"{cart_abandonment:.2%}")

st.markdown("---")

daily = filtered.groupby("event_date").agg(
    revenue=("revenue", "sum"),
    orders=("order_id", lambda x: (x.replace("", pd.NA).dropna()).nunique()),
    active_users=("user_id", "nunique"),
    sessions=("session_id", "nunique")
).reset_index()

left, right = st.columns(2)
with left:
    st.subheader("Revenue Trend")
    fig = px.line(daily, x="event_date", y="revenue", markers=True, template="plotly_dark")
    fig.update_layout(paper_bgcolor="#111827", plot_bgcolor="#111827")
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.subheader("Active Users Trend")
    fig = px.area(daily, x="event_date", y="active_users", template="plotly_dark")
    fig.update_layout(paper_bgcolor="#111827", plot_bgcolor="#111827")
    st.plotly_chart(fig, use_container_width=True)

left, right = st.columns(2)
with left:
    st.subheader("Revenue by Category")
    cat = filtered.groupby("category").agg(revenue=("revenue", "sum")).reset_index().sort_values("revenue", ascending=False)
    fig = px.bar(cat, x="category", y="revenue", text_auto=".2s", template="plotly_dark")
    fig.update_layout(paper_bgcolor="#111827", plot_bgcolor="#111827")
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.subheader("Traffic Source Performance")
    src = filtered.groupby("traffic_source").agg(revenue=("revenue", "sum"), users=("user_id", "nunique")).reset_index()
    fig = px.treemap(src, path=["traffic_source"], values="revenue", color="users", template="plotly_dark")
    fig.update_layout(paper_bgcolor="#111827")
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Conversion Funnel")
funnel = filtered.groupby("event_type").agg(users=("user_id", "nunique")).reset_index()
order = {"page_view": 1, "search": 2, "add_to_cart": 3, "checkout": 4, "purchase": 5}
funnel["step"] = funnel["event_type"].map(order)
funnel = funnel.sort_values("step")
fig = px.funnel(funnel, x="users", y="event_type", template="plotly_dark")
fig.update_layout(paper_bgcolor="#111827", plot_bgcolor="#111827")
st.plotly_chart(fig, use_container_width=True)

left, right = st.columns(2)
with left:
    st.subheader("Device Revenue Distribution")
    dev = filtered.groupby("device_type").agg(revenue=("revenue", "sum")).reset_index()
    fig = px.pie(dev, names="device_type", values="revenue", hole=0.45, template="plotly_dark")
    fig.update_layout(paper_bgcolor="#111827")
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.subheader("Customer Segmentation")
    cust = filtered.groupby("user_id").agg(revenue=("revenue", "sum")).reset_index()
    cust["segment"] = pd.cut(cust["revenue"], bins=[-1, 0, 50, 200, 100000], labels=["No purchase", "Low value", "Medium value", "High value"])
    seg = cust.groupby("segment", observed=True).agg(customers=("user_id", "count")).reset_index()
    fig = px.bar(seg, x="segment", y="customers", text_auto=True, template="plotly_dark")
    fig.update_layout(paper_bgcolor="#111827", plot_bgcolor="#111827")
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.markdown("## Data Engineering Layer")
x1, x2, x3 = st.columns(3)
x1.info("Raw ecommerce events are transformed into analytics-ready datasets.")
x2.info("Architecture inspired by Pub/Sub → Dataflow → BigQuery.")
x3.info("Bigtable represents a low-latency operational analytics layer.")

with st.expander("Preview processed events"):
    st.dataframe(filtered.head(100), use_container_width=True)

st.caption("Portfolio project by Micaela Feriale · Data Analytics & Data Engineering")
