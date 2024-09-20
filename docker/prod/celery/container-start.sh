#!/bin/sh
cd /code && \
celery -A ticketless worker --beat --loglevel=debug