
pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "joelpaul18/devops-app"
        IMAGE_TAG = "${BUILD_ID}"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    pytest -v
                '''
            }
        }

        stage('Build & Push') {
            steps {
                script {
                    docker.withRegistry(
                        'https://index.docker.io/v1/',
                        'docker-hub-credentials'
                    ) {
                        def customImage = docker.build(
                            "${DOCKER_IMAGE}:${IMAGE_TAG}"
                        )

                        customImage.push()
                    }
                }
            }
        }
    }
}
