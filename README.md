
# Subject-matter-graph-builder

A FastAPI Microservice that can build/update Knowledge Graphs based on the website content fed along with the power of Large Language Models (LLMs).


## OverView:

 This is the complete overview of the System.
 
## Contents

1. API endpoints Info
2. Setup & Usage
3. Request-Response Structure
## 1. API Endpoints Info

a. `/content/process-content` : this endpoint takes in the url of the website and generates Graph Data that can be parsed programmatically.

b. `/graph/build-graph` : this endpoint does same as that of `/content/process-content` along with Graph Operations from the generated data.

c. `/graph/update-graph` : this endpoint Updates the graph Database given Nodes and Edges.


## 2. Setup & Usage

```bash
# start docker desktop application, open a terminal/command prompt and navigate to this project and enter the following

# 1. Running Unit tests:

$ docker-compose -f docker-compose.unit-test.yml build unit-test

$ docker-compose -f docker-compose.unit-test.yml run unit-test

# 2. Running Integration tests:

$ docker-compose -f docker-compose.integration-test.yml build integration-test

$ docker-compose -f docker-compose.integration-test.yml run integration-test

# 3. Running the System:

$  docker-compose build

$  docker-compose up

```
## 3. Request-Response Structure

   Kindly check the file 'src/datamodels/models.py'