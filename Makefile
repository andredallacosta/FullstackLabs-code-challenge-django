create_env:
		virtualenv -p python3 env

activate_env:
		bash -c "source env/bin/activate"

install_requirements:
		pip install -r requirements.txt

freeze_requirements:
		pip freeze > requirements.txt

run:
		docker-compose up

migrate:
		docker-compose run web python3 manage.py makemigrations
		docker-compose run web python3 manage.py migrate
