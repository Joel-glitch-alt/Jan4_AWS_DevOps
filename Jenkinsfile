pipeline{
    agent any

     environment {
        SCANNER_HOME = tool 'sonar-scanner'
        SONARQUBE = 'Jenkins-Sonar-Server'
        // DOCKER_IMAGE = 'addition1905/jandevopsfour'
        // DOCKER_TAG = "${env.BUILD_NUMBER}"
    }
        
    stages{
        stage("Checkout"){
            steps{
                checkout scm
            }
          
        }
        stage("Build"){
            steps{
                echo "Building the application..."
                // Add build commands here
            }
        }
         stage("Test"){
        steps {
        echo 'Running tests...'
        sh '''
        python3 -m venv venv    
        venv/bin/pip install --upgrade pip
        venv/bin/pip install -r requirements.txt
        venv/bin/pytest --cov=. --cov-report=xml || true
        '''
            }
         }


        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv("${SONARQUBE}") {
                    sh """
                        ${SCANNER_HOME}/bin/sonar-scanner \
                          -Dsonar.projectKey=jan_key \
                          -Dsonar.projectName=Jan4 \
                          -Dsonar.sources=. \
                          -Dsonar.sourceEncoding=UTF-8 \
                          -Dsonar.python.coverage.reportPaths=coverage.xml
                    """
                }
            }
        }
    }
    post{
        always{
            echo "Pipeline execution completed."
        }
    }
 
}