import numpy as np
import pandas as pd
import time
import streamlit as st
import plotly.express as px

df = pd.read_csv("https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv")

st.set_page_config(
    page_title = 'Real-Time Data Science Dashboard',
    page_icon = '&',
    layout = 'wide'
)
st.title("Real-Time / Live Data Science Dashboard")

job_filter = st.selectbox("Select the Job", pd.unique(df['job']))

placeholder = st.empty()

df = df[df['job']==job_filter]

for seconds in range(200):

    df['age_new'] = df['age'] * np.random.choice(range(1,5))
    df['balance_new'] = df['balance'] * np.random.choice(range(1,5))
    avg_age = np.mean(df['age_new'])
    count_married = int(df[(df["marital"]=='married')]['marital'].count() + np.random.choice(range(1,30)))

    balance = np.mean(df['balance_new'])
    with placeholder.container():
        kpi1, kpi2, kpi3 =st.columns(3)
        kpi1.metric(label="Age", value=round(avg_age), delta= round(avg_age) - 10)
        kpi2.metric(label="Married Count", value= int(count_married), delta= - 10 + count_married)
        kpi3.metric(label="A/C Balance $", value= f"$ {round(balance,2)} ", delta= -round(balance/count_married) * 10)

        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            st.markdown('### First Charts')
            fig = px.density_heatmap(data_frame=df, y = 'age_new', x ='marital')
            st.write(fig)
        with fig_col2:
            st.markdown("### Second Charts")
            fig2 = px.histogram(data_frame = df, x = 'age_new')
            st.write(fig2)
        st.markdown("### Detailed View")
        st.dataframe(df)
        time.sleep(0.5)
