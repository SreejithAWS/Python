pipeline {
    agent any
    stages {
        stage ('Build') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pip install pytest'
            }
        }
        stage ('Test') {
            steps {
              sh 'pytest'   
            }
        }
    }
}
