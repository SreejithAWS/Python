pipeline {
    agent any
    environment {
        KUBECONFIG = '/home/jith/.kube/config'
        NAMESPACE = 'default'
        DEPLOYMENT_FILE = '/var/lib/jenkins/workspace/Pythonwebapp/Deployment.YAML'
    }
    stages {
        stage ('Build') {
            steps {
                sh 'pip install -r requirements.txt || true' 
                sh 'pip install pytest'
            }
        }
        stage ('Test') {
            steps {
                sh '/var/lib/jenkins/.local/bin/pytest'
            }
        }
        stage ('Docker image build') {
            steps {
                sh 'docker build -t sreejitheyne/pythonweb -f Dockerfile . '
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

