pipeline {
    agent any

    stages {
        stage('Install Python Packages') {
            steps {
                sh 'python3 -m pip install --user -r code/requirements.txt'
            }
        }

        stage('Retrain Model') {
            when {
                changeset "**/training.csv"
            }
            steps {
                echo "Detected change in training.csv. Running retrain.py..."
                sh 'python3 retrain.py'
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
