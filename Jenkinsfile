pipeline { 
    agent any 
    stages {
        stage('Build') { 
            steps { 
                sh 'docker build -t flim_docker .' 
            }
        }
        
        stage('Deliver') {
			steps {
				sh 'docker save flim_docker > flim_docker_image.tar'
				sh 'gzip flim_docker_image.tar'
			}
			
			post {
				success {
					archiveArtifacts 'flim_docker_image.tar.gz'
				}
				
			}
			
			
			
		}
    }
    
}
