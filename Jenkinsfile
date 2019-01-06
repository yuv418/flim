pipeline {
    agent none 
    stages {
        stage('Build') { 
            steps {
				withEnv(['PATH+EXTRA=/usr/sbin:/usr/bin:/sbin:/bin']) {  
					sh 'docker build -t flim_docker .'
				}
			}
        }
        
    }
}
