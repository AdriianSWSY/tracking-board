FROM python:3

WORKDIR /usr/src/backend

COPY poetry.lock .
COPY pyproject.toml .
COPY entrypoint.sh .

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
RUN chmod +x entrypoint.sh

COPY . .

ENTRYPOINT ["bash", "/usr/src/backend/entrypoint.sh"]