FROM python:3.9

RUN apt-get update -y
RUN apt-get install libsasl2-dev python-dev libldap2-dev libssl-dev -y

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# ENTRYPOINT python odoo-bin -d ${DB_NAME} -i base --addons-path=${ADDONS_PATH} --db_host=${DB_HOST} --db_user=${DB_USER} --db_password=${DB_PASSWORD} --without-demo=all
ENTRYPOINT python odoo-bin -d ${DB_NAME} --addons-path=${ADDONS_PATH} --without-demo=all --db_host=${DB_HOST} --db_user=${DB_USER} --db_password=${DB_PASSWORD}