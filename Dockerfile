FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy your Python script into the container
COPY deploy/kcc-master/ /app/kcc/
COPY deploy/kindlegen /app/
COPY deploy/index.py /app/
COPY deploy/base_options.json /app/options.json

RUN mkdir input
#Installing KindleGen
RUN mv kindlegen /usr/local/bin/

# Install any necessary dependencies (if your script requires any)
# Define the command to run your Python script
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

#Installing 7zip
RUN apt-get install -y p7zip-full

#Intalling mozjpeg
RUN apt-get update && apt-get -y install cmake protobuf-compiler
RUN pip install  --use-pep517 mozjpeg-lossless-optimization>=1.1.2

#installing requirements
RUN pip install -r /app/kcc/requirements.txt

# CMD python ./kcc/kcc-c2e.py -p K1 ./input/input.zip
CMD python index.py
