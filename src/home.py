import streamlit as st
import textwrap
from dotenv import load_dotenv
from streamlit.components.v1 import html
from langchain_openai import ChatOpenAI

from containers import sidebar

# from cnt import render_sidebar

# from process_images import DetectTable

from prompts import (
    queryTemplate1,
    queryTemplate2,
    queryTemplate3,
    summarizeChain,
)


def get_response(response: str) -> str:
    return "\n".join(textwrap.wrap(response, width=100))


def get_llm(value: str):
    llm = None
    if value == "default":
        llm = ChatOpenAI(temperature=0)
    elif value == "gpt-4-turbo-preview":
        llm = ChatOpenAI(model="gpt-4-turbo-preview", temperature=0)
    return llm


def handle_select_llm():
    value = st.session_state["llm_model_name"]
    st.session_state["llm"] = get_llm(value)


def render_page(auth):
    load_dotenv()
    queries = [queryTemplate1(), queryTemplate2(), queryTemplate3()]
    results = None
    # st.session_state.detect_table = DetectTable.instance()

    # st.set_page_config(
    #     page_title="Chat with multiple PDFs", page_icon=":books:", layout="wide"
    # )

    if "chain" not in st.session_state:
        st.session_state.chain = None

    st.header("Chat with multiple PDFs :books:")
    # if st.session_state["authentication_status"]:
    with st.sidebar:
        auth.logout()
        selected_llm_value = st.selectbox(
            key="llm_model_name",
            label="Select llm",
            options=[
                "default",
                "gpt-4-turbo-preview",
            ],
            index=0,
            on_change=handle_select_llm,
        )

        st.session_state["llm"] = get_llm(selected_llm_value)

        sidebar.render_sidebar(
            st=st,
            queries=queries,
        )
    if hasattr(st.session_state, "ticker") and hasattr(st.session_state, "results"):
        ticker = st.session_state["ticker"]
        results = st.session_state["results"]

        
        if len(results) == 3:
            st.subheader(f"Financial summary for {ticker}")
            col = st.columns((3, 3, 3), gap="medium")
            with col[0]:
                st.markdown("#### Investment Thesis")
                if results[0]:
                    st.markdown(results[0])
            with col[1]:
                st.markdown("#### Risk analysis")
                if results[1]:
                    st.markdown(results[1])
            with col[2]:
                st.markdown("#### Balance Sheet analysis")

                if results[2]:
                    st.markdown(results[2])

            # display_images()
