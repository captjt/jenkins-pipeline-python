node {
   	stage 'Start'
	   	echo 'Starting build for jenkins-pipeline-python'
   	stage 'Checkout'
	   	checkout scm
	stage 'Build'
		sh 'python3.6 -m venv env'
		sh 'source env/bin/activate'
		sh 'pip install -r requirements.txt'
		sh "ls -la ${pwd()}"
		sh 'python setup.py test'
	stage 'Publish'
		publishHTML (target: [
			allowMissing: false,
			alwaysLinkToLastBuild: false,
			keepAll: true,
			reportDir: 'htmlcov',
			reportFiles: 'index.html',
			reportName: "Jenkins Pipeline (Python)"
		])
}
