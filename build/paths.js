var path = require('path');
var fs = require('fs');


/** Parses package.json */
var pkg = JSON.parse(fs.readFileSync('./package.json', 'utf-8'));

/** Name of the sources directory */
var sourcesRoot = 'src/' + pkg.name + '/';

/** Name of the static (source) directory */
var staticRoot = sourcesRoot + 'static/';


/**
 * Application path configuration for use in gulp tasks/webpack
 */
module.exports = {
    // Parsed package.json
    package: pkg,

    // Path to the sass (sources) directory
    sassSrc: sourcesRoot + 'sass/**/*.scss',

    // Path to the (transpiled) css directory
    cssDir: staticRoot + 'css/',

    // Path to the js entry point (source)
    jsEntry: sourcesRoot + 'js/index.js',

    // Path to js (sources)
    jsSrc: sourcesRoot + '/js/**/*.js',

    // Path to the js (sources) directory
    jsSrcDir: sourcesRoot + 'js/',

    // Path to the (transpiled) js directory
    jsDir: staticRoot + 'js/',

    // Path to js spec (test) files
    jsSpec: sourcesRoot + 'test/**/*.spec.js',

    // Path to js spec (test) entry file
    jsSpecEntry: sourcesRoot + 'test/index.js',

    // Path to js code coverage directory
    coverageDir: 'build/reports/coverage/'
};
