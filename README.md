## How to use

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

git submodule init

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

### Prepare data

```
cd ../waveglow/experiments

sh prepare_data.sh
```

### Prepare a config file (Manually edit a file)

- Open config.json in waveglow/data/LJSpeech-1.1/config.json

- Modify "checkpoints" ("train_config" > "output_directory") to "../data/LJSpeech-1.1/checkpoints"

- Modify "train_files.txt" ("data_config" > "training_files") to "../data/LJSpeech-1.1/train_files.txt",

### Train 

```
cd ../src

python train.py -c ../data/LJSpeech-1.1/config.json
```




