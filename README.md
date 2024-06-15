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


## urls

- python : http://localhost:5001/elements (get elements from python)
- nodejs : http://localhost:3001/elements (get elements from nodejs)
- react-app : http://localhost:3000/ (access to web app)
