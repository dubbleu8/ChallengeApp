# Usa un'immagine base di Python
FROM python:3.9-slim

# Imposta la directory di lavoro all'interno del container
WORKDIR /app

# Copia il file requirements.txt nel container
COPY requirements.txt requirements.txt

# Installa le dipendenze
RUN pip install -r requirements.txt

# Copia il resto dell'applicazione nel container
COPY . .

# Espone la porta su cui gira l'app Flask
EXPOSE 5000

# Definisce il comando per eseguire l'applicazione
CMD ["python", "app.py"]
