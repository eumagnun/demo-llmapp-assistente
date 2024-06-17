#Base Image to use
FROM python:3.9

ENV STREAMLIT_SERVER_ENABLE_STATIC_SERVING=true

EXPOSE 8080
WORKDIR /app
COPY . ./

#install all requirements in requirements.txt
RUN pip install -r requirements.txt

# Run the web service on container startup
CMD ["streamlit", "run", "app.py", "--server.port=8080"]
