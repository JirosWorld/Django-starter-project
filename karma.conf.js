const argv = require('minimist')(process.argv.slice(2));
const JENKINS_URL = process.env.JENKINS_URL;

const log = require('npmlog');
log.level = 'silly';

const COVERAGE = argv.coverage === true || JENKINS_URL;// code coverage on by default on Jenkins, or activated by flag --coverage

var preprocessors = [];
var reporters = ['spec'];

var jspmConfigFiles = [
    'src/{{ project_name|lower }}/static/js/jspm.browser.js',
    'src/{{ project_name|lower }}/static/js/jspm.config.js',
];

// the devConfig is only needed if we're running with coverage enabled
if (COVERAGE) {
    jspmConfigFiles.push('src/jstests/jspm.test.js');
}

if (COVERAGE) {
    log.info('karma', 'Coverage enabled');
    preprocessors = ['babel'];
    reporters.push('coverage');
}


/* global module */
module.exports = function (config) {
    'use strict';

    config.set({
        logLevel: config.LOG_INFO,

        autoWatch: true,
        singleRun: true,

        browserNoActivityTimeout: 1000, // if you have a lot of files loaded async, up this value

        frameworks: ['jspm', 'jasmine-ajax', 'jasmine'],

        jspm: {
            config: jspmConfigFiles,
            loadFiles: [
                'src/jstests/**/*.spec.js'
            ],
            serveFiles: [
                'static/**/*.js',
                // 'static/images/**/*'
            ],
            stripExtension: false,
            meta: {
              "src/jstests/*.js": {
                "loader": "plugin-babel",
                // "babelOptions": {
                //   "plugins": [
                //     "babel-plugin-transform-react-jsx",
                //     "babel-plugin-transform-class-properties"
                //   ]
                // }
              }
            }
        },

        // karma serves everything from /base/, which is the 'cwd' (= project root)
        proxies: {
            '/static/src/jstests/': '/base/src/jstests/',
            '/static/': '/base/static/',
        },

        browsers: ['PhantomJS', 'Chrome'],

        preprocessors: {
            // limited to the 'js' subfolder, because it otherwise pre-processes the django apps js
            'static/js/**/!(jspm.browser|jspm.config|*spec).js': preprocessors
        },

        babelPreprocessor: {
            options: {
                plugins: [
                    'istanbul', // instrumenter for coverage
                    // 'transform-react-jsx',
                    // 'transform-class-properties'
                ],
                presets: ['es2015'],
                sourceMap: 'inline',
            },
            sourceFileName: function(file) {
                return file.originalPath;
            }
        },

        client: {
            captureConsole: true,
        },

        reporters: reporters,

        coverageReporter: {

            reporters: [
                {
                    type: 'text-summary',
                    subdir: normalizationBrowserName
                },
                {
                    type: 'html',
                    dir: 'reports/jstests/',
                    subdir: normalizationBrowserName
                },
                // for jenkins - Cobertura XML format
                {
                    type: 'cobertura',
                    dir: 'reports/jstests/',
                    subdir: '.',
                    file: 'coverage.xml'
                }
            ]
        }

    });

    function normalizationBrowserName(browser) {
        return browser.toLowerCase().split(/[ /-]/)[0];
    }

};
