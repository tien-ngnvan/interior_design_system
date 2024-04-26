import gradio as gr
from re_func_tab.func_tab2 import *
import cv2, os
import pandas as pd

def Tab2():
    with gr.Tab("Bright Image") as remove_tab:
        with gr.Row():
            with gr.Column():
                gr.Markdown("Choose way to segment")
            with gr.Column():
                method = gr.Dropdown(value="add_point",choices=["add_point", "remove_point"])

        with gr.Row():
            with gr.Column():
                image = cv2.imread(os.path.join("outputs", "output_tab1", "input_WB_new.png"))
                cv2.imwrite(os.path.join("outputs", "input_tab2", "image_0.png"), image) 
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)              
                input_image = gr.Image(value=image)
            with gr.Column():
                predict_image = gr.Image()
                
        with gr.Row():
            with gr.Column():
                reset_button = gr.Button("Reset")
            with gr.Column():
                undo_button = gr.Button("Undo")
            with gr.Column():
                apply_button = gr.Button("Apply")
        with gr.Row():
            remove_image = gr.Image() 
        input_image.select(segment_func, inputs=[input_image, method], outputs=[predict_image])
        apply_button.click(apply_func, inputs=[predict_image])
        undo_button.click(undo_func, inputs=[input_image], outputs=[predict_image])
        reset_button.click(reset_func, outputs=[predict_image])
    return remove_tab