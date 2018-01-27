FROM postgres:10

RUN mkdir /backup
ADD ./restore_db.sh /backup
ADD ./timezones_project_db.gz /backup

RUN cp /backup/restore_db.sh /docker-entrypoint-initdb.d/
