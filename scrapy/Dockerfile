FROM alpine:latest

# Installing client libraries and any other package you need
RUN apk update && apk add libpq

# Installing build dependencies
RUN apk add --virtual .build-deps gcc python-dev musl-dev postgresql-dev


RUN apk -U add \
        gcc \
        libgcc \
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
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev
RUN apk add gcc gfortran python python-dev py-pip build-base wget freetype-dev libpng-dev openblas-dev 

RUN ln -s /usr/include/locale.h /usr/include/xlocale.h

# Data analysis libs
RUN pip install numpy 
RUN pip install scikit-learn pandas matplotlib wordcloud 

# Connect to postgresql
RUN pip install psycopg2

# Delete build dependencies
RUN apk del .build-deps

WORKDIR /runtime/app

COPY entrypoint.sh /runtime/entrypoint.sh
RUN chmod +x /runtime/entrypoint.sh

ENTRYPOINT ["/runtime/entrypoint.sh"]
CMD ["scrapy"]