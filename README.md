## About the project

- This repository is for the couse work of [CS396/496: Deep Learning For Practitioners @ NU](https://pseeth.github.io/deep-learning-for-practitioners/)

- In the course, we read the paper of "Waveglow" and reproduced the result in the paper.

- Details of our project is in [waveglow project](https://github.com/asadayuki/waveglow/blob/master/doc/plan.md)

## Reproduction result

![graph](https://user-images.githubusercontent.com/55772141/83953931-46409b80-a80a-11ea-923c-5a3e41c9938f.png)

- 166 epochs - 181721 execution of mini bacthes (Training took about 4 days...)

- Envrionment

  - CPU : Intel(R) Xeon(R) Silver 4215 CPU @ 2.50GHz
  
  - GPU : GV100 [TITAN V] 
 
- Result 

  1. [original](https://drive.google.com/file/d/1hMlXP0V5-E8PsMyfvQ5sF-bsWLRVj7f6/view?usp=sharing), [reproduction result](https://drive.google.com/file/d/1NoVsutyB6uyyPNd2yvmqY8INlXLwRbUL/view?usp=sharing)

  2. [original](https://drive.google.com/file/d/1Rskr5KBvRn831sCUEMVNflkOOEvkMmjd/view?usp=sharing), [reproduction result](https://drive.google.com/file/d/1p7WGOqZbpxsUIV35A5sEzs2Eibf6Sc-5/view?usp=sharing)

  3. [original](https://drive.google.com/file/d/1aOUheoV7kDxyIf_vR_qduTdSfI7qtbqZ/view?usp=sharing), [reproduction result](https://drive.google.com/file/d/1yRIZLrB5AK20bI391oV4Se7OPb24ytcq/view?usp=sharing)

  4. [original](https://drive.google.com/file/d/1Ni4moSc077QcetjQrrZdfjb-YIm_fSQD/view?usp=sharing), [reproduction result](https://drive.google.com/file/d/1UyDfF5pZwraYpsDZcu0yYnAY23Zsxgqq/view?usp=sharing)

  5. [original](https://drive.google.com/file/d/1EqtIIw94fidh9WeMHgHvpgK_fcv3_8GI/view?usp=sharing), [reproduction result](https://drive.google.com/file/d/1a6tpZZ1ngwh7Qg0c-fZyXY0DQxslCwtX/view?usp=sharing)

  6. [original](https://drive.google.com/file/d/12cc603VZT6WDVOMMPp4C2TSHCEJoYdjD/view?usp=sharing), [reproduction result](https://drive.google.com/file/d/1AQAvZeGdvlhzy37sFIu_8_xKVAkAseP3/view?usp=sharing)

  7. [original](https://drive.google.com/file/d/16FYNkIBrX2zqP4lvTMU0vxYNSCF71cpR/view?usp=sharing), [reproduction result](https://drive.google.com/file/d/1gDILSFyS_zklq53bOEgqFczEmVCtYUas/view?usp=sharing)

  8. [original](https://drive.google.com/file/d/10SoMo8gbHxHfBuLq9xJr7APMJFLFM9hr/view?usp=sharing), [reproduction result](https://drive.google.com/file/d/1P7tXxoCVljoX9JaVQJ_SBOR4JaFm7aGC/view?usp=sharing)

  9. [original](https://drive.google.com/file/d/1rT6HhLPNfi0z3fA_8ABQ0cO82SjlLx3M/view?usp=sharing), [reproduction result](https://drive.google.com/file/d/1oPqZkUXDHdseLNqZ6XvFp4ywnl5uCjOH/view?usp=sharing)

  10. [original](https://drive.google.com/file/d/15DLRpDomHXSj0mED-UsuQNNj7tcuR5ID/view?usp=sharing), [reproduction result](https://drive.google.com/file/d/1ZeWP06vqS2wf8FcKjTdTT8917jXzv5cO/view?usp=sharing)

- [Trained model]()


## tips & tricks to run the code

- To run the code, GPU-enabled environment is necessary.

- When using different audio data as training dataset, make sure the mel-spectrogram looks right using demo.ipynb.  I tried using the audio files re-sampled using "librosa.output.write_wav".  But Waveglow program didn't load it properly, but didn't show any errors.  I didn't notice it until I display the mel-spectrogram using demo.ipynb...  So I re-created the dataset using "scipy.io.wavfile.write"

- When you run the code for the different dataset, don't forget to check the sampling rate of the dataset.  Then modify config.json and pass the sampling rate with "--sampling_rate XXXXX" to evaluate.py.

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



