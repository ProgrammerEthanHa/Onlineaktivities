import streamlit as st
import pandas as pd
import altair as alt

st.header("Vergleich der Häufigkeit der Online-Aktivitäten mit Freundinnen und Freunden")
st.subheader("1 = nie bis 6 = täglich / 2021")

source = pd.DataFrame({
        'Häufigkeit': [5.09, 2.64],
        'Aktivitäten': ['Chatten, über soziale Netzwerke und Messenger Kontakt haben', 'Gemeinsam Online-Spiele spielen']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Häufigkeit:Q',
        x='Aktivitäten:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Basis n = 1122; Jugendliche
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle:  AID:A 2021")