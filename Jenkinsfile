pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                url: 'https://github.com/majda250/cicids2017-intrusion-detection.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t intrusion-api .'
            }
        }

        stage('Run Container Test') {
            steps {
                sh '''
                docker run -d --name api-test -p 8000:8000 intrusion-api
                sleep 15
                curl http://localhost:8000/
                docker stop api-test
                docker rm api-test
                '''
            }
        }

        stage('Deploy to Render') {
            steps {
                sh '''
                curl -X POST https://api.render.com/deploy/srv-d9jqeljtqb8s73at9srg?key=Fchzc_0VrA8
                '''
            }
        }

    }
}