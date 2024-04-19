import streamlit as st

st.write('Hello, world!')

věta = st.text_input("Zadejte něco a stiskněte enter:")
st.write('Zadali jste: ', věta)

# Přidání tlačítka
if st.button('Stiskni mě'):
    st.write('Tlačítko bylo stisknuto!')

# Přidání posuvníku pro výběr čísla
number = st.slider('Vyber číslo:', 0, 100, 50)
st.write('Vybrané číslo:', number)

# Přidání výběru z možností
option = st.selectbox(
    'Jakou máte rádi zmrzlinu?',
    ('Čokoládová', 'Vanilková', 'Jahodová')
)
st.write('Vaše oblíbená zmrzlina:', option)

st.markdown("""
# Nadpis první úrovně
Toto je *kurzíva* a toto je **tučné**.

- Bod 1
- Bod 2
- Bod 3

""")
st.subheader('This is a subheader with a divider', divider='rainbow')
st.subheader('_Streamlit_ is :blue[cool] :sunglasses:')

st.write("This is some text.")

st.slider("This is a slider", 0, 100, (25, 75))

st.divider()  # 👈 Draws a horizontal rule

st.write("This text is between the horizontal rules.")

st.divider()  # 👈 Another horizontal rule



st.caption('This is a string that explains something above.')
st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')
