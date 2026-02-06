pipeline {
    agent any

    environment {
        IMAGE_NAME = "yourdockerhubusername/mlops-model"
    }

    stages {

        stage('Install Requirements') {
            steps {
                sh 'pip install --break-system-packages -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                sh 'python3 scripts/train.py'
            }
        }

        stage('Evaluate Model') {
            steps {
                sh '''
                python scripts/evaluate.py
                echo "Name: Nagam Sanjana"
                echo "Roll No: 2022BCS0208"
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Push Docker Image') {
            steps {
                sh '''
                docker login -u yourdockerhubusername -p yourpassword
                docker push $IMAGE_NAME
                '''
            }
        }
    }
}
