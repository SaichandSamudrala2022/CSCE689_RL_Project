Install conda with python 3.8 version

conda create --name DRL_GR_python3.8 python=3.8.10

conda activate DRL_GR_python3.8

pip install -r ./requirements.txt

OR if the above does not work:
  Install stable-baseline3, gym, pytorch,scipy, and sb3-contrib whose versions are mentioned in the requirements.txt.

Run following commands in the terminal for the respective algorithm:
python GenSolEvalComp_Pipeline.py --RL_algo PPO

python GenSolEvalComp_Pipeline.py --RL_algo A2C

python GenSolEvalComp_Pipeline.py --RL_algo TRPO

If the above command fails in a machine with less than 10 cores, take a look at line 61-63 in GenSolEvalComp_Pipeline.py and make the change mentioned there

Generate training logs in ./logs/ folder

run "python reward_plotter.py" to generate the reward plot we have in the paper
