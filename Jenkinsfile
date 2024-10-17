pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS_ID = 'dockerhub' // Use your configured credentials ID
        DOCKER_IMAGE_NAME = '9108205512/multibranch-sample-app'
        REGISTRY_URL = '' // Leave this empty for Docker Hub
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
                    // Build the Docker image
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
                    try {
                        echo "Attempting to push the Docker image ${DOCKER_IMAGE_NAME}:${env.BUILD_ID}..."
                        docker.withRegistry("${REGISTRY_URL}", "${DOCKER_CREDENTIALS_ID}") {
                            dockerImage.push()
                        }
                        echo "Docker image ${DOCKER_IMAGE_NAME}:${env.BUILD_ID} pushed to Docker Hub successfully."
                    } catch (Exception e) {
                        echo "Failed to push Docker image: ${e.message}"
                        currentBuild.result = 'FAILURE' // Mark the build as failed
                    }
                }
            }
        }

        stage('Cleanup') {
            steps {
                script {
                    // Remove the built image after pushing
                    dockerImage.inside {
                        sh 'docker rmi ${DOCKER_IMAGE_NAME}:${env.BUILD_ID}'
                    }
                }
            }
        }
    }
}
