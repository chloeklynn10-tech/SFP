import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Title
st.title("🎨 Fun Drawing Board")

st.write("Draw anything you like! Pick a color, set a stroke width, and doodle freely.")

# Sidebar controls
stroke_width = st.sidebar.slider("✏️ Pen thickness", 1, 25, 5)
stroke_color = st.sidebar.color_picker("🎨 Pen color", "#000000")  # black default
bg_color = st.sidebar.color_picker("🖼️ Background color", "#ffffff")  # white default
drawing_mode = st.sidebar.selectbox("Mode", ["freedraw", "line", "rect", "circle", "transform"])
realtime_update = st.sidebar.checkbox("Update in realtime", True)

# Create canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 255, 255, 0)",  # Transparent fill
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    update_streamlit=realtime_update,
    height=400,
    drawing_mode=drawing_mode,
    key="canvas",
)

# Display results
if canvas_result.image_data is not None:
    st.image(canvas_result.image_data, caption="🖌️ Your Drawing")
