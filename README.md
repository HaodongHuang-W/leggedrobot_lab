# leggedrobot_lab

leggedrobot_lab is an extension project based on the IsaacLab framework. 

TODO:
- [x] Unitree G1 Training
- [x] Unitree Go2 Training



## Get Ready

You need to install `Isaac Lab`.

## Installation

Using a python interpreter that has Isaac Lab installed, install the library

```bash
python -m pip install -e ./exts/leggedrobot_lab
```

## Try examples

Unitree Go2 Flat

```bash
# Train
python scripts/rsl_rl/train.py --task Isaac-Velocity-Flat-Unitree-Go2-v0 --headless
# Play
python scripts/rsl_rl/play.py --task Isaac-Velocity-Flat-Unitree-Go2-Play-v0
```

Unitree Go2 Rough

```bash
# Train
python scripts/rsl_rl/train.py --task Isaac-Velocity-Rough-Unitree-Go2-v0 --headless
# Play
python scripts/rsl_rl/play.py --task Isaac-Velocity-Rough-Unitree-Go2-Play-v0
```



## Code Contribution
The code was written with reference to [fan-ziqi](https://github.com/fan-ziqi/robot_lab).I would also like to thank [Jiaming Hu](https://jih189.github.io/isaaclab_project) for his guidance on the code.

