FROM python:3.12.3-slim-bullseye


WORKDIR .
COPY . .

RUN pip install --upgrade setuptools
RUN pip install -r  requirements.txt
EXPOSE 8000

CMD ["sh", "-c", "alembic -c alembic.ini upgrade head && uvicorn main:app --host 0.0.0.0 --port 8000"]
