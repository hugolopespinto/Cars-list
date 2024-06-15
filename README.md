# 3-Tier Application Setup

## Prerequisites

- install Docker

## Quick Start

1. Clone the repository and install the project:

   git clone git@github.com:hugolopespinto/Cars-list.git
   cd Cars-list
   cd .\client\
   npm install
   docker-compose up --build
   cd ..
   cd nodejs-service
   npm install
   cd ..
   docker-compose up --build

2. Troubleshooting

   If the Python server encounters issues connecting to the database, follow these steps:
   Navigate to the root directory of the project
   Restart the Python service container:
      ```docker restart hyperspace-python```

3. command-line python

    To execute the following commands, run the following
    commands in the terminal:
  
    ```docker exec -it hyperspace-python python manage.py {command} {args}```
  
   ex1: ```docker exec -it hyperspace-python python manage.py clear_db```

   ex2: ```docker exec -it hyperspace-python python manage.py create_db```

   ex3: ```docker exec -it hyperspace-python python manage.py create_item "McLaren F1 LM"```


## urls

- python : http://localhost:5001/elements (get elements from python)
- nodejs : http://localhost:3001/elements (get elements from nodejs)
- react-app : http://localhost:3000/ (access to web app)
