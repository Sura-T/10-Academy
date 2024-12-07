# 🌞 MoonLight Energy Solutions: Solar Radiation Insights Dashboard

## 📋 **Project Overview**

Welcome to the **MoonLight Energy Solutions Solar Radiation Insights Dashboard**! This dashboard is designed to help visualize key insights related to solar radiation, wind speed, temperature, and other environmental factors to support decision-making for solar investments.

The goal of this project is to:
- Analyze solar radiation measurement data across regions (Benin, Sierra Leone, and Togo).
- Identify key trends, patterns, and outliers using statistical analysis and visualization.
- Visualize the relationship between wind conditions, temperature, and solar radiation using **Streamlit**.

---

## 🏆 **Features**

1. **Exploratory Data Analysis (EDA)**:
   - Visualize trends in **Global Horizontal Irradiance (GHI)**, **Direct Normal Irradiance (DNI)**, and **Diffuse Horizontal Irradiance (DHI)** over time.
   - Perform **outliers detection** to identify anomalies in the GHI data.
   - Understand correlations among environmental variables like GHI, wind speed, humidity, and temperature.

2. **Interactive Streamlit Dashboard**:
   - A user-friendly, interactive dashboard with visualizations to explore data insights dynamically.
   - Features include:
     - Correlation heatmaps.
     - Time-series analysis.
     - Wind and solar speed analysis.
     - Outliers detection visualization.

---

## 📊 **Screenshots**

### **1. Time-Series Analysis**
Visualize trends of GHI, DNI, DHI, and Tamb over time.
![Time-Series Analysis Screenshot](assets/screenshots/time_series_analysis.png)

---

### **2. Correlation Heatmap Analysis**
View correlations between solar radiation, wind speed, and environmental factors.
![Correlation Heatmap Screenshot](assets/screenshots/correlation_heatmap.png)

---

### **3. Wind-Solar Analysis**
Explore the relationship between wind speed and GHI values dynamically.
![Wind-Solar Analysis Screenshot](assets/screenshots/wind_solar_analysis.png)

---

### **4. Outliers Detection**
Identify anomalies in GHI values using statistical visualization.
![Outliers Detection Screenshot](assets/screenshots/outliers_detection.png)

---

## ⚙️ **Setup Instructions**

To set up this project locally and run the dashboard:

---

### **1. Clone the Repository**
Clone this repository to your local machine:
```bash
git clone https://github.com/<your-github-username>/10-Academy.git
```

### **2. Navigate into the project directory**
```bash
cd 10-Academy
```
### **3. Set up a virtual environment**
Create a virtual environment using the following command:
```bash
python -m venv venv
```
### **4. Activate the virtual environment**
For Windows:
```bash
.\venv\Scripts\Activate
```
For macOS/Linux:
```bash
source venv/bin/activate
```
### **5. Install the required dependencies**
Run this command to install the required dependencies:
```bash
pip install -r requirements.txt
```
### **6. Run the Streamlit App**
Start the dashboard by running:
```bash
streamlit run src/app/main.py
```
Your default browser will open at: http://localhost:8501.

## ✨ How to Use the Dashboard

After running streamlit run, visit http://localhost:8501 in your browser.
Use the sidebar menu to select from:
- **Time-Series Analysis:** Visualize trends over time for GHI, DNI, DHI, and temperature.
- **Correlation Heatmap Analysis:** Visualize statistical relationships.
- **Wind-Solar Analysis:** Explore how wind speed interacts with GHI data.
- **Outliers Detection:** Visualize anomalies in the GHI data.

## ✨ Technologies Used
- **Python:** Programming language for analysis and visualization.
- **Pandas:** Data analysis.
- **Seaborn/Matplotlib:** Visualization libraries.
- **Streamlit:** Interactive dashboard.
- **Git/GitHub:** Version control system and collaboration platform.

## 💼 Acknowledgments
Special thanks to MoonLight Energy Solutions for the opportunity to demonstrate these insights and build this visualization pipeline.

## 📜 Contributing
If you want to contribute to this project, feel free to fork the repository, create a branch, and make a pull request with improvements!

## 🛠️ Contact
If you face any issues, feel free to contact:

Surafel Takele: surafeltakele09@gmail.com

Thank you for exploring this dashboard. Let’s build sustainable energy insights together! 🌞
