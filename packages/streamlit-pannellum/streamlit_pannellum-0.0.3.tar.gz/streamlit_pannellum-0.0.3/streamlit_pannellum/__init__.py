import os
import streamlit.components.v1 as components

_RELEASE = True

if not _RELEASE:
  _component_func = components.declare_component(
    "streamlit_pannellum",
    url="http://localhost:5173", # vite dev server port
  )
else:
  parent_dir = os.path.dirname(os.path.abspath(__file__))
  build_dir = os.path.join(parent_dir, "frontend/dist")
  _component_func = components.declare_component("streamlit_pannellum", path=build_dir)

def streamlit_pannellum(config={}, key=None):
  component_value = _component_func(config=config, key=key, default=0)
  return component_value

if not _RELEASE:
  import streamlit as st
  st.subheader("Component Test")
  streamlit_pannellum(
    config={
      "default": {
        "firstScene": "first",
      },
      "scenes": {
        "first": {
          "title": "My first example",
          "type": "equirectangular",
          "panorama": "https://pannellum.org/images/alma.jpg",
          "autoLoad": True,
          "author": "Me",
          "hotSpots": [
            {
              "pitch": 15,
              "yaw": 0,
              "type": "info",
              "text": "This is an info."
            },
            {
              "pitch": 0,
              "yaw": -10,
              "type": "scene",
              "text": "Second scene",
              "sceneId": "second"
            }
          ],
        },
        "second": {
          "title": "My second example",
          "type": "equirectangular",
          "panorama": "https://pannellum.org/images/alma.jpg",
          "autoLoad": True,
          "author": "always Me",
          "hotSpots": [
            {
              "pitch": 15,
              "yaw": 0,
              "type": "info",
              "text": "This is an info."
            },
            {
              "pitch": 0,
              "yaw": -10,
              "type": "scene",
              "text": "First scene",
              "sceneId": "first"
            }
          ],
        }
      }
    }
  )
