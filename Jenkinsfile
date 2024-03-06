pipeline {
    agent {
        docker { 
            image 'sreejitheyne/bimage:latest' 
            args '--user root'
        }
    }
    // environment {
     //   NAMESPACE = 'defaultjenkins-agent'
     //   DEPLOYMENT_FILE = '/var/lib/jenkins/workspace/Pythonwebapp/Deployment.YAML'
     //   DOCKER_HOST = 'tcp://localhost:2375'
   // }
    stages {
        stage ('Build') {
             steps {
                script {
                    // Install dependencies from requirements.txt
                    sh 'pip install -r requirements.txt' 
                    // Install pytest
                    //sh 'pip install pytest'
                }
            }
        }
        //stage ('Test') {
        //     steps {
        //            sh '/usr/local/bin/pytest'
        //    }
        //}
        stage ('Docker image build') {
            steps {
                sh 'service docker start && docker ps'
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
