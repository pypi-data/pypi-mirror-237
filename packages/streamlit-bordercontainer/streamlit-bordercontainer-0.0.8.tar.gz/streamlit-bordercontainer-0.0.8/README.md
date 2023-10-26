# streamlit-bordercontainer

a box which can set style easily

## Installation instructions 

```sh
pip install streamlit-bordercontainer
```

## Usage instructions

```python
import streamlit as st

from st_bordercontainer import st_bordercontainer

chatlist = [
      {
        "question": {
          "type": "img",
          "content":
            "https://static.openxlab.org.cn/landmarks/pc/footerbanner.png",
        },

        "user": "user"
      },
      {
        "response": {
          "type": "text",
          "content":
            "ou'll most likely want to pass some data back to Python like thisou'll most likely want to pass some data back to Python like thisou'll most likely want to pass some data back to Python like thisou'll most likely want to pass some data back to Python like thisou'll most likely want to pass some data back to Python like thisou'll most likely want to pass some data back to Python like this",
        },
        "robot": "robot1"
      },
      {
        "response": {
          "type": "img",
          "content":
            "https://static.openxlab.org.cn/landmarks/pc/footerbanner.png",
        },

        "robot": "robot2"
      },
      {
        "question": {
          "type": "text",
          "content":
            "ou'll most likely want to pass some data back to Python like thisou'll most likely want to pass some data back to Python like thisou'll most likely want to pass some data back to Python like thisou'll most likely want to pass some data back to Python like thisou'll most likely want to pass some data back to Python like thisou'll most likely want to pass some data back to Python like this",
        },
        "user": "user2"
      }
]
value = st_bordercontainer(chatlist = chatlist,height=300)

st.write(value)
