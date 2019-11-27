pipeline{
    agent any
    stages{ 
        stage('---Test Uno---'){
            steps{
                sh "pytest tests/anti_vowel_test.py"
            }
        }
        stage('---Test Dos---'){
            steps{
                sh "pytest tests/count_test.py"
            }
        }
        stage('---Test Tres---'){
            steps{
                sh "pytest tests/multiply_list_test.py"
            }
        }
    }
}