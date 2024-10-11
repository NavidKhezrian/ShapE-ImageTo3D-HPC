#!/bin/bash -l
#                                  # -l is necessary to initialize modules correctly!
#SBATCH --time=00:05:00            # comments start with # and do not count as interruptions
#SBATCH --gres=gpu:a100:1
#SBATCH --partition=a100
#SBATCH --export=NONE              # do not export environment from submitting shell
                                   # first non-empty non-comment line ends SBATCH options
unset SLURM_EXPORT_ENV             # enable export of environment from this script to srun


mkdir -p "output/$1"



singularity run --bind ./output:/user/source/output/ \
                --bind ./input:/user/source/input \
                 shap_e_img.sif --img_path /user/source/input/$1.png --output_path /user/source/output/$1/
                    
