pipeline {
    agent any
    
    environment{
        DOCKER_IMAGE = "joelpaul18/devops-app"
        IMAGE_TAG = "${env.BUILD_ID}"
    }
    
    stages {
        stage('checkout') {
            steps {
                checkout scm
            }
        }
    }
    
    stages {
        stage('Test') {
            steps {
                '''
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                pytest -v
                '''
            }
        }
    }
    
    stages {
        stage('Build & Push') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'docker-hub-credentials') {
                        def customImage = docker.build("${DOCKER_IMAGE}:${IMAGE_TAG}")
                        customImage.push()
                    }
                }
            }
        }
    }
}

