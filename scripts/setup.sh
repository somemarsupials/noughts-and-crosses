echo "creating virtual environment..."
python3 -m venv .venv --prompt xo

echo "sourcing environment..."
source .venv/bin/activate

echo "installing dependencies..."
pip3 install -r requirements.txt
