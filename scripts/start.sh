docker build -t minufrontend .
yarn build:production
docker run -it -p 8080:80 minufrontend