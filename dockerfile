FROM python:3.14-slim

WORKDIR /app

COPY auditor.py .
COPY modular_auditor.py .

CMD ["python", "modular_auditor.py"]