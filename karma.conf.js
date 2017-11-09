var path = require('path');
var paths = require('./build/paths');
var webpackConfig = require('./webpack.config.js');


// Add istanbul-instrumenter to webpack configuration
webpackConfig.module.loaders.push({
    test: /\.js$/,
    include: __dirname + '/' + paths.jsSrcDir,
    loader: 'istanbul-instrumenter-loader',
    enforce: 'post',

    options: {
        esModules: true
    }
});


// The preprocessor config
var preprocessors = {};
preprocessors[paths.jsSpecEntry] = [
    'webpack'
]


// The main configuration
var configuration = function(config) {
    config.set({
        frameworks: [
            'jasmine-jquery',
            'jasmine-ajax',
            'jasmine'
        ],

        files: [
            paths.jsSpecEntry
        ],

        preprocessors: preprocessors,

        webpack: webpackConfig,

        webpackMiddleware: {
            noInfo: true
        },

        coverageReporter: {
            reporters: [
                { type: 'cobertura', dir: paths.coverageDir, subdir: '.', file: 'coverage.xml' },
                { type: 'html', dir: paths.coverageDir, subdir: 'html' },
                { type: 'text' }
            ]
        },

        reporters: ['spec', 'coverage'],

        browsers: ['Chrome', 'Firefox', 'PhantomJS'],
    });
}


module.exports = configuration;
