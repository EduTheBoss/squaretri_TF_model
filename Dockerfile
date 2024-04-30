FROM python
COPY . /squaretri_TF_model
WORKDIR /squaretri_TF_model
RUN pip install -r requirements.txt
CMD ["python", "backend.py"]