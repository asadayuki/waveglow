## About the project

- This repository is for the couse work of [CS396/496: Deep Learning For Practitioners @ NU](https://pseeth.github.io/deep-learning-for-practitioners/)

- In the course, we read the paper of "Waveglow" and reproduced the result in the paper.

- Details of our project is in [waveglow project](https://github.com/asadayuki/waveglow/blob/master/doc/plan.md)

## How to use the code

### Create an environment with python = 3.6

```
conda create -n [name of environment] python=3.6 
conda activate [name of environment]
```

### Download code

```
git clone https://github.com/asadayuki/waveglow.git
git clone https://github.com/NVIDIA/apex
```

### Set up sub-modules 

```
cd waveglow
git submodule add http://github.com/NVIDIA/tacotron2 src/tacotron2
git submodule update
```

### Install libraries

```
pip install -r requirements.txt
```

### Set up apex

```
cd ../apex
pip install -v --no-cache-dir ./
```

### Prepare data for demo ( This uses public speech data called "LJSpeech-1.1") 

```
cd ../waveglow/experiments
sh prepare_data.sh
```

### Prepare a config file for demo (Manually edit a file)

- Open ../data/LJSpeech-1.1/config.json
- Modify "checkpoints" ("train_config" > "output_directory") to "../data/LJSpeech-1.1/checkpoints"
- Modify "train_files.txt" ("data_config" > "training_files") to "../data/LJSpeech-1.1/train_files.txt",

### Train 

```
cd ../src
python train.py -c ../data/LJSpeech-1.1/config.json
```

### Inference (This needs to be done after all the steps above)

try running notebook/demo.ipynb



