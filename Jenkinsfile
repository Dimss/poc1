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
                            env.shortCommit = checkout(scm).GIT_COMMIT.substring(0, 7)
                            env.rabbitmqName = "rabbitmq-${env.shortCommit}"
                            env.models = openshift.process(testDepTemplate, "-p=RABBITMQ_NAME=${rabbitmqName}")
                            openshift.create(env.models)
                            def deployment = openshift.selector("deployment/${rabbitmqName}")
                            deployment.untilEach(1) {
                                echo "${it.object()}"
                                return it.object().status.readyReplicas == 1
                            }
                            echo "${deployment}"
                            echo "${env.models}"
                            echo "${env.shortCommit}"
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
                        RABBITMQ_IP="${env.rabbitmqName}"
                        RABBITMQ_QUEUE="sites-${env.shortCommit}"
                        pipenv run test
                    """
                }
            }
        }

//        stage("Cleanup test resources") {
//            steps {
//                script {
//                    openshift.withCluster() {
//                        openshift.withProject() {
//                            openshift.delete(env.models)
//                        }
//                    }
//                }
//            }
//        }


    }
}