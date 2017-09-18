#!groovy

node {

  stage('Build') {
    checkout scm
    sh '''virtualenv env
./env/bin/python bootstrap.py test
. env/bin/activate
./env/bin/python src/manage.py makemigrations --merge --noinput
./env/bin/python src/manage.py collectstatic --link --noinput'''
  }

  stage('Test') {
    sh ". env/bin/activate && ./env/bin/python src/manage.py jenkins  -r --project-apps-tests --enable-coverage --pep8-ignore=W293,W291,E501,E261 --pep8-exclude=migrations,static,media --pylint-rcfile=pylint.rc --coverage-rcfile=.coveragerc"
    junit 'reports/junit.xml'
  // TODO: Pick up Coverage (reports/coverage.xml) and violations (reports/pep8.report, pyflakes.report, pylint.report)
  }

// Enable for SonarQube
//  stage('Analysis') {
//    def scannerHome = tool 'SonarQube Scanner 2.8';
//    withSonarQubeEnv('Jenkins Scanner') {
//      sh "${scannerHome}/bin/sonar-scanner"
//    }
//  }
}