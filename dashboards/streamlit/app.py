
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(
    page_title="Executive E-commerce BI Dashboard",
    page_icon="📊",
    layout="wide"
)

@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/ecommerce_dashboard_dataset.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df

df = load_data()

st.title("📊 Executive E-commerce BI Dashboard")
st.caption("Interactive business intelligence dashboard for revenue, marketing performance, conversion and profitability analysis.")

# Sidebar filters
st.sidebar.header("Dashboard Filters")

date_min = df["date"].min().date()
date_max = df["date"].max().date()
date_range = st.sidebar.date_input(
    "Date range",
    value=(date_min, date_max),
    min_value=date_min,
    max_value=date_max
)

channels = st.sidebar.multiselect(
    "Channel",
    sorted(df["channel"].unique()),
    default=sorted(df["channel"].unique())
)

regions = st.sidebar.multiselect(
    "Region",
    sorted(df["region"].unique()),
    default=sorted(df["region"].unique())
)

categories = st.sidebar.multiselect(
    "Category",
    sorted(df["category"].unique()),
    default=sorted(df["category"].unique())
)

devices = st.sidebar.multiselect(
    "Device",
    sorted(df["device"].unique()),
    default=sorted(df["device"].unique())
)

filtered = df.copy()

if len(date_range) == 2:
    start_date, end_date = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
    filtered = filtered[(filtered["date"] >= start_date) & (filtered["date"] <= end_date)]

filtered = filtered[
    filtered["channel"].isin(channels)
    & filtered["region"].isin(regions)
    & filtered["category"].isin(categories)
    & filtered["device"].isin(devices)
]

if filtered.empty:
    st.warning("No data available for the selected filters.")
    st.stop()

# KPIs
revenue = filtered["revenue_usd"].sum()
orders = filtered["orders"].sum()
sessions = filtered["sessions"].sum()
spend = filtered["marketing_spend_usd"].sum()
profit = filtered["profit_usd"].sum()

conversion = orders / sessions if sessions else 0
aov = revenue / orders if orders else 0
cac = spend / orders if orders else 0
roas = revenue / spend if spend else np.nan
margin = profit / revenue if revenue else 0

kpi1, kpi2, kpi3, kpi4, kpi5, kpi6 = st.columns(6)
kpi1.metric("Revenue", f"${revenue:,.0f}")
kpi2.metric("Orders", f"{orders:,.0f}")
kpi3.metric("Conversion", f"{conversion:.2%}")
kpi4.metric("AOV", f"${aov:,.2f}")
kpi5.metric("CAC", f"${cac:,.2f}")
kpi6.metric("ROAS", "N/A" if np.isnan(roas) else f"{roas:.2f}x")

st.divider()

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "Executive Overview",
    "Marketing Performance",
    "Commercial Segments",
    "Data Table"
])

with tab1:
    monthly = filtered.groupby("month", as_index=False).agg(
        revenue_usd=("revenue_usd","sum"),
        orders=("orders","sum"),
        sessions=("sessions","sum"),
        marketing_spend_usd=("marketing_spend_usd","sum"),
        profit_usd=("profit_usd","sum")
    )
    monthly["conversion_rate"] = monthly["orders"] / monthly["sessions"]
    monthly["cac_usd"] = monthly["marketing_spend_usd"] / monthly["orders"]
    monthly["roas"] = monthly["revenue_usd"] / monthly["marketing_spend_usd"].replace(0, np.nan)

    c1, c2 = st.columns(2)
    with c1:
        fig = px.line(monthly, x="month", y="revenue_usd", markers=True, title="Revenue Trend")
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        fig = px.bar(monthly, x="month", y="orders", title="Monthly Orders")
        st.plotly_chart(fig, use_container_width=True)

    c3, c4 = st.columns(2)
    with c3:
        fig = px.line(monthly, x="month", y="conversion_rate", markers=True, title="Conversion Rate")
        fig.update_yaxes(tickformat=".2%")
        st.plotly_chart(fig, use_container_width=True)
    with c4:
        fig = px.line(monthly, x="month", y="cac_usd", markers=True, title="Customer Acquisition Cost")
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    channel = filtered.groupby("channel", as_index=False).agg(
        revenue_usd=("revenue_usd","sum"),
        orders=("orders","sum"),
        sessions=("sessions","sum"),
        marketing_spend_usd=("marketing_spend_usd","sum"),
        profit_usd=("profit_usd","sum")
    )
    channel["conversion_rate"] = channel["orders"] / channel["sessions"]
    channel["cac_usd"] = channel["marketing_spend_usd"] / channel["orders"]
    channel["roas"] = channel["revenue_usd"] / channel["marketing_spend_usd"].replace(0, np.nan)

    c1, c2 = st.columns(2)
    with c1:
        fig = px.bar(channel.sort_values("revenue_usd", ascending=False), x="channel", y="revenue_usd", title="Revenue by Channel")
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        fig = px.scatter(channel, x="cac_usd", y="roas", size="revenue_usd", hover_name="channel", title="CAC vs ROAS by Channel")
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Channel KPI Table")
    st.dataframe(
        channel.sort_values("revenue_usd", ascending=False),
        use_container_width=True
    )

with tab3:
    c1, c2 = st.columns(2)

    category = filtered.groupby("category", as_index=False).agg(
        revenue_usd=("revenue_usd","sum"),
        orders=("orders","sum"),
        profit_usd=("profit_usd","sum")
    )
    category["gross_margin_pct"] = category["profit_usd"] / category["revenue_usd"]

    region = filtered.groupby("region", as_index=False).agg(
        revenue_usd=("revenue_usd","sum"),
        orders=("orders","sum")
    )

    with c1:
        fig = px.treemap(category, path=["category"], values="revenue_usd", color="gross_margin_pct", title="Revenue & Margin by Category")
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        fig = px.bar(region.sort_values("revenue_usd", ascending=False), x="region", y="revenue_usd", title="Revenue by Region")
        st.plotly_chart(fig, use_container_width=True)

    device = filtered.groupby("device", as_index=False).agg(
        revenue_usd=("revenue_usd","sum"),
        orders=("orders","sum"),
        sessions=("sessions","sum")
    )
    device["conversion_rate"] = device["orders"] / device["sessions"]

    fig = px.bar(device, x="device", y="conversion_rate", title="Conversion Rate by Device")
    fig.update_yaxes(tickformat=".2%")
    st.plotly_chart(fig, use_container_width=True)

with tab4:
    st.subheader("Filtered Dataset")
    st.dataframe(filtered, use_container_width=True)

    csv = filtered.to_csv(index=False).encode("utf-8")
    st.download_button(
        "Download filtered data as CSV",
        csv,
        "filtered_ecommerce_dashboard_data.csv",
        "text/csv"
    )
