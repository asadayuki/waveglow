#!/bin/sh

echo 'downloading data'
mkdir ../data
wget https://data.keithito.com/data/speech/LJSpeech-1.1.tar.bz2 -O ../data/LJSpeech-1.1.tar.bz2
echo 'downloaded'

echo 'unzipping data'
tar -jxvf ../data/LJSpeech-1.1.tar.bz2 -C ../data/
rm ../data/LJSpeech-1.1.tar.bz2
mkdir ../data/LJSpeech-1.1/mels
mkdir ../data/LJSpeech-1.1/result
echo 'unzipped'

echo 'create file list'
ls ../data/LJSpeech-1.1/wavs/*.wav | tail -n+10 > ../data/LJSpeech-1.1/train_files.txt 
ls ../data/LJSpeech-1.1/wavs/*.wav | head -n10 > ../data/LJSpeech-1.1/test_files.txt

echo 'copy config.json'
cp ../src/config.json ../data/LJSpeech-1.1/

