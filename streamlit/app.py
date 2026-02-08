import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path to import langchain_helper
sys.path.append(str(Path(__file__).parent.parent))
from langchain_helper import generate_restaurant_name_items

# Page configuration
st.set_page_config(
    page_title="Restaurant Name Generator",
    page_icon="🍽️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        color: #FF6B6B;
        font-size: 3em;
        font-weight: bold;
        margin-bottom: 0.5em;
    }
    .sub-header {
        text-align: center;
        color: #4ECDC4;
        font-size: 1.2em;
        margin-bottom: 2em;
    }
    .restaurant-name {
        text-align: center;
        color: #FFE66D;
        font-size: 2.5em;
        font-weight: bold;
        padding: 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        margin: 20px 0;
    }
    .menu-container {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
    }
    .menu-item {
        font-size: 1.1em;
        padding: 8px;
        margin: 5px 0;
        background-color: white;
        border-left: 4px solid #667eea;
        border-radius: 5px;
        color: #333333;
    }
    .sidebar .sidebar-content {
        background-color: #f0f2f6;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">🍽️ Restaurant Name Generator</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Discover the perfect name and menu for your restaurant using AI</div>', unsafe_allow_html=True)

st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("🌍 Choose Your Cuisine")
    st.markdown("Select a cuisine type to generate a unique restaurant name and menu items.")
    
    cuisine = st.selectbox(
        "Cuisine Type:",
        ("Indian", "Arabian", "Mexican", "Italian", "American", "Japanese", "Chinese"),
        index=0
    )
    
    st.markdown("---")
    st.markdown("### About")
    st.info("This app uses AI to generate creative restaurant names and matching menu items based on your chosen cuisine.")

# Main content
if cuisine:
    with st.spinner(f'🔮 Generating {cuisine} restaurant concept...'):
        response = generate_restaurant_name_items(cuisine)
    
    # Display restaurant name with custom styling
    st.success("✨ Your Restaurant Concept is Ready!")
    st.markdown(f'<div class="restaurant-name">{response["restaurant_name"].strip()}</div>', unsafe_allow_html=True)
    
    # Display menu items
    st.markdown("### 📋 Suggested Menu Items")
    menu_items = [item.strip() for item in response['menu_items'].strip().split("\n") if item.strip()]
    
    for item in menu_items:
        st.markdown(f'<div class="menu-item">{item}</div>', unsafe_allow_html=True)
    
    # Footer section
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Cuisine", cuisine, "")
    with col2:
        st.metric("Menu Items", len([i for i in menu_items if i.strip()]), "")
    with col3:
        if st.button("🔄 Generate New"):
            st.rerun()
else:
    st.info("👈 Please select a cuisine from the sidebar to get started!")