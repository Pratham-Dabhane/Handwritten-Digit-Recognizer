pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Pratham-Dabhane/Handwritten-Digit-Recognizer'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                python -m venv venv
                venv\\Scripts\\activate
                python -m pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                // Add test logic here (if any)
            }
        }

        stage('Build') {
            steps {
                echo 'Build stage (optional for Streamlit app)...'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying app...'
                // Deploy logic here (Streamlit sharing / containerize / etc.)
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
