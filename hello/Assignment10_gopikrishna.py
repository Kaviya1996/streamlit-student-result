import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Multi-Sheet Excel Data Integration",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Automated Multi-Sheet Excel Data Integration")
st.write("Upload one or more Excel files (.xlsx) and merge all sheets into a single CSV file.")

# File Upload
uploaded_files = st.file_uploader(
    "Upload Excel Files",
    type=["xlsx"],
    accept_multiple_files=True
)

if uploaded_files:

    all_dataframes = []

    try:
        for uploaded_file in uploaded_files:

            st.subheader(f"📄 Processing: {uploaded_file.name}")

            # Read Excel File
            excel_file = pd.ExcelFile(uploaded_file)

            st.write("Detected Sheets:")
            st.write(excel_file.sheet_names)

            # Read all sheets
            for sheet in excel_file.sheet_names:

                df = pd.read_excel(uploaded_file, sheet_name=sheet)

                # Skip empty sheets
                if not df.empty:
                    df["Source_File"] = uploaded_file.name
                    df["Source_Sheet"] = sheet

                    all_dataframes.append(df)

        if all_dataframes:

            # Merge all sheets
            merged_df = pd.concat(all_dataframes, ignore_index=True)

            st.success("✅ All sheets merged successfully.")

            # Sort Option
            st.subheader("Sort Data")

            sort_column = st.selectbox(
                "Select a column for ascending sort",
                merged_df.columns
            )

            merged_df = merged_df.sort_values(
                by=sort_column,
                ascending=True
            )

            # Preview
            st.subheader("📋 Merged Data Preview")
            st.dataframe(
                merged_df,
                use_container_width=True
            )

            # CSV Conversion
            csv = merged_df.to_csv(index=False).encode("utf-8")

            # Download Button
            st.download_button(
                label="⬇ Download Merged CSV",
                data=csv,
                file_name="merged_excel_data.csv",
                mime="text/csv"
            )

            st.info(
                f"Total Records: {len(merged_df)} | "
                f"Total Columns: {len(merged_df.columns)}"
            )

        else:
            st.warning("No data found in the uploaded sheets.")

    except Exception as e:
        st.error(f"Error: {e}")

else:
    st.info("Please upload one or more Excel files.")
