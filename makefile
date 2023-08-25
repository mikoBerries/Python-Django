server:
	./myDjangoProject/manage.py runserver

migration:
	py ./myDjangoProject/manage.py makemigrations

migrate:
	py ./myDjangoProject/manage.py migrate

shell:
	py ./myDjangoProject/manage.py shell


.phony: server migration migrate shell
