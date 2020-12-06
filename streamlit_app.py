import altair as alt
import wandb
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


with st.echo(code_location='below'):
    query_params = st.experimental_get_query_params()
    path = query_params.get("path", "wandb/dogs/3a1k7v1o")

    api = wandb.Api()
    run = api.run(path)
    st.dataframe(run.history())
