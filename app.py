import streamlit as st
import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from datetime import datetime
import plotly.express as px
import plotly as plotly
import plotly.graph_objs as go

PROD_CURVE_DATA = 'data/Gas_prod_data.csv'

def create_tsa_predictions(df):
    # ARIMA model
    model = ARIMA(df, order=(5,1,0))
    model_fit = model.fit()
    output = model_fit.forecast()

    return output

def get_data():
    return pd.read_csv(PROD_CURVE_DATA, header=0, parse_dates=True, squeeze=True)

def create_scatter(df):

    # create plot
    fig = go.Figure(
        data=go.Scatter(
            x=df['days'],
            y=df['rate'],
            mode='markers'
        )
    )

    # Update plot layout
    fig.update_layout(
        xaxis_title="Days",
        yaxis_title="Rate (mcf)"

    )
    return fig

def create_arima_scatter(df):

    # create plot
    fig = go.Figure(
        data=go.Scatter(
            x=df.index,
            y=df['rate'],
            mode='markers'
        )
    )

    # Update plot layout
    fig.update_layout(
        xaxis_title="Days",
        yaxis_title="Rate (mcf)"

    )
    return fig

def get_sidebar():
    return st.sidebar.markdown("""
        # The Vektir Group, LLC \n
        - Dev: Tyler Hunt
        - Email: vektirgroup@gmail.com
        - Date: 01/01/2021
        - GitHub: https://bit.ly/3o5cMxa
        """)

if __name__ =='__main__':
    df = get_data()
    o_fig = create_scatter(df)
    sb = get_sidebar()

    st.markdown("""
        # Production - Curve Decline Analysis
        ---
    """)

    #Arima df
    n_df = df[['date', 'rate']]
    n_df.set_index('date', inplace = True)
    y_pred = create_tsa_predictions(n_df)

    # Chart Visuals
    st.plotly_chart(o_fig)

    st.markdown("""
        #### Model Information
        - Test #1 - 30 Days - Statsmodels ARIMA
        -   Prediction (30 Days): """ + str(y_pred) + """
    """)


