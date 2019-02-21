import groovy.json.JsonOutput

def getJobName() {
    jobNameList = env.JOB_NAME.split("/")
    if (jobNameList.size() > 0) {
        return jobNameList[jobNameList.size() - 1]
    } else {
        return jobName
    }
}

def getAppName() {
    return "${getJobName()}-${getGitCommitShrotHash()}"
}

def getGitCommitShrotHash() {
    return checkout(scm).GIT_COMMIT.substring(0, 7)
}

pipeline {
    agent any
//    agent {
//        node {
//            label 'python36'
//        }
//    }
    stages {
        stage('Checkout code') {
            echo "${env.gitlabSourceBranch}"
            steps {
                checkout changelog: true, poll: true, scm: [
                        $class                           : 'GitSCM',
                        branches                         : [[name: "origin/${env.gitlabSourceBranch}"]],
                        doGenerateSubmoduleConfigurations: false,
                        submoduleCfg                     : [],
                ]
            }
        }
//        stage("Install PIP dependencies") {
//            steps {
//                script {
//                    sh "pipenv install"
//                }
//            }
//        }
//        stage("Deploy tests infra dependencies") {
//            steps {
//                script {
//                    openshift.withCluster() {
//                        openshift.withProject() {
//                            def testDepTemplate = readFile('ocp/ci/unittests-resources-template.yaml')
//                            env.shortCommit = checkout(scm).GIT_COMMIT.substring(0, 7)
//                            env.rabbitmqName = "rabbitmq-${env.shortCommit}"
//                            def models = openshift.process(testDepTemplate, "-p=RABBITMQ_NAME=${rabbitmqName}")
//                            openshift.create(models)
//                            def deployment = openshift.selector("deployment/${rabbitmqName}")
//                            deployment.untilEach(1) {
//                                echo "${it.object()}"
//                                return it.object().status.readyReplicas == 1
//                            }
//                            echo "${deployment}"
//                            echo "${models}"
//                            echo "${env.shortCommit}"
//                            echo "${currentBuild.number}"
//
//                        }
//                    }
//
//                }
//            }
//        }
//        stage("Run tests") {
//            steps {
//                script {
//                    sh """
//                        echo PROFILE=prod >.env
//                        echo RABBITMQ_IP="${env.rabbitmqName}" >>.env
//                        echo RABBITMQ_QUEUE="sites-${env.shortCommit}" >>.env
//                        pipenv run test
//                    """
//                }
//            }
//        }
//
//        stage("Cleanup test resources") {
//            steps {
//                script {
//                    openshift.withCluster() {
//                        openshift.withProject() {
//                            def testDepTemplate = readFile('ocp/ci/unittests-resources-template.yaml')
//                            def models = openshift.process(testDepTemplate, "-p=RABBITMQ_NAME=${env.rabbitmqName}")
//                            openshift.delete(models)
//                        }
//                    }
//                }
//            }
//        }

        stage("Create S2I image stream and build configs") {
            steps {
                script {
                    openshift.withCluster() {
                        openshift.withProject() {
//                            def icBcTemplate = readFile('ocp/ci/app-is-bc.yaml')
//                            def models = openshift.process(icBcTemplate,
//                                    "-p=BC_IS_NAME=${getAppName()}",
//                                    "-p=DOCKER_REGISTRY=${env.DOCKER_REGISTRY}",
//                                    "-p=DOCKER_IMAGE_NAME=/${env.DOCKER_IMAGE_PREFIX}/${GOVIL_APP_NAME}",
//                                    "-p=DOCKER_IMAGE_TAG=${getGitCommitShrotHash()}-${currentBuild.number}",
//                                    "-p=GIT_REPO=${scm.getUserRemoteConfigs()[0].getUrl()}",
//                                    "-p=GIT_REF=${env.BRANCH_NAME}",
//                                    "-p=S2I_BUILDER_ISTAG=${env.S2I_BUILD_IMAGE}"
//                            )
//                            echo "${JsonOutput.prettyPrint(JsonOutput.toJson(models))}"
//                            openshift.create(models)
                            echo "${getAppName()}"
                            echo "${env.DOCKER_REGISTRY}"

                            echo "${env.BRANCH_NAME}"
                            def scmVars = checkout scm
                            echo "${scmVars}"
                            def tag = sh(returnStdout: true, script: "git tag --contains").trim()
                            echo "==========================="
                            echo "${tag}"
                            echo "${env.gitlabBranch}"
                            echo sh(returnStdout: true, script: 'env')
                            echo "==========================="
                            echo "${env.gitlabActionType}"
                            echo "${env.gitlabBranch}"
                            echo "==========================="
//                            echo "============ THIS IS MASTER PUSH ==============="
//                            echo "==========================="

//                            sh(returnStdout: true, script: "git tag --points-at")


                        }
                    }
                }
            }
        }
    }


    post {
        failure {
            script {
                openshift.withCluster() {
                    openshift.withProject() {
                        def testDepTemplate = readFile('ocp/ci/unittests-resources-template.yaml')
                        def models = openshift.process(testDepTemplate, "-p=RABBITMQ_NAME=${env.rabbitmqName}")
                        openshift.delete(models)

                    }
                }
            }
        }
    }
}