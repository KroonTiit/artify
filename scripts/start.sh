#!/bin/sh
set -e
npm run build
echo open the browser on localhost:3000
docker-compose up