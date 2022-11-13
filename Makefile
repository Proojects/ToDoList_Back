install:
	pip install -r requirements.txt

lint:
	flake8 to_do_list/

run:
	python manage.py run
