pipeline  {
    agent any
    
    environment {
        ENV = 'qa'
        PYTHONPATH = "${WORKSPACE}"
    }
    
    stages {
        stage('Setup') {
            steps {
                sh 'python -m pip install -r requirements.txt'
            }
        }
        
        stage('Test') {
            steps {
                sh '''
                    export ENV=qa
                    pytest --alluredir=allure-results --junitxml=junit.xml
                '''
            }
        }
        
        stage('Reports') {
            steps {
                publishHTML([
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'allure-results',
                    reportFiles: 'index.html',
                    reportName: 'Allure Report'
                ])
                
                junit 'junit.xml'
            }
        }
    }
    
    post {
        always {
            archiveArtifacts artifacts: 'allure-results/**, junit.xml', fingerprint: true
        }
    }
}
 