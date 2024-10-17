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
                git url: 'https://github.com/your-username/your-repo.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${DOCKER_IMAGE_NAME}:${env.BUILD_ID}")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry("${REGISTRY_URL}", "${DOCKER_CREDENTIALS_ID}") {
                        dockerImage.push()
                    }
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
