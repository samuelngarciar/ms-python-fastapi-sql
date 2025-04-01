# ms-python-fastapi-sql
Model project for teach concepts

This is a microservice that allow show you the best practices respect desing, implementation and access to database considerating the follows aspects:

1. Distribution reponsability in layers (models, repositories, services and api)
2. Tecnology stack
   - FastAPI: Helps you create web APIs quickly and easily.
   - Uvicorn: Runs your FastAPI app fast.
   - SQLAlchemy: Lets you work with databases and ORM using Python.
   - pyodbc: Connects Python to different databases.
3. Access to MS SQL Server 2019
3. Health check operation
   
## Setup and test
### 1. Start up database MSSQL on docker
docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=YourPassword01-' -p 1433:1433 --name sqlserver4 -d mcr.microsoft.com/mssql/server:2019-latest image
![image](https://github.com/user-attachments/assets/dbea9d26-237f-44c9-b764-037f4eb53b2b)




