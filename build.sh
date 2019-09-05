docker build -t my-flask -f Dockerfile-flask .
docker build -t my-nginx -f Dockerfile-nginx .
docker network create app-network
docker run -d --name flask --net app-network -v "./:/app" app-flask
docker run -d --name nginx --net app-network -p "5000:80" app-nginx