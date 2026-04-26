import streamlit as st
import json

st.set_page_config(page_title="Daily Reflection Agent", page_icon="🌳")

# Load JSON
with open("../tree/reflection-tree.json", "r", encoding="utf-8") as f:
    tree = json.load(f)

nodes = {node["id"]: node for node in tree["nodes"]}

# Session state
if "current" not in st.session_state:
    st.session_state.current = tree["start"]

st.title("🌳 Daily Reflection Tree")
st.write("Deterministic employee reflection tool")

node = nodes[st.session_state.current]

# Render nodes
if node["type"] == "start":
    st.write(node["text"])
    if st.button("Begin"):
        st.session_state.current = node["next"]
        st.rerun()

elif node["type"] == "question":
    st.subheader(node["text"])

    choice = st.radio("Choose one:", [opt["label"] for opt in node["options"]])

    if st.button("Next"):
        for opt in node["options"]:
            if opt["label"] == choice:
                st.session_state.current = opt["next"]
                st.rerun()

elif node["type"] in ["reflection", "bridge", "summary"]:
    st.info(node["text"])

    if st.button("Continue"):
        st.session_state.current = node["next"]
        st.rerun()

elif node["type"] == "end":
    st.success(node["text"])

    if st.button("Restart"):
        st.session_state.current = tree["start"]
        st.rerun()