FROM python:3.14-slim

WORKDIR /app
RUN mkdir -p /app/data

COPY auditor.py .
COPY modular_auditor.py .
COPY persistent_auditor.py .

VOLUME ["/app/data"]

CMD ["python", "persistent_auditor.py"]