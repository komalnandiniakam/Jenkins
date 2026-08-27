pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/komalnandiniakam/Jenkins.git'
            }
        }
        stage('Build') {
            steps {
                sh 'echo "Build stage running"'
                sh 'python3 --version'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 test_calculator.py'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "Deploy stage placeholder"'
            }
        }
    }
}
