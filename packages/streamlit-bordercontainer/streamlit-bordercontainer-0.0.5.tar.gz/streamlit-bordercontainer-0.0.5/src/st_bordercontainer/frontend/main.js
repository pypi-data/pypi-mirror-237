// The `Streamlit` object exists because our html file includes
// `streamlit-component-lib.js`.
// If you get an error about "Streamlit" not being defined, that
// means you're missing that file.

function sendValue(value) {
  Streamlit.setComponentValue(value);
}

/**
 * The component's render function. This will be called immediately after
 * the component is initially loaded, and then again every time the
 * component gets new data from Python.
 */
function onRender(event) {
  // Only run the render code the first time the component is loaded.
  if (!window.rendered) {
    // You most likely want to get the data passed in like this
    // const {input1, input2, input3} = event.detail.args
    // You'll most likely want to pass some data back to Python like this
    // sendValue({output1: "foo", output2: "bar"})
    const { chatlist, height } = event.detail.args;

    let innerHtml = "";
    if (chatlist?.length && chatlist.length > 0) {

      for (let i = 0; i < chatlist.length; i++) {
        innerHtml += `
         '<div class="${
           chatlist[i].user ? "messageRow" : "responseRow"
         }"><div class="${chatlist[i].user ? "avator" : "rebotAvator"}"> ${
          chatlist[i].user ? chatlist[i].user : chatlist[i].robot
        }</div> ${
          chatlist[i].user
            ? chatlist[i].question.type === "img"
              ? "<div class='imgBox'><img src=" +
                chatlist[i].question.content +
                " /></div>"
              : "<div class='questionBox'>" +
                chatlist[i].question.content +
                " </div>"
            : chatlist[i].response.type === "img"
            ? "<div class='imgBox'><img src=" +
              chatlist[i].response.content +
              " /></div>"
            : "<div class='responseBox'>" +
              chatlist[i].response.content +
              " </div>"
        }</div>

        `;
      }
    }

    if (innerHtml) {
      document.getElementById("borderContainer").innerHTML = innerHtml;
    }
    document.getElementById("borderContainer").style.height = height - 2 + "px";
    Streamlit.setFrameHeight(height);
    window.rendered = true;
  }
}

// Render the component whenever python send a "render event"
Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender);
// Tell Streamlit that the component is ready to receive events
Streamlit.setComponentReady();
// Render with the correct height, if this is a fixed-height component
Streamlit.setFrameHeight(640);
