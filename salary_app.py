import streamlit as st
import pickle
import pandas as pd

# Load the trained regression model
with open("kaggle2022_model.pkl", "rb") as f:
    model = pickle.load(f)  


# Define the education mapping used in training
education_mapping = {
    "I did not complete any formal education": 0,
    "Primary/elementary school": 0,
    "Secondary school": 1,
    "Some college/university study without earning a bachelor’s degree": 1,
    "Bachelor’s degree": 2,
    "Professional degree": 3,
    "Master’s degree": 3,
    "Doctoral degree": 4,
    "No response": 0,
    "Not answered": 0
}

# Available countries based on cleaned data model (excluding reference category 'Canada')
available_countries = ["Canada", "Australia", "Bangladesh", "Brazil", "South Africa", "South Korea",
                       "Spain", "Taiwan", "Thailand", "Tunisia", "Turkey", 
                       "United Kingdom of Great Britain and Northern Ireland",
                       "United States of America", "Vietnam" , "Chile",
                       "China",
                       "Columbia"
                       "Egypt", "Other"]  # Canada is the reference (not one-hot encoded)

        


# App UI
st.title("💼 Salary Predictor")
st.subheader("📈 Predict your salary based on skills, experience, and education")

# User Inputs
education = st.selectbox("🎓 Education Level", list(education_mapping.keys()))
years_coding = st.slider("💻 Years of Coding Experience", 0, 40, 5)
country = st.selectbox("🌍 Country", available_countries)

codes_java = st.checkbox("Codes in JAVA")
codes_python = st.checkbox("Codes in Python")
codes_sql = st.checkbox("Codes in SQL")
codes_go = st.checkbox("Codes in GO")

# Map education
education_num = education_mapping[education]

# Create feature dictionary
features = {
    "Education": education_num,
    "Years_Coding": years_coding,
    "Codes_In_JAVA": int(codes_java),
    "Codes_In_Python": int(codes_python),
    "Codes_In_SQL": int(codes_sql),
    "Codes_In_GO": int(codes_go),
    # One-hot encoded country features (Canada is the reference, so all 0 if Canada)
    "Country_Other": 0,
    "Country_Australia": 0,  
    "Country_Bangladesh": 0,
    "Country_Brazil": 0,
    "Country_South Africa": 0,  
    "Country_South Korea" : 0,
    "Country_Spain": 0,
    "Country_Taiwan": 0,
    "Country_Thailand": 0,  
    "Country_Tunisia": 0 ,
    "Country_Turkey": 0,
    "Country_United Kingdom of Great Britain and Northern Ireland": 0,
    "Country_United States of America" : 0,  
    "Country_Viet Nam" : 0,
    "Country_Canada" : 0,
    "Country_Chile" : 0,
    "Country_China": 0,
    "Country_Colombia": 0,
    "Country_Egypt": 0,
    "Country_France": 0,
}
if country != "Canada":
    valid_countries = {
        "Australia",
        "Bangladesh",
        "Brazil",
        "South Africa",
        "South Korea",
        "Spain",
        "Taiwan",
        "Thailand",
        "Tunisia",
        "Turkey",
        "United Kingdom of Great Britain and Northern Ireland",
        "Viet Nam",
        "United States of America",
        "Chile",
        "China",
        "Columbia"
        "Egypt",
        "Other"
    }



    if country in valid_countries:
        features[f"Country_{country}"] = 1
    else: 
        features["Country_Canada"] = 1



# Convert to DataFrame for prediction
input_data = pd.DataFrame([features])

# Section header
st.markdown("### 📊 Salary Prediction")
st.write("Click the button below to estimate your salary:")

if st.button("💵 Predict Salary"):
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Estimated Salary: **${prediction:,.2f}**")

# Footer
st.markdown("---")
st.markdown(
    "<small>📘 Built with ❤️ using Streamlit — by Jiya, Rhea, and Michael>",
    unsafe_allow_html=True
)
