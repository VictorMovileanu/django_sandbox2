# Personal cheat sheet

## Setup

### Local requirements
```
sudo apt-get update
sudo apt-get -y install python3-pip
pip3 install virtualenv
```
### Set up environment
```bash
git clone https://github.com/ViggieSmalls/django_sandbox
cd django_sandbox
virtualenv venv --python=python3.6
source venv/bin/activate
```

### Set up local development server
These commands are all run in the virtual environment
```bash
pip install -r requirements.txt
python manage.py migrate
```

### Pip helpers
Uninstall all pip packages
```
pip freeze | xargs pip uninstall -y
```
