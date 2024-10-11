
# ShapE-TextTo3D-HPC

This project is a 3D image-to-3D model pipeline that is containerized using Singularity and is ready to run on an HPC system. It is designed for users who need to transform 2D images into 3D models using the ShapE framework while leveraging the power of high-performance computing (HPC). The project has been successfully tested on the HPC system at [FAU](https://hpc.fau.de/).

## Features
- Converts 2D images to 3D models using ShapE.
- Containerized with Singularity for easy deployment on HPC environments.
- Includes an example job script for submission on SLURM-based HPC systems.
- Tested on the A100 GPU partition.

## Reference
This project utilizes the model and concepts from the following repository:
[ShapE Image-to-3D Model by OpenAI](https://huggingface.co/openai/shap-e-img2img)

### Installation

To set up the project, follow these steps:

1. **Clone the Repository**:  
   Clone the main repository of this project using the command below:

   ```bash
   git clone https://github.com/NavidKhezrian/ShapE-ImageTo3D-HPC.git
   cd ShapE-ImageTo3D-HPC
   ```

2. **Clone the shap-e-img2img Repository**:  
   After cloning the main repository, navigate to the project's main directory and clone the `shap-e-img2img` repository from Hugging Face using:

   ```bash
   git lfs install
   git clone https://huggingface.co/openai/shap-e-img2img
   ```

   Ensure that the `shap-e-img2img` repository is cloned within the main directory of your project for proper integration.


## Usage

### Running on an HPC System
1. Build the Singularity image using the provided `singularity.def` file:
    ```bash
    singularity build shap_e_img.sif singularity.def
    ```

2. Prepare your input image in `.png` format and place it in the `input` directory.

3. Submit the job to the SLURM scheduler using the provided `job.sh` script:
    ```bash
    sbatch job.sh <image_name>
    ```
   Replace `<image_name>` with the name of your image (without the `.png` extension). The output 3D model will be saved in the `output` directory.

### Example
To run the pipeline with an image named `apple`, execute:
```bash
sbatch job.sh apple
```
The resulting 3D model will be saved in the `output/apple/` directory.

## Files Overview
- `main.py`: Contains the main script for converting images to 3D models.
- `singularity.def`: Singularity definition file for building the container.
- `job.sh`: SLURM job script for running the containerized pipeline on an HPC system.
- `requirements.txt`: Lists all necessary Python dependencies.



