import pandas as pd
import streamlit as st

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

page_names_to_funcs = {
    "About": about,
    "Tasks": tasks
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()