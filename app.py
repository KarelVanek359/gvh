import streamlit as st
import webbrowser
st.markdown("# Kabinet fyziky GVHL")

st.image("gvh_logo.jpg")
st.markdown("### Kliknutím na tlačítko přejdeš na stránku se soubory:")

def open_url(url):
    webbrowser.open_new_tab(url)
tlacitko=st.button("Přejdi na cloud",on_click=open_url("https://onedrive.live.com/?authkey=%21AAdbH59Zolh4Vcg&id=815B93FBD69EACCA%21106&cid=815B93FBD69EACCA"))


