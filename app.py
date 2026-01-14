import streamlit as st
import pandas as pd
import joblib   # ✅ pickle hata diya

# ---------------- LOAD MODEL ----------------
model = joblib.load("model.pkl.gz")   # ✅ correct way

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Exam Score Prediction",
    page_icon="📘",
    layout="centered"
)

st.title("📘 Exam Score Prediction System")
st.markdown("Predict student exam score using study habits and lifestyle factors")

# ---------------- USER INPUTS ----------------
st.header("📌 Enter Student Details")

age = st.slider("Age", 15, 30, 20)
gender = st.selectbox("Gender", ["male", "female", "other"])
course = st.selectbox("Course", ["bca", "b.sc", "diploma", "b.tech", "other"])
study_hours = st.slider("Study Hours per Day", 0.0, 12.0, 3.0)
attendance = st.slider("Class Attendance (%)", 0.0, 100.0, 75.0)
internet = st.selectbox("Internet Access", ["yes", "no"])
sleep_hours = st.slider("Sleep Hours", 0.0, 12.0, 7.0)
sleep_quality = st.selectbox("Sleep Quality", ["poor", "average", "good"])
study_method = st.selectbox("Study Method", ["self study", "coaching", "online videos"])
facility = st.selectbox("Facility Rating", ["low", "medium", "high"])
exam_difficulty = st.selectbox("Exam Difficulty", ["easy", "moderate", "hard"])

# ---------------- PREDICTION ----------------
if st.button("🎯 Predict Exam Score"):

    input_data = pd.DataFrame([{
        "age": age,
        "gender": gender,
        "course": course,
        "study_hours": study_hours,
        "class_attendance": attendance,
        "internet_access": internet,
        "sleep_hours": sleep_hours,
        "sleep_quality": sleep_quality,
        "study_method": study_method,
        "facility_rating": facility,
        "exam_difficulty": exam_difficulty
    }])

    prediction = model.predict(input_data)

    st.success(f"📊 Predicted Exam Score: **{prediction[0]:.2f}**")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("💡 *Developed using Machine Learning & Streamlit*")
