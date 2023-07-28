pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 jenkinspy.py'
      }
    }
    stage('hello') {
      steps {
        sh 'python3 hello.py'
      }
    }
  }
}
