pipeline {
    agent none 
    stages {
        stage('Build') { 
            steps {
				node {
					checkout scm

					def customImage = docker.build("my-image:${env.BUILD_ID}")
					
				}
			}
        }
        
    }
}
