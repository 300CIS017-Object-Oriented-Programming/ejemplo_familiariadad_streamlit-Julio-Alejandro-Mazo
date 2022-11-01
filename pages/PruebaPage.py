import streamlit as st

def probar_streamlit():
    """ Ponga aqui todos los controles de prueba para que entienda como funciona"""
    st.write("Agregue aquí botones, paneles, y opciones tal como se describe en el readme")
    st.button("Soy un boton")

    if st.button('Say hello'):
        st.write('Why hello there')
    else:
        st.write('Goodbye')


# Main call
if __name__ == "__main__":
    probar_streamlit()