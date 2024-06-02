!sudo apt install tesseract-ocr
!pip install pytesseract
!pip install gradio
def save_image(image):

    import shutil
    import os

    output_dir = "/content/images/"
    image_name = "image.jpg"

    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for img in image:
        shutil.copy(img.name, os.path.join(output_dir, image_name))

    return "Successful!"
def process_image():

    import pytesseract
    from PIL import Image

    image_path = "/content/images/image.jpg"
    text = pytesseract.image_to_string(Image.open(image_path))

    return text
import gradio as gr

css = """
.col{
    max-width: 50%;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
"""

with gr.Blocks(css=css) as demo:
    gr.Markdown("## <center>OCR App</center>")

    with gr.Tab("Upload image and extract text"):
      with gr.Column(elem_classes="col"):

        with gr.Tab("Live demo section"):
          with gr.Column():

            ocr_save_input = gr.Files(label="Upload image")
            ocr_save_button = gr.Button("Save image")
            ocr_save_output = gr.Textbox(label="Output")

            ocr_process_button = gr.Button("Process image")
            ocr_process_output = gr.Textbox(label="Output")

            gr.ClearButton([ocr_save_input, ocr_save_output, ocr_process_output])

    #########################################################################################################

    ocr_save_button.click(save_image, inputs=ocr_save_input, outputs=ocr_save_output)
    ocr_process_button.click(process_image, inputs=None, outputs=ocr_process_output)

    #########################################################################################################

demo.queue()
demo.launch(debug=True, share=True)
