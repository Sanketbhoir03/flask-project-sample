pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Clone your Git repository
                git 'https://github.com/Sanketbhoir03/flask-project-sample.git'

            }
        }

        stage('Setup Python') {
            steps {
                // Install python3 and pip if not installed
                sh '''
                if ! command -v python3 >/dev/null 2>&1; then
                  sudo apt-get update
                  sudo apt-get install -y python3
                fi

                if ! command -v pip3 >/dev/null 2>&1; then
                  sudo apt-get install -y python3-pip
                fi
                '''
            }
        }

        stage('Install dependencies') {
            steps {
                // Install dependencies from requirements.txt
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Kill existing Flask app') {
            steps {
                // Kill any process using port 5000 (ignore errors)
                sh 'fuser -k 5000/tcp || true'
            }
        }

        stage('Run Flask app') {
            steps {
                // Run app.py in background, redirect logs to flask.log
                sh 'nohup python3 app.py > flask.log 2>&1 &'
            }
        }
    }

    post {
        always {
            echo 'Jenkins pipeline completed.'
        }
    }
}
