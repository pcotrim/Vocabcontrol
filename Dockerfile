# Base Image
FROM python:3.8-slim

# Work directory
WORKDIR /workspace

# Copy requirements and install dependencies
# COPY requirements.txt requirements.txt
COPY . .
RUN pip install virtualenv
RUN python -m venv venv
RUN . venv/bin/activate
RUN pip install --upgrade pip

# RUN set -eux; \
RUN pip install rasa spacy dataparser gunicorn Flask requests flask_cors
# RUN mkdir -p tesauro
RUN cd tesauro
RUN pip3 install -r requirements.txt

# Copy other project files
# COPY . .

# Expose a port to Containers
EXPOSE 333-10100

# Install Supervisor
RUN pip install supervisor

RUN sudo ufw allow 333/tcp
# Copy Supervisor configuration file
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Run supervisord
# RUN cd tesauro && rasa run --enable-api -m ./models/20240103-220920-ivory-loop.tar.gz --cors "*"
# CMD ["rasa", "run", "--enable-api", "-m", "./models/20240103-220920-ivory-loop.tar.gz", "-p", "10001"]
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
# CMD ["gunicorn", "chatbot:app"]