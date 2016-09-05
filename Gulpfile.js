'use strict';

var gulp = require('gulp');
var path = require('path');
var rename = require("gulp-rename");
var watch = require('gulp-watch');

var autoprefixer = require('gulp-autoprefixer');
var sass = require('gulp-sass');
var sourcemaps = require('gulp-sourcemaps');
var neat = require('bourbon-neat');


/**
 * Sass related tasks
 */
var sass_src = 'src/{{ project_name|lower }}/sass/**/*.scss';
var css_dir = 'src/{{ project_name|lower }}/static/css';


gulp.task('sass', function() {
    gulp.src(sass_src)
        .pipe(sourcemaps.init())
        .pipe(sass({
            outputStyle: 'expanded',
            includePaths: neat.includePaths
        }).on('error', sass.logError))
        .pipe(autoprefixer({
            browsers: ['last 2 versions'],
            cascade: false
        }))
        .pipe(sourcemaps.write('./'))
        .pipe(gulp.dest(css_dir));
});


gulp.task('watch_sass', ['sass'], function() {
    gulp.watch(sass_src, ['sass']);
});


/**
 * Collectstatic equivalent (more or less)
 */

var STATIC_ROOT = './static';
var STATIC_APPDIRS = 'src/{{ project_name|lower }}/*/static/**/*.js';
var STATICFILES_DIRS = [
    'src/{{ project_name|lower }}/static/**/*.js'
];

gulp.task('watch_collectstatic', function() {
    var src = [STATIC_APPDIRS].concat(STATICFILES_DIRS);
    return watch(src, {verbose: true, base: 'src/{{ project_name|lower }}'})
        .pipe(rename(function(file) {
            var bits = file.dirname.split('/');
            // strip off 'static' (and appname if present)
            file.dirname = bits.slice(slice).join('/');
            return file;
        }))
        .pipe(gulp.dest(STATIC_ROOT));
});


/**
 * default executed task when running 'gulp'
 */
gulp.task('default', ['watch_sass', 'watch_collectstatic']);
