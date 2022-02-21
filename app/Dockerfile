FROM jaredhanson11/serverbase

# Install required packages
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache -r requirements.txt \
    && rm requirements.txt

# Copy server code to the /app/ dir
COPY ./entrypoint.sh /
COPY ./app.py ./
