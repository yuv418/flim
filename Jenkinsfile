pipeline {
agent none 
	stages {
		stage('Build') { 
				agent{
					node {
						checkout scm

						def customImage = docker.build(":${env.BUILD_ID}")
						
					}
					
			}
				
		}
	}
	
}

