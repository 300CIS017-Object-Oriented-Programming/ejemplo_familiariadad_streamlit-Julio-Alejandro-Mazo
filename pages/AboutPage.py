import streamlit as st
from controller.AppController import AppController


def mostrar():
    return """
        #### 
        Aplicación de **streamlit**.

        ####
        Ejemplo elaborado para @   por Julio Mazo.
        
        Hola como estan?
        
        Soy su mes favorito

        """



# Main call
if __name__ == "__main__":
    st.write(mostrar())