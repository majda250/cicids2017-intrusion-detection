pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t intrusion-api .'
            }
        }

        stage('Run Container Test') {
            steps {
                sh '''
                # supprimer l'ancien conteneur s'il existe
                docker rm -f api-test || true

                # lancer le nouveau conteneur
                docker run -d --name api-test -p 8001:8000 intrusion-api

                # attendre le démarrage
                sleep 15

                # tester l'API
                STATUS=$(curl -o /dev/null -s -w "%{http_code}" http://localhost:8001/)

                if [ "$STATUS" != "200" ]; then
                    docker logs api-test
                    docker rm -f api-test
                    exit 1
                fi

                docker rm -f api-test
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