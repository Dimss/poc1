pipeline {
    agent {
        node {
            label 'python36'
        }
    }
    stages {
        stage("Install PIP dependencies") {
            steps {
                script {
                    sh "pipenv install"
                }
            }
        }
        stage("Deploy tests infra dependencies") {
            steps {
                script {
                    openshift.withCluster() {
                        openshift.withProject() {
                            def testDepTemplate = readFile('ocp/ci/unittests-resources-template.yaml')
                            def commitHash = checkout(scm).GIT_COMMIT
                            def rabbitmqName = "rabbitmq-${commitHash.substring(0, 7)}"
                            def models = openshift.process(testDepTemplate, "-p=RABBITMQ_NAME=${rabbitmqName}")
                            openshift.create(models)
                            def deployment = openshift.selector("deployment/${rabbitmqName}")
                            deployment.untilEach(1) { // We want a minimum of 1 build
                                echo "${it.object()}"
                                return it.object().status.readyReplicas == 1
                            }
                            openshift.delete(models)
                            echo "${deployment}"
                            echo "${models}"
                            echo "${commitHash}"
                            echo "${currentBuild.number}"

                        }
                    }

                }
            }
        }
        stage("Run tests") {
            steps {
                script {
                    sh """
                        PROFILE=prod
                        RABBITMQ_IP="rabbitmq-${checkout(scm).GIT_COMMIT.substring(0, 7)}"
                        RABBITMQ_QUEUE="sites-${checkout(scm).GIT_COMMIT.substring(0, 7)}"
                        pipenv run test
                    """
                }
            }

        }


    }
}