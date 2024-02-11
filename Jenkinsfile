pipeline {
    agent any
    stages {
        stage ('Build') {
            steps {
                sh 'pip install -r requirements.txt'
                 sh 'pytest'
            }
        }
        stage ('Test') {
            steps {
                sh 'pip install pytest'
            }
        }
    }
}
