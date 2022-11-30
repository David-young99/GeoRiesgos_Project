import streamlit as st

st.title("Complete la información sobre la alerta que desea enviar")
st.subheader("Atención, recuerde que este formulario es únicamente para alertas de emergencia, los datos se enviarán al grupo de whatsapp de los líderes comunitarios y gestores de riesgo")
st.subheader("Introduzca los datos solicitados en la parte inferior: ")



with st.form("Myform1", clear_on_submit=True):
    name = st.text_input("Introduzca el nombre del emisor de la alerta:")
    emaill = st.text_input("introduzca su correo electrónico")
    disaster = st.selectbox("Seleccione una opción con base al desastre observado", ["Alerta por deslizamiento", "Alerta por inundación", "Alerta por ambas amenazas"])
    message = st.text_input("Introduzca más detalles sobre la emergencia")


    button = st.form_submit_button("Submit")