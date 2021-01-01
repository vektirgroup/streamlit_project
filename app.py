import streamlit as st
import pandas as pd
import pandas as np
import plotly.express as px
import plotly as plotly
import plotly.graph_objs as go

PROD_CURVE_DATA = 'data/Gas_prod_data.csv'

def get_data():
    return pd.read_csv(PROD_CURVE_DATA)

def create_scatter(df):
    # create plot
    fig = go.Figure(
        data=go.Scatter(
            x=df['Days'],
            y=df['Rate'],
            mode='markers'
        )
    )
    # Updtae plot layout
    fig.update_layout(
        title="Original Data - ",
        xaxis_title="Days",
        yaxis_title="Rate"

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
    fig = create_scatter(df)
    sb = get_sidebar()
    st.markdown("# Production - Curve Decline Analysis")
    st.markdown("""
        ###### Motivation: Build a Machine Learning Algorithm that can accurately predict estimated production rate 30 day out!
    """)

    st.plotly_chart(fig)


