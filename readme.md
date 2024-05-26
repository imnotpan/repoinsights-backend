Ejecución en local

docker swarm init
docker network create --driver overlay --attachable repoinsight_network

-- Para restaurar .tar se debe en dbveaver presionar CREATE DATABASE, y restaurar base de datos
-- No debe haberse generado esquemas ni nada de esta.

METABASE

se debe ejecutar
docker-compose -f docker-compose.local.yml up -d metabase-db

restaurar la base de datos

y luego
docker-compose -f docker-compose.local.yml up -d
para el resto de los servicios

usuario: matias.barra64@gmail.com
pass: vps228.2o22
