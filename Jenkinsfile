pipeline{
    agent any
        
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
        // stage("Test"){
        //     steps{
        //         echo "Running tests..."
        //         // Add test commands here
        //     }
        // }
    }
 
}