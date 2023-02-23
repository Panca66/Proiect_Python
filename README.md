# Anca
git clone https://github.com/Panca66/Proiect_Python
cd Proiect_Python/
python -m venv virtual
source virtual/Scripts/activate
pip install flask
pip install flask-sqlalchemy
export FLASK_APP = app.py
flask db init
flask db update
flask run
