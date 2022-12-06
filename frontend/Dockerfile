# frontent/Dockerfile

FROM python:3.10-slim

EXPOSE 8501

WORKDIR /myapp

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]


# RUN pip install --upgrade pip

# RUN pip install -r requirements.txt

# COPY . /myapp

# ENTRYPOINT ["streamlit","run"]
# CMD ["/app.py"]
