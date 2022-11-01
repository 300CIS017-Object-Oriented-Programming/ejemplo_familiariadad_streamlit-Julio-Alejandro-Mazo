import streamlit as st

def probar_streamlit():

    col1, col2 = st.columns(2)

    with col1:
        st.header("Hello")
        st.write("Bienvenidos")
        if st.button('¿Como estan?'):
            st.write('¿Qué estan haciendo?')
        else:
            st.write('Goodbye\n')


    with col2:
        st.header("A dog")
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