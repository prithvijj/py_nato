pipeline {
	agent none
	stages {
		stage('Build'){
			agent{
				docker{
					image 'python:3-alpine'
				}
			}
			steps {
				sh 'python -m py_compile py_nato.py'
			}
		}
		stage('Test'){
			agent {
				docker {
					image 'qnib/pytest'
				}
			}
			steps {
				sh 'py.test --verbose --junit-xml test_results.xml test_nato.py'
			}
			post {
				always {
					junit 'test_results.xml'
				}
			}
		}
	}
}