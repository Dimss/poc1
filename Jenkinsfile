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
                            def test = checkout(scm).GIT_COMMIT
//                            def shortCommit = sh(returnStdout: true, script: "git log -n 1 --pretty=format:'%h'").trim()
//                            def rabbitmqName = "rabbitmq-${shortCommit}"
                            def models = openshift.process(testDepTemplate, "-p=RABBITMQ_NAME=asdasd")
                            echo "${models}"
                            echo "${commitHash}"
                            echo "${test}"
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