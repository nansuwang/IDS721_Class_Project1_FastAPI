# use conda to forge the dependencies
FROM public.ecr.aws/lambda/python:3.8
FROM continuumio/miniconda3:4.10.3-alpine

# make the dir
RUN mkdir -p /app

# copy files
COPY app.py /app/
COPY main.py /app/
COPY Makefile /app/
COPY predictors.py /app/
COPY test_app.py /app/
COPY regression_model.pkl /app/

# install all packages
RUN conda install --yes --freeze-installed -c conda-forge \
    pandas==1.3.2 \
    numpy==1.21.2 \
    boto3 \
    python-json-logger \
    scipy==1.7.1 \
    sklearn \
    matplotlib==3.4.3 \
    fastapi==0.68.1 \
    pylint==2.10.2 \
    uvicorn==0.15.0 \
    gunicorn==19.9.0 \
    uvloop==0.16.0 \
    httptools==0.3.0 \
    pydantic==1.8.2 \
    mangum==0.12.2 \
    pytest \
    black \
    requests \
    pickle \
    && conda clean -afy

# set working dir
WORKDIR /app

# expose to ports
EXPOSE 80
EXPOSE 8080

# entry point
ENTRYPOINT [ "python" ]
CMD [ "/app/app.py" ]