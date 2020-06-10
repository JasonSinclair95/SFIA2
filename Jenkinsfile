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
                sh './script/ansible.sh'
            }
        }    
        stage('depoly application through docker compose') {
            agent { label 'Recruitmenyt_vm'}
            steps{
                sh './script/deploy_app.sh'   
            }
        }
    }
}