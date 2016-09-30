var path = require('path');
var fs = require('fs');


/** Parses package.json */
var package = JSON.parse(fs.readFileSync('./package.json', 'utf-8'));

/** Name of the sources directory */
var sourcesRoot = 'src/' + package.name + '/';

/** Name of the static (source) directory */
var staticRoot = sourcesRoot + 'static/';


/**
 * Application path configuration for use in gulp tasks/webpack
 */
module.exports = {
    // Parsed package.json
    package: package,

    // Path to the sass (sources) directory
    sassSrc: sourcesRoot + '/sass/**/*.scss',

    // Path to the (transpiled) css directory
    cssDir: staticRoot + 'css/',

    // Path to the js entry point (source)
    jsEntry: sourcesRoot + '/js/index.js',

    // Path to the js (sources) directory
    jsSrc: sourcesRoot + '/js/**/*.js',

    // Path to the (transpiled) js directory
    jsDir: staticRoot + 'js/',
};
