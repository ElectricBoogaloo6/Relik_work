#!/bin/bash -l
#SBATCH -J Relik-testing
#SBATCH -N 1
#SBATCH --ntasks-per-node=4
#SBATCH --nodelist=node[010-014]
#SBATCH --gpus=1
#SBATCH --time=15:00:00
#SBATCH --mail-type=START,END,FAIL
#SBATCH --mail-user=k.mihhailov@student.vu.nl

echo "== Starting run at $(date)"
echo "== Job ID: ${SLURM_JOBID}"
echo "== Node list: ${SLURM_NODELIST}"
echo "== Submit dir: ${SLURM_SUBMIT_DIR}"
echo "== Scratch dir: ${TMPDIR}"

source miniconda/bin/activate
conda activate ./relik_env
python Relik_test.py

