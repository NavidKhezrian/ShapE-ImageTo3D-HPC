#!/usr/bin/python3

import argparse 
import torch
from torch import autocast
from PIL import Image
from torchvision.transforms import functional as F
from diffusers.utils import export_to_obj
from diffusers import ShapEImg2ImgPipeline



def shap_e(img_path, guidance_scale, num_inference_steps, frame_size,output_path):

    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    pipe = ShapEImg2ImgPipeline.from_pretrained("/user/source/model/shap-e-img2img", torch_dtype=torch.float16, variant="fp16")
    pipe = pipe.to(device)

    img = Image.open(img_path).convert("RGB")

    with autocast(device):
        img_resized = F.resize(img, (256, 256))
        images = pipe(
            img_resized,
            guidance_scale=guidance_scale,
            num_inference_steps=num_inference_steps,
            frame_size=frame_size,
            output_type="mesh",
            generator=torch.Generator(device=device)
        ).images

    export_to_obj(images[0], output_path + "model.obj")   

def main():
    # Create an argument parser with descriptions
    parser = argparse.ArgumentParser(description="Create 3d model from an image.")
    
    # Define command-line arguments
    parser.add_argument(
        "--img_path", type=str,
        nargs="?"
    )
    parser.add_argument(
        "--guidance_scale",
        type=float,
        default=3.0,
        help=""
    )
    parser.add_argument(
        "--num_inference_steps",
        type=int,
        default=64,
        help=""
    )
    parser.add_argument(
        "--frame_size",
        type=int,
        default=256,
        help=""
    )
    parser.add_argument(
        "--output_path",
        type=str,
        help=""
    )
    # Parse the command-line arguments
    args = parser.parse_args()
    
    # Call the stable_diffusion function with parsed arguments
    shap_e(
        args.img_path,
        args.guidance_scale,
        args.num_inference_steps,
        args.frame_size,
        args.output_path
    )

# Execute the main function if the script is run as the main module
if __name__ == "__main__":
    main()

