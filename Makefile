.PHONY: run clean test coverage reload

# run the django web server
run:
	./manage.py runserver 0.0.0.0:8000

# remove pyc junk
clean:
	find -iname "*.pyc" -delete
	find -iname "__pycache__" -delete
