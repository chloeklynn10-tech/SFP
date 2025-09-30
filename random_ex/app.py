import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image

st.title("🎨 Advanced Drawing Board")

st.write("Choose pen styles, colors, and paper backgrounds to draw on.")

# Sidebar controls
st.sidebar.header("🖌️ Drawing Settings")

# Pen thickness
stroke_width = st.sidebar.slider("✏️ Pen thickness", 1, 50, 5)

# Pen color
stroke_color = st.sidebar.color_picker("🎨 Pen color", "#000000")

# Pen type
pen_type = st.sidebar.radio("🖊️ Pen type", ["Normal", "Highlighter"])

if pen_type == "Highlighter":
    stroke_color = stroke_color + "80"  # make it transparent

# Paper background options
paper_choice = st.sidebar.selectbox("📄 Paper type", ["White", "Notebook", "Yellow Pad"])

if paper_choice == "White":
    bg_color = "#ffffff"
    bg_image = None
elif paper_choice == "Notebook":
    # Light blue ruled notebook
    bg_color = "#ffffff"
    bg_image = "https://i.imgur.com/8fKQ7YQ.png"
elif paper_choice == "Yellow Pad":
    bg_color = "#fffacd"  # light yellow
    bg_image = None

# Drawing mode
drawing_mode = st.sidebar.selectbox("Mode", ["freedraw", "line", "rect", "circle", "transform"])

# Canvas
canvas_result = st_canvas(
    fill_color="rgba(255,255,255,0)",
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    background_image=Image.open("notebook.jpg") if paper_choice == "Notebook" else None,
    update_streamlit=True,
    height=500,
    width=700,
    drawing_mode=drawing_mode,
    key="canvas",
)

# Save button
if canvas_result.image_data is not None:
    st.image(canvas_result.image_data, caption="🖌️ Your Drawing")
    if st.button("💾 Save as PNG"):
        Image.fromarray(canvas_result.image_data.astype("uint8")).save("my_drawing.png")
        st.success("Saved as my_drawing.png ✅")
