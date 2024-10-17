pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS_ID = 'dockerhub'
        DOCKER_IMAGE_NAME = 'shashidharabc/multibranch-sample-app'
        REGISTRY_URL = 'https://index.docker.io/v1/'
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/ShashidharBC/multibranch-sample-app.git', branch: 'main'
            }
        }

        stage('Check Docker') {
            steps {
                sh 'docker --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${DOCKER_IMAGE_NAME}:${env.BUILD_ID}")
                    echo "Docker image ${DOCKER_IMAGE_NAME}:${env.BUILD_ID} built successfully."
                }
            }
        }

        stage('Print Environment Variables') {
            steps {
                script {
                    echo "DOCKER_CREDENTIALS_ID: ${DOCKER_CREDENTIALS_ID}"
                    echo "DOCKER_IMAGE_NAME: ${DOCKER_IMAGE_NAME}"
                    echo "REGISTRY_URL: ${REGISTRY_URL}"
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    echo "Attempting to push the Docker image..."
                    docker.withRegistry("${REGISTRY_URL}", "${DOCKER_CREDENTIALS_ID}") {
                        dockerImage.push()
                    }
                    echo "Docker image pushed to Docker Hub successfully."
                }
            }
        }

        stage('Cleanup') {
            steps {
                script {
                    dockerImage.inside {
                        sh 'docker rmi ${DOCKER_IMAGE_NAME}:${env.BUILD_ID}'
                    }
                }
            }
        }
    }
}
