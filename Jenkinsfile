pipeline {
    agent any

    environment {
        PYTHONPATH = '.'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Pratham-Dabhane/Handwritten-Digit-Recognizer.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Set up a virtual environment (optional but cleaner)
                sh '''
                    python -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                // Run your test file (create test_app.py as discussed)
                sh '''
                    . venv/bin/activate
                    python test_app.py
                '''
            }
        }

        stage('Build') {
            steps {
                echo 'Building application...'
                // You can optionally run Streamlit build checks or package prep here
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                // Example of simple Streamlit CLI deployment
                // Or scp to a server if you're self-hosting
                // sh 'streamlit run app.py &'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
