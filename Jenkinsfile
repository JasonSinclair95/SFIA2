pipeline {
    agent any
    stages {
        stage('Development environment'){
            steps{
                sh 'chmod +x ./script/*'
                sh './script/jenks.sh'
            }
        
            }
        }
        
    }