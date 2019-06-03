pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
              sh 'source Vdirr/bin/activate'
              sh 'python mytest/manage.py test'
            }
        }
    }
}
