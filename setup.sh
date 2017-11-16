# Contains all the commands used for setup for posterity

conda install virtualenv
virtualenv venv --no-site-packages
source venv/bin/activate
pip install -r requirements.txt
echo "Now download save.zip from https://worksheets.codalab.org/bundles/0xbe46c9b116fa443fb5cb743ab9fa4104/"
echo "Download glove vectors from https://worksheets.codalab.org/bundles/0x15a09c8f74f94a20bec0b68a2e6703b3/"
