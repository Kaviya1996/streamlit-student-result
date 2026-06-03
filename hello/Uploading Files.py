import streamlit as st
import pandas as pd
from io import StringIO

# Page Configuration
st.set_page_config(
    page_title="Multi-Sheet Excel Data Integration",
    page_icon="📊",
    layout="wide"
)

#uploaded_file = st.file_uploader("Choose a file")
#if uploaded_file is not None:
    # To read file as bytes:
#    bytes_data = uploaded_file.getvalue()
#    st.write(bytes_data)

    # To convert to a string based IO:
#    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
#    st.write(stringio)

    # To read file as string:
#    string_data = stringio.read()
#    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
#    dataframe = pd.read_csv(uploaded_file)
#    st.write(dataframe)

st.title("Excel to CSV Merger")

uploaded_files = st.file_uploader(
    "Upload Excel Files",
    accept_multiple_files=True,
    type=["xlsx"]
)

if uploaded_files:
    mergedata=[]
    for uploaded_file in uploaded_files:
        st.subheader(f"📄 {uploaded_file.name}")

        df = pd.read_excel(uploaded_file)
        
        st.dataframe(df)

        #if len(uploaded_files) == 2:
        mergedata.append(df)

    merged_df = pd.concat(mergedata, ignore_index=True)

    #merged_df = merged_df.sort_values(by="SNo", ascending=True)

    st.subheader("Merged Data")
    st.dataframe(merged_df)

    csv_data = merged_df.to_csv(index=False)

        #if len(uploaded_files) == 2:
            #df1 = pd.read_excel(uploaded_files[0])
            #df2 = pd.read_excel(uploaded_files[1])

            #merged_df = pd.merge(df1, df2)

            #st.dataframe(merged_df)

    # Download Button
    st.download_button(
        label="Download Merged CSV",
        data=csv_data,
        file_name="merged_data.csv",
        mime="text/csv"
    )
