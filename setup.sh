# Contains all the commands used for setup for posterity
# First you need to download and install python3.5.2
conda install virtualenv
virtualenv venv --no-site-packages
source venv/bin/activate
# For CPU
export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-0.11.0-py3-none-any.whl
pip install --upgrade $TF_BINARY_URL
pip install -r requirements.txt


echo "Now download save.zip from https://worksheets.codalab.org/bundles/0xbe46c9b116fa443fb5cb743ab9fa4104/"
echo "Download glove vectors from https://worksheets.codalab.org/bundles/0x15a09c8f74f94a20bec0b68a2e6703b3/"

mkdir bi-att-flow/data
mkdir bi-att-flow/data/squad
wget https://github.com/allenai/bi-att-flow/blob/demo/data/squad/shared_test.json bi-att-flow/data/squad
