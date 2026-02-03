FROM public.ecr.aws/docker/library/python:3.13.11-alpine
WORKDIR /usr/src/app
EXPOSE 8080
COPY . .
RUN python3 -m pip install --upgrade pip setuptools && \
    python3 -m pip install . pytest requests && \
    python3 -m pip cache purge
CMD ["python3", "./server.py"]
