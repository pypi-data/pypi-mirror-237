from pathlib import Path
from typing import Optional

import streamlit as st
import streamlit.components.v1 as components

# Tell streamlit that there is a component called st_bordercontainer,
# and that the code to display that component is in the "frontend" folder
frontend_dir = (Path(__file__).parent / "frontend").absolute()
_component_func = components.declare_component(
	"st_bordercontainer", path=str(frontend_dir)
)

# Create the python function that will be called
def st_bordercontainer(
    key: Optional[str] = None,
    chatlist = [],
    height = 400
):
    """
    Add a descriptive docstring
    """
    component_value = _component_func(
        key=key,
        chatlist=chatlist,
        height=height
    )

    return component_value


def main():
    # st.write("## Example")
    chatlist = [
      {
        "question":
          "https://static.openxlab.org.cn/landmarks/pc/footerbanner.png",
        "response": "ou'll most likely want to pass some data back to Python like thisou'll most likely want to pass some data back to Python like thisou'll most likely want to pass some data back to Python like thisou'll most likely want to pass some data back to Python like thisou'll most likely want to pass some data back to Python like thisou'll most likely want to pass some data back to Python like this",
        "user": "user",
        "robot": "robot",
      },
      {
        "question":
          "https://static.openxlab.org.cn/landmarks/pc/footerbanner.png",
        "response": "ssss",
        "user": "assistant",
        "robot": "robot",
      }
     ]
    value = st_bordercontainer(chatlist = chatlist,height=300)

    st.write(value)


if __name__ == "__main__":
    main()
