# Brief-PME

## Liste des commandes utilisées

### Docker
Supprime les anciens conteneurs et volumes
Reconstruit et relance les services  

```
docker-compose down -v  
docker-compose up --build
```
Pour tester Docker dans Powershell
```
docker info
```

Ouvrir la bdd dans le terminal : 

```
docker exec -it database sh
sqlite3 /data/database.db
.tables
```

Copier le ficheir db sur le pc
```
docker cp database:/data/database.db .
```