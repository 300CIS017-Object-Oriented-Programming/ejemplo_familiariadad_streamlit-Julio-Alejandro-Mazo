import streamlit as st

def probar_streamlit():

    st.write("Bienvenidos")
    if st.button('¿Como estan?'):
        st.write('¿Qué estan haciendo?')
    else:
        st.write('Goodbye\n')

    """ Ponga aqui todos los controles de prueba para que entienda como funciona"""
    st.write("Agregue aquí botones, paneles, y opciones tal como se describe en el readme")
    st.button("Soy un boton\n")

    genre = st.radio(
        "Cuál es tu película favorita",
        ('Jhon Wick', 'Bob Esponja', 'Black Adam'))

    if genre == 'Jhon wick':
        st.write('Selecionaste Jhon Wick.')
    else:
        st.write("Eres la Bestia")


# Main call
if __name__ == "__main__":
    probar_streamlit()