# dashboard.py (updated) - robust CSV loading: local file OR user upload fallback
import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(layout="wide", page_title="User Growth & Engagement")

def try_load_csv(path, parse_dates=None):
    if path and os.path.exists(path):
        try:
            return pd.read_csv(path, parse_dates=parse_dates)
        except Exception as e:
            st.error(f"Failed to read {path}: {e}")
            return None
    return None

orders_path = "sample_orders.csv"
rfm_path = "rfm_customers.csv"

df = try_load_csv(orders_path, parse_dates=["InvoiceDate"])
rfm = try_load_csv(rfm_path)

if df is None or rfm is None:
    st.warning("CSV files not found in the app folder. Please upload them (use the same files you exported from the notebook).")
    uploaded_orders = st.file_uploader("Upload sample_orders.csv", type=["csv"], accept_multiple_files=False)
    uploaded_rfm = st.file_uploader("Upload rfm_customers.csv", type=["csv"], accept_multiple_files=False)
    if uploaded_orders is not None:
        try:
            df = pd.read_csv(uploaded_orders, parse_dates=["InvoiceDate"])
            st.success("Loaded sample_orders.csv from upload.")
        except Exception as e:
            st.error(f"Could not parse uploaded sample_orders.csv: {e}")
    if uploaded_rfm is not None:
        try:
            rfm = pd.read_csv(uploaded_rfm, index_col=0)
            st.success("Loaded rfm_customers.csv from upload.")
        except Exception as e:
            st.error(f"Could not parse uploaded rfm_customers.csv: {e}")

if df is None or rfm is None:
    st.stop()

st.sidebar.header("Filters")
min_date_default = df['InvoiceDate'].min().date()
max_date_default = df['InvoiceDate'].max().date()
min_date, max_date = st.sidebar.date_input("Date range", [min_date_default, max_date_default])

country_options = ["All"]
if 'Country' in df.columns:
    country_options += sorted(df['Country'].dropna().unique().tolist())
country = st.sidebar.selectbox("Country (if available)", options=country_options)

df = df[(df['InvoiceDate'].dt.date >= min_date) & (df['InvoiceDate'].dt.date <= max_date)]
if country != "All":
    df = df[df['Country'] == country]

st.title("📈 User Growth & Engagement Dashboard")
col1, col2 = st.columns([2,1])

with col1:
    st.header("Revenue Trend")
    revenue_m = df.groupby(pd.Grouper(key='InvoiceDate', freq='M'))['TotalAmount'].sum().reset_index()
    fig = px.line(revenue_m, x='InvoiceDate', y='TotalAmount', title="Monthly Revenue")
    st.plotly_chart(fig, use_container_width=True)

    st.header("Retention Cohort")
    st.markdown("Loading Error. Serverside Issue.")
    if os.path.exists("cohort_heatmap.png"):
        st.image("cohort_heatmap.png", caption="Cohort retention heatmap")

with col2:
    st.header("Top RFM Segments")
    if 'RFM_score' not in rfm.columns and {'Recency','Frequency','Monetary'}.issubset(rfm.columns):
        try:
            rfm_temp = rfm.copy()
            rfm_temp['R_score'] = pd.qcut(rfm_temp['Recency'], 5, labels=[5,4,3,2,1])
            rfm_temp['F_score'] = pd.qcut(rfm_temp['Frequency'].rank(method='first'), 5, labels=[1,2,3,4,5])
            rfm_temp['M_score'] = pd.qcut(rfm_temp['Monetary'], 5, labels=[1,2,3,4,5])
            rfm_temp['RFM_score'] = rfm_temp['R_score'].astype(str) + rfm_temp['F_score'].astype(str) + rfm_temp['M_score'].astype(str)
            top_segments = rfm_temp['RFM_score'].value_counts().head(8).reset_index()
            top_segments.columns = ['RFM','count']
        except Exception:
            top_segments = pd.DataFrame({'RFM':[], 'count':[]})
    else:
        top_segments = rfm['RFM_score'].value_counts().head(8).reset_index()
        top_segments.columns = ['RFM','count']

    if not top_segments.empty:
        fig2 = px.pie(top_segments, names='RFM', values='count', title="Top RFM segments")
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.info("RFM segments not available in the uploaded RFM file.")

    st.header("Clusters")
    if 'cluster' in rfm.columns:
        clusters = rfm['cluster'].value_counts().reset_index()
        clusters.columns = ['cluster','count']
        fig3 = px.bar(clusters, x='cluster', y='count', title='Cluster sizes')
        st.plotly_chart(fig3, use_container_width=True)
    else:
        st.info("Cluster column not found in RFM file. Please include 'cluster' in rfm_customers.csv if available.")

st.markdown("---")
st.write("Data snapshot and export:")
st.dataframe(df.sample(min(200, len(df))).reset_index(drop=True))

st.download_button("Download filtered orders CSV", df.to_csv(index=False), file_name="filtered_orders.csv")

if st.button("Download RFM CSV (original)"):
    st.download_button("Download RFM", rfm.to_csv(index=True), file_name="rfm_customers.csv")
