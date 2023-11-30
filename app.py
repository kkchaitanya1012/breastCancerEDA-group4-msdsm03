

import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import pygwalker as pyg
import altair as alt
from pygwalker.api.streamlit import init_streamlit_comm, get_streamlit_html



st.set_page_config(
    page_title="📖 Breast Cancer Dashboard",
    layout="wide"
)

file_id = '1b2Ztm96gkVadOftMmlUXowbQtzGL8Vqp'

download_link = f'https://drive.google.com/uc?id={file_id}'

data = pd.read_csv(download_link)



def about():
    st.title("📖 Breast Cancer Data EDA")

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

def analyze():
    st.title("Visualisations and Analysis")
    st.divider()
    st.header("Class Distrubution")
    st.bar_chart(data['diagnosis'].value_counts())
    imbalance = data['diagnosis'].value_counts()[0]/data['diagnosis'].value_counts()[1]
    st.write("The dataset is imbalanced with a ratio of 1:", imbalance)
    st.divider()
    st.header("Outlier and Distribution Analysis with respect to Diagnosis")
    parameters = st.selectbox("Select a parameter", data.columns)
    boxplot = alt.Chart(data).mark_boxplot().encode(
        x='diagnosis',
        y=parameters,
        color='diagnosis'
    ).properties(
        width=700,
        height=500,
        title="Outlier and Distribution Analysis with respect to Diagnosis",
        
    )
    st.altair_chart(boxplot,theme="streamlit")
    st.divider()
    st.header("Pair Plot")
    st.write("The pair plot shows the relationship between the different features")
    cols = ['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean', 'compactness_mean',	'concavity_mean', 'diagnosis']
    pairplot = alt.Chart(data[cols]).mark_circle().encode(
        alt.X(alt.repeat("column"), type='quantitative'),
        alt.Y(alt.repeat("row"), type='quantitative'),
        color='diagnosis:N'
    ).properties(
        width=150,
        height=150
    ).repeat(
        row=['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean'],
        column=['smoothness_mean', 'compactness_mean',	'concavity_mean']
    )
    st.altair_chart(pairplot)
    st.divider()
    st.header("Correlation Matrix")
    st.write("The correlation matrix shows the correlation between the different features")
    corr = data.corr()
    st.dataframe(corr)
    st.divider()
    st.header("Correlation Bar Chart")
    st.write("The correlation bar chart shows the correlation between the different features")
    


page_names_to_funcs = {
    "About": about,
    "Tasks": tasks,
    "📈 Analysis and Viz": analyze,
    "Dashboard Playground ⏯️" : dashboard
}

demo_name = st.sidebar.selectbox("Choose a page", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()