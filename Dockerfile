FROM python:3.11
WORKDIR /Fetch
COPY . /Fetch
EXPOSE 8501
RUN pip install -r requirements.txt
CMD [ "streamlit","run", "app.py"]