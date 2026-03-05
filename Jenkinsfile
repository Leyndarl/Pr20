pipeline {
    agent any

    stages {
        stage('Install') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat 'pytest -q'
            }
        }
    }
}
