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
COPY requirements.txt /app/

# install all packages
RUN pip install -r requirements.txt

# set working dir
WORKDIR /app

# expose to ports
EXPOSE 80
EXPOSE 8080

# entry point
ENTRYPOINT [ "python" ]
CMD [ "/app/app.py" ]