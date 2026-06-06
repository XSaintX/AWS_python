# Users API — AWS Lambda + PostgreSQL + FastAPI


Serverless REST API for managing users, built with **AWS SAM**, **Python**, and **PostgreSQL** (RDS). The Lambda function exposes HTTP endpoints behind API Gateway and reads user data from a `usuarios` table via SQLAlchemy. <br />
Is part of an online course about AWS, the project is still building but contains the basis of a project with AWS. <br />
The course was done with python 3.9, I modified to python 3.13 without environment so it was totally different from the original one.
## Features
- `GET /users` — list all users (`id`, `name`, `surname`, `city`)
- `POST /users` — create a user *(in progress)*
- CORS enabled for browser clients
- PostgreSQL connection via environment variables
## Tech stack
| Layer        | Technology                          |
|-------------|--------------------------------------|
| Runtime     | Python 3.9 (Docker) / 3.13 (SAM)    |
| IaC         | AWS SAM                             |
| Compute     | AWS Lambda                          |
| API         | API Gateway                         |
| Database    | PostgreSQL (RDS)                    |
| ORM         | SQLAlchemy + psycopg2               |
## Project structure
. ├── Dockerfile # Container image for Lambda ├── samconfig.toml # SAM deploy settings └── modules/ └── users/ ├── app.py # Lambda handler (API routes) ├── requirements.txt ├── config/ │ └── config.py # DB settings from env vars └── db/ └── database.py # SQLAlchemy connection & queries


## Prerequisites
- [AWS CLI](https://aws.amazon.com/cli/) configured with a profile that can deploy Lambda
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
- [Docker](https://www.docker.com/) (for container-based builds)
- A PostgreSQL database with a `usuarios` table
## Environment variables
| Variable           | Description              |
|--------------------|--------------------------|
| `POSTGRES_HOST`    | RDS hostname             |
| `POSTGRES_PORT`    | Port (default: `5432`)   |
| `POSTGRES_USER`    | Database user            |
| `POSTGRES_PASSWORD`| Database password        |
| `POSTGRES_DB`      | Database name            |
