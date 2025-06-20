pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/newdelthis/ml-deploy.git'
            }
        }

        stage('Retrain Model') {
            steps {
                sh 'python retrain.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ml-api:latest .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker rm -f ml-api || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name ml-api ml-api:latest'
            }
        }
    }
}
