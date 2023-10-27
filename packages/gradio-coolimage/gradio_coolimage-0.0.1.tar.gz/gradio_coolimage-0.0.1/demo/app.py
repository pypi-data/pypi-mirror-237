
import gradio as gr
from gradio_coolimage import CoolImage


example = CoolImage().example_inputs()

demo = gr.Interface(
    lambda x:x,
    CoolImage(),  # interactive version of your component
    CoolImage(),  # static version of your component
    # examples=[[example]],  # uncomment this line to view the "example version" of your component
)


demo.launch()
