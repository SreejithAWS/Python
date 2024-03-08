pipeline {
    agent any
    stages {
        stage ('Build') {
             steps {
                script {
                    sh 'pip install -r requirements.txt' 
                }
            }
        }
        stage ('Docker image build') {
            steps {
                sh 'docker build -t sreejitheyne/pythonweb  . '
            }
        }
        stage('Push to docker hub') {
            steps {
                   withCredentials([string(credentialsId: 'dockerhub', variable: 'dockerhubpasswd')]){
                        sh "docker login -u sreejitheyne -p ${dockerhubpasswd}"
                    }
                        sh 'docker push sreejitheyne/pythonweb'
                }
            }
        stage('Kubernetes Deployment') {
            steps {
                    sh "kubectl --kubeconfig=${KUBECONFIG} --namespace=${NAMESPACE} apply -f ${DEPLOYMENT_FILE}"

                }
        }
    }
}
