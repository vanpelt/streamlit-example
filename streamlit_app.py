import altair as alt
import wandb
import pandas as pd
import streamlit as st

"""
# W&B Streamlit Demo
"""


with st.echo(code_location="below"):
    query_params = st.experimental_get_query_params()
    path = query_params.get("path", "wandb/dogs/3a1k7v1o")

    st.markdown("# Path\n`{}`".format(path))
    # TODO: waiting for a way to get secrets
    # api = wandb.Api()
    # run = api.run(path)
    # st.dataframe(run.history())
