FROM python:3.11.1-slim-bullseye

WORKDIR /pokemon_translation
COPY . /pokemon_translation
RUN pip3 install -r requirements.txt

EXPOSE 5000
CMD python pokemon_translation/app.py --update --port 5000
