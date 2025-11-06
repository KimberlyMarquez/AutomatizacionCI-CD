pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building . . .'
                bat "python -m py_compile shoppingCart.py"
            }
        }

        stage('Test') {
            steps {
                echo 'Testing . . .'
                bat "python -m unittest discover -v"
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploy . . .'
            }
        }
    }
}
