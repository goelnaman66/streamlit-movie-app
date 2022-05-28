import numpy as np
import pickle
import pandas as pd
import streamlit as st 

def Analysis():
  df=pd.read_csv("surprise_results.csv")
  st.text("")
 
  col1, col2, col3 = st.columns(3)
  col2.header('Statistics')
  col2.write(df)
  x=df['Algorithm']
  y1=df['test_rmse']
  y2=df['fit_time']
  y3=df['test_time']
  df = df.rename(columns={'Algorithm':'index'}).set_index('index')
  st.text("")
  st.text("")
  st.text("")
  st.text("")
  st.text("")
  st.text("")
  col1, col2, col3 = st.columns(3)
  col1.line_chart(df["test_rmse"])
  col2.line_chart(df['fit_time'])
  col3.line_chart(df['test_time'])



def main():
    st.set_page_config(layout="wide")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Movie Recommendation Analysis </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.text("")
    if st.button("Start Analysis"):
        Analysis()
    

if __name__=='__main__':
    main()
    
    
    
