import streamlit as st
import pyvista as pv
# from pyvista.examples import planefile
from stpyvista import stpyvista

from stpyvista.utils import start_xvfb

if "IS_XVFB_RUNNING" not in st.session_state:
  start_xvfb()
  st.session_state.IS_XVFB_RUNNING = True 


st.title("Interactive 3D Mesh Visualization")
st.write("Some useful text here.")

# Set up a PyVista plotter
plotter = pv.Plotter(window_size=(500, 900))
plotter.view_isometric()
plotter.set_background("darkgray")
# plotter.camera.zoom('tight')

# mesh = pv.Sphere()
mesh = pv.Cylinder()
# mesh = pv.read(planefile)
actor = plotter.add_mesh(mesh, color="lightblue", show_edges=True)



color = st.sidebar.color_picker("pick a color", "#82E0AA")
# camera_position = plotter.camera_position
# print(camera_position)

actor.prop.color = pv.Color(color)

# plotter.camera_position = camera_position
# stpyvista(plotter, key='pv_shape') # this key is troublesome!

stpyvista(plotter)

st.write("More text after plot")



print('made it to the end')
# uvicorn main:app --reload # backend
# streamlit run app.py # frontend