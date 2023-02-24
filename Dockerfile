FROM python

RUN apt -y update

RUN apt -y install

WORKDIR /tmp/install

COPY . .

RUN python -m pip install --upgrade pip

RUN pip install poetry autopep8 pytest

RUN autopep8 src/ tests/

RUN poetry install

RUN poetry run pytest

RUN poetry build

RUN pip install dist/*.whl

WORKDIR / 

ENTRYPOINT [ "ircd" ]
