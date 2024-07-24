# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install required packages
pip install -r requirements.txt

# Run the main analysis script (replace 'main.py' with your actual script name)
python scrape.py