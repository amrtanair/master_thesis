#!/bin/bash
echo "This script installs OIE2016 dataset. `QASRL-full` folder must be present in the current folder"
echo "Cloning ..."
git clone https://github.com/gabrielStanovsky/supervised-oie.git
git clone https://github.com/gabrielStanovsky/oie-benchmark.git
rm -rf oie-benchmark/QASRL-full
mv QASRL-full oie-benchmark/
cd oie-benchmark/
pip install -r requirements.txt
./create_oie_corpus.sh
echo "Installation complete !"
