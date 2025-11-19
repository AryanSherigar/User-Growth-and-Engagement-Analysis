# 📈 User Growth & Engagement Analysis with Campaign Optimization

## 🔍 Project Overview
This project performs a full end-to-end analysis of user acquisition, retention, and engagement for an e-commerce platform.  
Using a year-long transactional dataset, it uncovers customer segments, identifies growth bottlenecks, and simulates A/B experiments to optimize marketing campaigns.  
The project also includes an interactive dashboard (Streamlit) and exportable insights for stakeholders.

## 🎯 Business Objective & Why It Matters
E-commerce platforms grow sustainably only when user acquisition is paired with strong retention and high customer lifetime value (LTV).  
This project focuses on answering:

- Which users drive the most revenue?
- Which segments are at risk of churn?
- Which marketing campaigns should be run or optimized?
- Where should marketing spend be allocated for maximum ROI?

These insights directly support:
- Lower CAC  
- Improved activation  
- Higher repeat purchases  
- More efficient marketing campaign strategy

## 📦 Dataset Description
**Source:** Kaggle E-Commerce Data  
**Type:** Transaction-level retail data (1 year)

Includes:
- InvoiceNo, CustomerID  
- Product StockCode & Description  
- Quantity, UnitPrice  
- Timestamped InvoiceDate  
- Country  
- Derived fields: TotalAmount, InvoiceYearMonth, CohortMonth, RFM scores, clusters  

# 🧠 Methodology

## 🧹 1. Data Cleaning
Steps included:
- Removed duplicates & invalid transactions  
- Converted timestamps & standardized data types  
- Created new features (`TotalAmount`, `InvoiceYearMonth`, `CohortMonth`)  
- Identified and removed returns or zero-value orders  
- Handled missing CustomerIDs  

Tools used: Python (pandas, numpy)

## 📊 2. Exploratory Data Analysis (EDA)
Performed:
- Revenue & order trend analysis  
- Cohort retention heatmaps  
- Country-level purchase patterns  
- Product-level revenue contribution  
- Time-series seasonality  

## 🎯 3. RFM Segmentation
Computed Recency, Frequency, Monetary metrics for each customer.

Deliverables:
- 5×5×5 RFM score grid  
- Top RFM segments  
- High-value, high-frequency, and churn-risk segments  

## 👥 4. Clustering
Used KMeans clustering with silhouette optimization to discover behavioral personas.

Clusters included:
- High-Value Loyalists  
- Frequent Bargain Seekers  
- Low-Frequency Explorers  
- Dormant / Churn-Risk Users

## 🧪 5. A/B Testing
Designed and simulated experiments such as:
- Reactivation discounts  
- Personalized push notifications  
- Homepage personalization  
- Recommendation banners  

Included:
- Hypothesis definition  
- Power analysis & sample size calculations  
- Impact measurement (lift, confidence intervals)  
- Guardrail metrics (refund rate, AOV)

# ⭐ Key Insights (3–5 bullet points)

- High-value customers contribute disproportionately to revenue and exhibit strong repeat behavior—ideal for retention campaigns.  
- Churn-risk cohorts show rapid drop-off after Month 2, highlighting the need for early lifecycle nudges.  
- Seasonal spikes in revenue align with holiday months, suggesting increased budget allocation during peak periods.  
- Cluster 0 (top spenders) shows high frequency and monetary value, making them ideal for personalized promotions.  
- A/B simulations indicate engagement campaigns may lift repeat purchases by 8–15% depending on segment.

# 📌 Results & Recommendations

### ✔ Recommendations
- Prioritize high-value segments for loyalty and retention programs.  
- Target dormant but high-potential users with personalized reactivation incentives.  
- Reallocate marketing budget to channels driving high LTV and lower churn rates.  
- Intensify campaigns during peak months identified in seasonal revenue patterns.  
- Use automated lifecycle journeys (Day-7, Day-30) to sustain engagement.

### ✔ Outcomes
- Clear segmentation of customers  
- Identified actionable growth levers  
- Built scalable experimentation framework  
- Delivered dashboards for ongoing monitoring  

# 🖼 Screenshots

### 📈 Monthly Revenue Trend
![Monthly Revenue](dashboard_images/monthly_revenue.png)

### 🔥 Cohort Retention Heatmap
![Cohort Retention](dashboard_images/cohort_retention.png)

### 🎯 RFM Segments
![RFM Pie](dashboard_images/rfm_pie.png)

### 👥 Cluster Distribution  
![Cluster Bar](dashboard_images/cluster_bar.png)

# 🧪 How to Run the Notebook

### 1. Open in Colab
Upload the notebook and dataset then run all cells.

### 2. Local Execution
```bash
pip install -r requirements.txt
jupyter notebook
```

# 🖥 How to Run the Streamlit App

### Local
```bash
pip install -r requirements.txt
streamlit run dashboard.py
```

### If CSVs are missing
The app will prompt you to upload:
- sample_orders.csv  
- rfm_customers.csv

### Streamlit Cloud Deployment
1. Push repo to GitHub  
2. Go to https://streamlit.io/cloud  
3. Create New App → Choose repo  
4. Select dashboard.py  
5. Deploy  
