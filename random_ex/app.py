import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image

st.title("🎨 Advanced Drawing Board Pro")

st.write("Choose pens, paints, paper types, and start drawing!")

# Sidebar controls
st.sidebar.header("🖌️ Drawing Settings")

# Tool selection
tool = st.sidebar.selectbox(
    "✏️ Choose a tool",
    ["Pencil", "Eraser", "Charcoal", "Ink Pen", "Fountain Pen", 
     "Acrylic Paint", "Watercolor", "Crayon", "Gouache", "Oil Paint", "Fill Paint"]
)

# Stroke size
stroke_width = st.sidebar.slider("🖊️ Brush size", 1, 60, 5)

# Color picker
stroke_color = st.sidebar.color_picker("🎨 Color", "#000000")

# Paper type
paper_choice = st.sidebar.selectbox("📄 Paper type", ["White", "Notebook", "Yellow Pad", "Grid"])

if paper_choice == "White":
    bg_color = "#ffffff"
    bg_image = None
elif paper_choice == "Notebook":
    bg_color = "#ffffff"
    bg_image = "notebook.jpg"  # You can replace with your own image
elif paper_choice == "Yellow Pad":
    bg_color = "#fffacd"
    bg_image = None
elif paper_choice == "Grid":
    bg_color = "#ffffff"
    bg_image = "grid.png"  # optional grid background

# Simulate tool behavior
if tool == "Eraser":
    stroke_color = bg_color  # draw with background color
elif tool == "Charcoal":
    stroke_width *= 2
    stroke_color = stroke_color + "40"  # semi-transparent, rough effect
elif tool == "Ink Pen":
    stroke_width = max(1, stroke_width // 2)
elif tool == "Fountain Pen":
    stroke_color = stroke_color + "90"  # semi-transparent
elif tool == "Acrylic Paint":
    stroke_color = stroke_color + "FF"  # strong opaque
elif tool == "Watercolor":
    stroke_color = stroke_color + "30"  # very transparent
elif tool == "Crayon":
    stroke_color = stroke_color + "AA"
elif tool == "Gouache":
    stroke_color = stroke_color + "D0"
elif tool == "Oil Paint":
    stroke_width *= 3
    stroke_color = stroke_color + "F0"
elif tool == "Fill Paint":
    st.warning("Click on shapes to fill color (use 'rect' or 'circle' mode).")

# Drawing mode
drawing_mode = st.sidebar.selectbox("🖌️ Mode", ["freedraw", "line", "rect", "circle", "transform"])

# Canvas
canvas_result = st_canvas(
    fill_color=stroke_color if tool == "Fill Paint" else "rgba(255, 255, 255, 0)",
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    background_image=Image.open(bg_image) if bg_image else None,
    update_streamlit=True,
    height=600,
    width=800,
    drawing_mode=drawing_mode,
    key="canvas",
)

# Save drawing
if canvas_result.image_data is not None:
    st.image(canvas_result.image_data, caption="🖌️ Your Drawing")
    if st.button("💾 Save as PNG"):
        Image.fromarray(canvas_result.image_data.astype("uint8")).save("my_drawing.png")
        st.success("Saved as my_drawing.png ✅")
