pip freeze
pip install -r ./main/src/requirements.txt
python ./main/src/manage.py migrate
start http://localhost:8000
python ./main/src/manage.py runserver
