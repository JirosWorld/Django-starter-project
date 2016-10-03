var paths = require('./build/paths');
var webpackConfig = require('./webpack.config.js');


// Add istanbul-instrumenter to webpack configuration
webpackConfig.module.loaders.push(
    {
        test: /\.js$/,
        exclude: /(node_modules|test)/,
        loader: 'babel-istanbul-loader'
    }
);


// The preprocessor config
var preprocessors = {}
preprocessors[paths.jsSpec] = [
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
            paths.jsSpec,
        ],

        preprocessors: preprocessors,

        webpack: webpackConfig,

        webpackMiddleware: {
            noInfo: true
        },

        coverageReporter: {
            dir: paths.coverageDir
        },

        reporters: ['spec', 'coverage'],

        browsers: ['Chrome'],
    });
}


module.exports = configuration;
