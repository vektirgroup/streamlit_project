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
        title="Original Data",
        xaxis_title="Days",
        yaxis_title="Rate"

)
    return fig

def st_sidebar():
    return st.sidebar.Markdown('## The Vektir Group, LLC ')

if __name__ =='__main__':
    df = get_data()
    fig = create_scatter(df)
    st.markdown("## Production - Curve Decline Analysis")
    st.markdown("#### Original Data")

    st.plotly_chart(fig)


