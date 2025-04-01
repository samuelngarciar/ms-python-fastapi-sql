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
docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=YourPassword01-' -p 1433:1433 --name sqlserver -d mcr.microsoft.com/mssql/server:2019-latest
![image](https://github.com/user-attachments/assets/dbea9d26-237f-44c9-b764-037f4eb53b2b)

### 2. Check the container is running up ok
docker ps
![image](https://github.com/user-attachments/assets/b6ed1a43-51e2-4b0a-84c0-18f5041e2808)

### 3. Clone this repository and build the image docker
docker build --no-cache -t ms-python-fastapi-sql .
![image](https://github.com/user-attachments/assets/6d7f9ef4-01f3-40d2-92f9-9c1e5685bcf0)

### 4. Check the image generated
docker images
![image](https://github.com/user-attachments/assets/9972a803-aac9-4615-8d36-fc1948464fc6)

### 5. Start up the container
docker run --net=host -p 5000:5000 --name service ms-python-fastapi-sql
![image](https://github.com/user-attachments/assets/6e74d734-0129-4d25-8b78-46b95e2d260c)

In other terminal session execute the follows test

## Tests
### Test 1, Request the sysobjects table and check time consumed
time curl -v "http://localhost:5000/sysobjects?limit=5&offset=10"
![image](https://github.com/user-attachments/assets/616241c1-f41a-41a3-81a8-acd68fdf07bf)


### Test 2, Request the microservice health check
time curl -v "http://localhost:5000/health"
![image](https://github.com/user-attachments/assets/1cb9ecde-c6e3-4aba-abc3-c966b65567f8)













