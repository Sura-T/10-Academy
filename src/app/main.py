import streamlit as st
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend for compatibility
import matplotlib.pyplot as plt
import seaborn as sns
import os


# Helper function to load the datasets using absolute paths
def load_data():
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))  # Dynamically resolve path
        data_benin = pd.read_csv(os.path.join(base_dir, "../../assets/data/benin-malanville.csv"))
        data_sierra_leone = pd.read_csv(os.path.join(base_dir, "../../assets/data/sierraleone-bumbuna.csv"))
        data_togo = pd.read_csv(os.path.join(base_dir, "../../assets/data/togo-dapaong_qc.csv"))

        st.success("Data loaded successfully")
        return data_benin, data_sierra_leone, data_togo
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None, None, None


# Main Dashboard Logic
def main():
    st.title("MoonLight Energy Solutions - Solar Radiation Insights")
    st.write(
        """
        This interactive dashboard allows users to visualize and explore trends
        related to solar radiation, temperature, wind speed, and other environmental data insights.
        """
    )

    # Load the data
    data_benin, data_sierra_leone, data_togo = load_data()

    if data_benin is None or data_sierra_leone is None or data_togo is None:
        st.stop()

    # Sidebar for navigation
    options = ["Time-Series Analysis", "Correlation Analysis", "Wind-Solar Analysis", "Outliers Detection"]
    selected_option = st.sidebar.selectbox("Choose Analysis", options)

    # Handle navigation logic
    if selected_option == "Wind-Solar Analysis":
        st.subheader("Wind-Solar Analysis: Wind Speed vs. GHI")
        
        # Check if required columns exist before attempting visualization
        if all(col in data_benin.columns for col in ["WS", "GHI"]):
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.scatter(data_benin['WS'], data_benin['GHI'], alpha=0.5, label="Benin")
            ax.scatter(data_sierra_leone['WS'], data_sierra_leone['GHI'], alpha=0.5, label="Sierra Leone")
            ax.scatter(data_togo['WS'], data_togo['GHI'], alpha=0.5, label="Togo")
            ax.set_xlabel("Wind Speed (m/s)")
            ax.set_ylabel("Global Horizontal Irradiance (W/m²)")
            ax.legend()
            st.pyplot(fig)
        else:
            st.error("Required columns ('WS', 'GHI') are missing in the data.")

    elif selected_option == "Outliers Detection":
        st.subheader("Outliers in GHI")
        
        # Check if the data is available before plotting
        if "GHI" in data_benin.columns and not data_benin['GHI'].isna().all():
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.boxplot(data=data_benin, x='GHI', ax=ax)
            st.pyplot(fig)
        else:
            st.error("No valid GHI data found to analyze for outliers.")

    elif selected_option == "Time-Series Analysis":
        st.subheader("GHI, DNI, DHI, and Tamb over Time")
        
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(pd.to_datetime(data_benin['Timestamp']), data_benin['GHI'], label="Benin GHI")
        ax.plot(pd.to_datetime(data_sierra_leone['Timestamp']), data_sierra_leone['GHI'], label="Sierra Leone GHI")
        ax.plot(pd.to_datetime(data_togo['Timestamp']), data_togo['GHI'], label="Togo GHI")
        
        ax.set_xlabel("Timestamp")
        ax.set_ylabel("Global Horizontal Irradiance (W/m²)")
        ax.legend()
        
        st.pyplot(fig)

    elif selected_option == "Correlation Analysis":
        st.subheader("Correlation Heatmap Analysis")
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(data_benin.select_dtypes(include="number").corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
        st.pyplot(fig)


main()
