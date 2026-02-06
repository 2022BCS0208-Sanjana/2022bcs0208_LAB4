pipeline {

    
    agent any

    environment {
        IMAGE_NAME = "2022bcs0208sanjana/mlops-model"
    }

    stages {
        stage('Install Python') {
    steps {
        sh '''
        apt-get update
        apt-get install -y python3 python3-pip
        '''
    }
}
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
                python3 scripts/evaluate.py
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
