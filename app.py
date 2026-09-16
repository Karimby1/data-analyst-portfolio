import pathlib

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Karim Ben Youssef — Data Analyst",
    page_icon="📊",
    layout="wide",
)

st.markdown(
    """
    <style>
        .block-container {padding: 0 !important; max-width: 100% !important;}
        header[data-testid="stHeader"] {display: none;}
        iframe {border: none;}
    </style>
    """,
    unsafe_allow_html=True,
)

fragment_path = pathlib.Path(__file__).parent / "index.html"
fragment_html = fragment_path.read_text(encoding="utf-8")

page_html = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
</head>
<body style="margin:0;">
{fragment_html}
</body>
</html>"""

components.html(page_html, height=1000, scrolling=True)
