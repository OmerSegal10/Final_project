pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'omersegal10/flask-app'
        GITHUB_API_URL = 'https://api.github.com'
        GITHUB_REPO = 'OmerSegal10/Final_project'
        GITHUB_TOKEN = credentials('github-creds')
    }

    stages {
        stage("Checkout code") {
            steps {
                checkout scm
            }
        }

        stage("Build Docker image") {
            steps {
                script {
                    dockerImage = docker.build("${env.DOCKER_IMAGE}:latest", "--no-cache .")
                }
            }
        }

        stage("Run Tests") {
            steps {
                script {
                    dockerImage.inside {
                        sh 'python -m unittest discover -s tests'
                    }
                }
            }
        }

        stage("Push Docker image") {
            when {
                branch 'feature'
            }
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-creds') {
                        dockerImage.push("latest")
                    }
                }
            }
        }

        stage("Create Pull Request") {
            when {
                not {
                    branch 'feature'
                }
            }
            steps {
                script {
                    def branchName = env.BRANCH_NAME
                    def pullRequestTitle = "Merge ${branchName} into feature"
                    def pullRequestBody = "Automatically generated merge request for branch ${branchName}"

                    sh """
                        curl -X POST -H "Authorization: token ${GITHUB_TOKEN}" \
                        -d '{ "title": "${pullRequestTitle}", "body": "${pullRequestBody}", "head": "${branchName}", "base": "feature" }' \
                        ${GITHUB_API_URL}/repos/${GITHUB_REPO}/pulls
                    """
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
