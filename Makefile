create_env:
		virtualenv -p python3 env

activate_env:
		bash -c "source env/bin/activate"

install_requirements:
		pip install -r requirements.txt

freeze_requirements:
		pip freeze > requirements.txt

run:
		python3 manage.py runserver

migrate:
		python3 manage.py makemigrations
		python3 manage.py migrate
