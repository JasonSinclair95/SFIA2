pipeline{
    agent any
    stages {
        stage("Enable my script folder to be executable") {
            steps {
               sh "chmod +x ./script/*"
            }
        }
        stage(' Prepair enviornment') {
            steps{
                sh './script/installation.sh'
            }
        }    
        stage('depoly application through docker compose') {
            steps{
                sh 'source ~/.bashrc'
                sh 'docker-compose down' 
                sh 'sleep 5'
                sh 'docker-compose up --build -d'
                sh 'sleep 15'     
            }
        }
    }
}