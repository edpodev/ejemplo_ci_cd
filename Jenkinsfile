pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t mi-app-flask .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                    docker stop mi-app-flask || true
                    docker rm mi-app-flask || true
                    docker run -d --name mi-app-flask -p 5000:5000 mi-app-flask
                '''
            }
        }
    }

    post {
        success {
            echo 'Deploy exitoso!'
        }
        failure {
            echo 'Algo salió mal.'
        }
    }
}