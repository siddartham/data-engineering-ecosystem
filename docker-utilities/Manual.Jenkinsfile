pipeline {
    agent {
        docker {
            image 'artifactory.my.com:9001/sustainability/test-corretto8-python38-spark30'
            args (
                '-ti -u ci ' +
                // This following is necessary in order to use docker
                '-v /var/run/docker.sock:/var/run/docker.sock ' +
                '--network host ' +
                '--uts=host'
            )
        }
    }
    stages {
        stage('install'){
            when {
                anyOf {
                    branch "main"
                    branch "PR-*"
                }
            }
            steps {
                sh "make ci-install"
            }
        }
        stage('test') {
            // Run tox if package files have changed, tests have changed,
            // requirements have changed, this is our first build, or
            // the previous build failed
            when {
                anyOf {
                    branch "PR-*"
                }
                anyOf {
                    changeset "docker_utilities/**"
                    changeset "setup.py"
                    changeset "setup.cfg"
                    changeset "tests/**"
                    buildingTag()
                    expression {
                        return currentBuild.previousBuild == null
                    }
                    expression {
                        !("SUCCESS".equals(currentBuild.previousBuild.result))
                    }
                }
            }
            steps {
                sh 'make test'
            }
        }
        stage('distribute') {
            // Distribute if this is the main branch and setup files have
            // changed, the previous build failed, or a build tag is detected
            when {
                branch "main"
                anyOf {
                    changeset "setup.py"
                    changeset "setup.cfg"
                    buildingTag()
                    expression {
                        return currentBuild.previousBuild == null
                    }
                    expression {
                        !("SUCCESS".equals(currentBuild.previousBuild.result))
                    }
                }
            }
            steps {
                sh 'make distribute'
            }
        }
    }
    post {
        // Install mail-client
        always {
            sh "python3 -m venv venv"
            sh "venv/bin/pip3 install mail-client"
        }
        // Email Build Results to the Author of the Commit
        success {
            sh (
                "venv/bin/mail-client send " +
                "-t \"\$(git --no-pager show -s --format=%ae ${env.GIT_COMMIT})\" " +
                "-pcp \"app/sustainability/bmx/a.BMX.SUSTAINABILITY\" " +
                "-s \"Success - ${env.JOB_NAME}\" " +
                "-b \"${env.BUILD_URL}\" || " +
                "venv/bin/mail-client send " +
                "-t ${env.CHANGE_AUTHOR_EMAIL} " +
                "-pcp \"app/sustainability/bmx/a.BMX.SUSTAINABILITY\" " +
                "-s \"Success - ${env.JOB_NAME}\" " +
                "-b \"${env.BUILD_URL}\""
            )
        }
        failure {
            sh (
                "venv/bin/mail-client send " +
                "-t \"\$(git --no-pager show -s --format=%ae ${env.GIT_COMMIT})\" " +
                "-pcp \"app/sustainability/bmx/a.BMX.SUSTAINABILITY\" " +
                "-s \"Failure - ${env.JOB_NAME}\" " +
                "-b \"${env.BUILD_URL}\" || " +
                "venv/bin/mail-client send " +
                "-t ${env.CHANGE_AUTHOR_EMAIL} " +
                "-pcp \"app/sustainability/bmx/a.BMX.SUSTAINABILITY\" " +
                "-s \"Failure - ${env.JOB_NAME}\" " +
                "-b \"${env.BUILD_URL}\""
            )
        }
        aborted {
            sh (
                "venv/bin/mail-client send " +
                "-t \"\$(git --no-pager show -s --format=%ae ${env.GIT_COMMIT})\" " +
                "-pcp \"app/sustainability/bmx/a.BMX.SUSTAINABILITY\" " +
                "-s \"Aborted - ${env.JOB_NAME}\" " +
                "-b \"${env.BUILD_URL}\" || " +
                "venv/bin/mail-client send " +
                "-t ${env.CHANGE_AUTHOR_EMAIL} " +
                "-pcp \"app/sustainability/bmx/a.BMX.SUSTAINABILITY\" " +
                "-s \"Aborted - ${env.JOB_NAME}\" " +
                "-b \"${env.BUILD_URL}\""
            )
        }
    }
}
