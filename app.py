import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import pygwalker as pyg
from pygwalker.api.streamlit import init_streamlit_comm, get_streamlit_html



st.set_page_config(
    page_title="Breast Cancer Dashboard",
    layout="wide"
)

file_id = '1b2Ztm96gkVadOftMmlUXowbQtzGL8Vqp'

download_link = f'https://drive.google.com/uc?id={file_id}'

data = pd.read_csv(download_link)



def about():
    st.title("Breast Cancer Data EDA")

    st.write("The Wisconsin Breast Cancer Dataset deals with the 32 features impact breast cancer and its diagnosis of 570 participants")

    col1,col2 = st.columns(2)

    with col1:
        st.header("Rows")
        st.write("570")
    with col2:
        st.header("Columns")
        st.write("32")
    
    st.header("Data")
    st.dataframe(data, use_container_width = True)

def tasks():
    st.title("Tasks")
    group4Tasks = [
        "Summary Statistics" ,
        "Outlier Detection" ,
        "Data Distribution Analysis" ,
        "Class Distribution" ,
        "Correlation Analysis" ,
        "Feature Relationships" ,
        "Categorical Data Analysis/Segmentation",
        "Feature Importance" 
    ]
    group4Members = ["Hemaank","Chaitanya","Amit","Imran","Aadar","Akash","Pragya","Sonu"]

    taskData = pd.DataFrame(list(zip(group4Tasks, group4Members)), columns =['Task', 'Member'])
    st.dataframe(taskData, use_container_width = True)

def dashboard():
    init_streamlit_comm()
    @st.cache_resource
    def get_pyg_html(df: pd.DataFrame) -> str:
        html = get_streamlit_html(df, spec="./gw0.json", use_kernel_calc=True, debug=False)
        return html
    @st.cache_data
    def get_df() -> pd.DataFrame:
        return data
    
    df = get_df()

    components.html(get_pyg_html(df), width=1300, height=1000, scrolling=True)


page_names_to_funcs = {
    "About": about,
    "Tasks": tasks,
    "Dashboard" : dashboard
}

demo_name = st.sidebar.selectbox("Choose a page", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()