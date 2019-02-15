pipeline {
//    agent any
    agent {
        node {
            label 'python36'
        }
    }
    stages {
        stage("Install PIP dependencies") {
            steps {
                script {
                    openshift.withCluster() {
                        openshift.withProject() {
//                            def ciTemplate = readFile('ocp/ci/ci-template.yaml')
//                            def models = openshift.process(
//                                    "openshift//postgresql-ephemeral",
//                                    "-p=POSTGRESQL_DATABASE=postgres",
//                                    "-p=POSTGRESQL_PASSWORD=postgres",
//                                    "-p=POSTGRESQL_USER=postgres",
//                                    "-p=DATABASE_SERVICE_NAME=pg")
//                            openshift.create(models)
//                            def scmUrl = scm.getUserRemoteConfigs()[0].getUrl()
//                            def currentOcpProject = openshift.project()
//                            def models = openshift.process(ciTemplate,
//                                    "-p=PROJECT_NAME=${currentOcpProject}",
//                                    "-p", "GIT_REPO_URL=${scmUrl}")
//                            openshift.delete(models)
//                            echo "${models.size()}"
//                            for (o in models) {
//                                echo "${o}"
//                                echo "${o.metadata}"
//                                echo "${o.metadata.name}"
//                                echo "${o.kind}"
//                                if (o.kind == "ImageStream" & o.metadata.name == "postgres"){
//                                    echo "${o}"
//                                }
//                            }
//                            sh "pipenv install"
                        }
                    }
                }
            }
        }
        stage("Deploy tests dependencies") {
            steps {
                script {
                    openshift.withCluster() {
                        openshift.withProject() {
                            def testDepTemplate = readFile('ocp/ci/unittests-resources-template.yaml')
                            def commitHash = checkout(scm).GIT_COMMIT
                            def rabbitmqName = "rabbitmq-${commitHash.substring(0, 7)}"
                            def models = openshift.process(testDepTemplate, "-p=RABBITMQ_NAME=${rabbitmqName}")
                            def createdObj = openshift.create(models)
                            def deployment = openshift.selector( "deployment/${rabbitmqName}" )
                            deployment.untilEach(1) { // We want a minimum of 1 build

                                // Unlike watch(), untilEach binds 'it' to a Selector for a single object.
                                // Thus, untilEach will only terminate when all selected objects satisfy this
                                // the condition established in the closure body (or until the timeout(10)
                                // interrupts the operation).
                                echo "${it.object()}"
                                return it.object().status.readyReplicas == 1
                            }
                            openshift.delete(models)
//                            def deployment = createdObj.related('deployments')
//                            builds.untilEach(1) { // We want a minimum of 1 build
//
//                                // Unlike watch(), untilEach binds 'it' to a Selector for a single object.
//                                // Thus, untilEach will only terminate when all selected objects satisfy this
//                                // the condition established in the closure body (or until the timeout(10)
//                                // interrupts the operation).
//
//                                return it.object().status.phase == "Complete"
//                            }
                            echo "${deployment}"
                            echo "${models}"
                            echo "${commitHash}"
                            echo "${currentBuild.number}"

                        }
                    }

                }
            }
        }
//        stage("Run tests") {
//            steps {
//                script {
//                    sh "pipenv run test"
//                }
//            }
//
//        }


    }
}