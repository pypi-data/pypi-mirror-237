
import gradio as gr
from gradio_testtextbox9 import TestTextbox9


example = TestTextbox9().example_inputs()

demo = gr.Interface(
    lambda x:x,
    TestTextbox9(),  # interactive version of your component
    TestTextbox9(),  # static version of your component
    # examples=[[example]],  # uncomment this line to view the "example version" of your component
)


demo.launch()
