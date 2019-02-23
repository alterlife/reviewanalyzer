FROM alpine:latest

# Installing client libraries and any other package you need
RUN apk update && apk add libpq

# Installing build dependencies
RUN apk add --virtual .build-deps gcc python-dev musl-dev postgresql-dev


RUN apk -U add \
        gcc \
        libffi-dev \
        libxml2-dev \
        libxslt-dev \
        musl-dev \
        openssl-dev \
        python-dev \
        py-imaging \
        py-pip \
        curl ca-certificates \
    && update-ca-certificates \
    && rm -rf /var/cache/apk/* \
    && pip install --upgrade pip \
    && pip install Scrapy


# Installing and build python module
RUN pip install psycopg2

# Delete build dependencies
RUN apk del .build-deps

WORKDIR /runtime/app

COPY entrypoint.sh /runtime/entrypoint.sh
RUN chmod +x /runtime/entrypoint.sh

ENTRYPOINT ["/runtime/entrypoint.sh"]
CMD ["scrapy"]