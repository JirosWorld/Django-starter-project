var paths = require('./build/paths');
var webpackConfig = require('./webpack.config.js');


// Add istanbul-instrumenter to webpack configuration
webpackConfig.module.postLoaders = [
    {
        test: /\.js$/,
        include: paths.jsSrcDir,
        loader: 'istanbul-instrumenter'
    }
];


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
            dir: paths.coverageDir,
            reporters: [
                { type: 'html', subdir: 'report-html' },
                { type: 'text' }
            ]
        },

        reporters: ['spec', 'coverage'],

        browsers: ['Chrome', 'Firefox', 'PhantomJS'],
    });
}


module.exports = configuration;
