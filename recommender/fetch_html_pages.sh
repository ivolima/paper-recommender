#!/bin/bash
# a basic crawler in bash
# usage: fetch_html_pages.sh urlfile.txt <numprocs>
URLS_FILE=$1
CRAWLERS=$2

mkdir -p data/pages

WGET_CMD="wget \
  --tries=5 \
  --dns-timeout=30 \
  --connect-timeout=5 \
  --read-timeout=5 \
  --directory-prefix=data/pages \
  --wait=2 \
  --random-wait \
  --no-parent \
  --no-verbose \
  --reject *.jpg --reject *.gif \
  --reject *.png --reject *.css \
  --reject *.pdf --reject *.bz2 \
  --reject *.gz  --reject *.zip \
  --reject *.mov --reject *.fla \
  --reject *.xml \
  --no-check-certificate"

cat $URLS_FILE | xargs  -P $CRAWLERS -I _URL_ $WGET_CMD _URL_
