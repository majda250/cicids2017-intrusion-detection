pipeline {

    agent any

    environment {
        IMAGE_NAME = "cicids2017-api"
        CONTAINER_NAME = "cicids2017-container"
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Récupération du projet depuis GitHub...'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Construction de l’image Docker...'
                sh 'docker build -t ${IMAGE_NAME}:latest .'
            }
        }

        stage('Verify Image') {
            steps {
                echo 'Vérification de l’image...'
                sh 'docker images'
            }
        }

        stage('Run Container') {
            steps {
                echo 'Lancement du conteneur...'
                sh '''
                docker rm -f ${CONTAINER_NAME} || true
                docker run -d \
                    --name ${CONTAINER_NAME} \
                    -p 8000:8000 \
                    ${IMAGE_NAME}:latest
                '''
            }
        }

        stage('API Health Check') {
            steps {
                echo 'Test de l’API...'
                sh '''
                sleep 10
                curl http://host.docker.internal:8000/
                '''
            }
        }

        stage('Stop Container') {
            steps {
                echo 'Arrêt du conteneur...'
                sh '''
                docker stop ${CONTAINER_NAME}
                docker rm ${CONTAINER_NAME}
                '''
            }
        }

    }

    post {

        success {
            echo 'Pipeline exécutée avec succès.'
        }

        failure {
            echo 'La pipeline a échoué.'
        }

        always {
            sh 'docker rm -f ${CONTAINER_NAME} || true'
        }
    }
}