pipeline {
    agent {
        kubernetes {
            label 'my-pod-template-label' // Label of the pod template
            defaultContainer 'jnlp'
            yaml """
apiVersion: v1
kind: Pod
metadata:
  labels:
    some-label: 'my-pod-template-label'
spec:
  containers:
  - name: jenkins-agent
    image: jenkins/inbound-agent
    command:
    - '/bin/sh'
    - '-c'
    - 'cat'
    volumeMounts:
    - name: docker-socket
      mountPath: /var/run/docker.sock
  volumes:
  - name: docker-socket
    hostPath:
      path: /var/run/docker.sock
"""
        }
    }
    environment {
        NAMESPACE = 'defaultjenkins-agent'
        DEPLOYMENT_FILE = '/var/lib/jenkins/workspace/Pythonwebapp/Deployment.YAML'
        DOCKER_HOST = 'tcp://localhost:2375'
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
