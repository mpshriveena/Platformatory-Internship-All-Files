docker run node
docker ps # only running processes
docker ps -a # all processes
docker run -it node

# Basic Structure
FROM node # first step
WORKDIR /app
COPY . .
[or]
COPY . /app
RUN npm install
EXPOSE 80
CMD ["node", "server.js"] # Last step [cmd won't be done at the time of image creation]

# Building image and running container
docker build .
docker run image_id
docker stop container_name
docker run -p 3000:80 image_id # publish [very necessary] # runs deault in attach mode

# Optimized Structure
FROM node
WORKDIR /app
COPY package.json /app
RUN npm install
COPY . /app
EXPOSE 80
CMD ["node", "server.js"]

docker COMMAND --help
docker run -a 8000:80 image_id # Attach mode 
docker run -d 8000:80 image_id # Detach mode
docker attach container_name # If you want to attach an already detached container
docker logs container_name
docker logs -f container_name # To keep on listening

#-i --> interactive -t--> exposes a terminal
docker run -it image_id
docker start container_name # Restart already created container
docker start -a -i container_name

docker rm container_name

sudo docker exec -u root -it kafka-1 /bin/bash
sudo docker exec -u root -it kafka-2 /bin/bash
sudo docker exec -u root -it kafka-3 /bin/bash

docker-compose up --build

sudo docker exec -u root -it kafka1 /bin/bash
sudo docker exec -u root -it kafka2 /bin/bash
sudo docker exec -u root -it kafka3 /bin/bash
sudo docker exec -u root -it kfkclient /bin/bash

docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container_id_or_name>