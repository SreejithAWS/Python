pipeline {
    agent any
    stages {
        stage ('Build') {
            steps {
                sh 'pip install -r requirments.txt, pytest '
            }
        }
        stage ('Test') {
            steps {
                sh 'pytest'
            }
        }
    }
}
