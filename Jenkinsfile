
pipeline{
    agent any
    stages{
        stage("build enviorment"){
            steps{
                // sh 'sudo apt update -y'
                // sh 'sudo apt-get install -y unzip xvfb libxi6 libgconf-2-4'
                // sh 'sudo apt-get install default-jdk'
                // sh 'sudo apt-get remove docker docker-engine docker.io -y'
                // sh 'sudo apt-get purge containderd.io docker.io'
                // sh 'sudo apt-get install containerd.io'
                // sh 'sudo apt install docker.io -y'
                // sh 'sudo apt install docker-compose -y'
                // sh 'sudo systemctl start docker'
                // sh 'sudo systemctl enable docker'
                // sh 'sudo systemctl status docker'
                // sh 'sudo usermod -aG docker $USER'
            }
        }
        stage('depoly application through docker compose'){
            steps{
                sh 'docker-compose down' 
                sh 'sleep 5'
                sh 'docker-compose up --build -d'
                sh 'sleep 15'     
            }
        }
    }
}