import numpy as np 
import pandas as pd 
import streamlit as st 
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.markdown('''
# ***The EDA App***
(This is the EDA App created in streamlit using the pandas profiling)
''')

#upload CSV data
with st.sidebar.header('1. Upload CSV data'):
  uploaded_file = st.sidebar.file_uploader("Upload your input CSV file",type=["csv"])
  st.sidebar.markdown('''
  Example of CSV input
  ''')
  #pandas profiling Report
  if uploaded_file is not None:
    @st.cache_data
    def load_csv():
      csv = pd.read_csv(uploaded_file)
      return csv
    df = load_csv()
    pr = ProfileReport(df,exploration = True)
    st.header('***Input Datframe***')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st.profile_report(pr)
  else:
    st.info("Awaiting for CSV file to be uploaded.")
    if st.button('Press to use Example Dataset'):
      @st.cache_data
      def load_data():
        a = pd.DatFrame(
          np.random.rand(100,5),
          columns = ['a','b','c','d','e']
        )
        return a 
      df = load_data()
      pr = ProfileReport(df,explorative=True)
      st.header('**Input DataFrame**')
      st.write(df)
      st.write('---')
      st.header('**Pandas Profiling Report')
      st.profile_report(pr)





        