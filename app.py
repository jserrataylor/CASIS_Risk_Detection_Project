import streamlit as st
import joblib
import numpy as np

# Carga del modelo
model = joblib.load('casis_svm_model.pkl')

# Título de la aplicación
st.title('CASIS Screening Tool')

# Versión de la aplicación
st.write("**_Version 1.0_**")
st.write("***Conductas Autolesivas Sin Intención Suicida / Non-Suicidal Self-Injury***")

# Advertencia de uso
st.write("**Usage Warnings:** This tool is **ONLY** for academic and research purposes and should not be used as a clinical diagnosis. It is intended to provide an initial impression based on risk screening, and any serious concerns should be discussed with a health professional. This trial version is **ONLY** to illustrate its operation.")

# Política de privacidad y consentimiento
st.markdown("""
### Privacy Policy and Consent

Before you begin, please read our [Privacy Policy](https://jserrataylor.github.io/pages/casis/privacy_and_data.md) to understand how we protect and use the data we collect.

By continuing with this questionnaire, you agree that:
- The system provides an initial impression, and does NOT offer a clinical diagnosis.
- Your responses will be used solely for academic and research purposes.
- Your data will be anonymized to protect your identity.
- We do not store personal or identifiable data after the session ends, only data on application usage and interactions.
- We implement security measures to protect your data against unauthorized access and loss.
- We reserve the right to modify our privacy policy. Any changes will be communicated through our platform.
""")

# Confirmación de consentimiento
if st.checkbox('**I accept the conditions, am 18 years or older, and understand the privacy policy.**'):

    # Instrucciones para el usuario
    st.markdown("""
    **User Instructions:**

    This questionnaire is designed to assess the risk of **Non-Suicidal Self-Injury (NSSI)**. Please respond honestly to each question by selecting the option that best reflects your current situation.

    After you have answered all the questions, click the "**Submit**" button to obtain the results of the assessment.
    """)

    # Definición de las preguntas
    questions = [
        "Are you concerned about your eating habits?",
        "Do you have trouble sleeping?",
        "Have you attended counseling or psychotherapy for concerns about your mental health?",
        "Have you felt the need to reduce your use of alcoholic beverages or other drugs?",
        "Have you had panic attacks or episodes of severe anxiety?",
        "Have you seriously considered harming another person?",
        "Have you had sexual contacts or other sexual experiences unwillingly?"
    ]

    # Formulario de preguntas
    form = st.form(key='casis_form')
    answers = []
    for question in questions:
        answer = form.radio(question, ['Yes', 'No'], index=1, key=question)
        answers.append(answer)

    # Botón de envío
    submit_button = form.form_submit_button(label='Submit')

    if submit_button:
        # Conversión de respuestas a valores numéricos y predicción
        numerical_answers = [1 if a == 'Yes' else 0 for a in answers]
        prediction_proba = model.predict_proba([numerical_answers])
        proba = prediction_proba[0][1] * 100  # Assuming the second class is of interest

        # Traducción del mensaje de resultado según la probabilidad
        if proba < 25:
            gradation = "low"
            advice = "However, if you have concerns about your wellbeing, consider seeking professional support."
        elif proba < 50:
            gradation = "moderately low"
            advice = "It would be prudent to more closely evaluate your experiences and consider seeking professional support."
        elif proba < 75:
            gradation = "moderate"
            advice = "It is advisable to seek professional support to further explore these indicators."
        else:
            gradation = "high"
            advice = "Seeking professional support as soon as possible is highly recommended."

        result = f"Based on your responses, the results suggest a **{gradation}** possibility of having indicators associated with NSSI with a {proba:.2f}% probability. {advice}"
        st.write(result)
else:
    st.write("**You must accept the conditions to continue.**")

# Contacto técnico y agradecimientos
st.write("**Technical Contact:** If you need any information or have any questions about this application, you can contact the email: mhs.rrp@upr.edu")
st.write("**Acknowledgments:** We appreciate the collaboration of the Graduate Studies and Research Deanery, the Deanery of Students, and the Department of Student Development Counseling at the Rio Piedras Campus.")
st.write("**How to cite this application:** Serra-Taylor, J. & Perez-Torres, S. (2024). CASIS Screening Tool (Version 1.0) [Software]. Retrieved from https://casis-app-test.streamlit.app/")

