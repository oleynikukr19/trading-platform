## Prerequisites

To be able to run the server and execute the tests Docker should be installed.

Download and install\
https://docs.docker.com/get-docker/

Clone the project locally\
```git clone https://github.com/Alfresco/acs-deployment.git```

Change directory to the project folder\
```cd <project directory>```

## Run the server

Change directory to the project folder\
```cd <project directory>```

Build Docker Image\
```docker build -t trading-platform -f server/Dockerfile . ```

Run Docker Container\
```docker run -d -p 8000:8000 trading-platform```

Base URL will be:\
```localhost:8000```

To execute requests to the server, please refer to the documentation (trading-platform/openapi_doc.yml)

## Run the tests

Change directory to the project folder\
```cd <project directory>```

Build Docker Image\
```docker build -t trading-platform-testing -f tests/Dockerfile . ```

Run tests\
```docker run --rm -v ${PWD}/tests:/usr/src/app/tests my_test_image```

HTML report after execution will be available at ```${PWD}/tests```\
If you need to redirect it to different location, change this path.


