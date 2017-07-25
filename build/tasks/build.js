'use strict';
var gulp = require('gulp');


/**
 * Default task
 * Run using "gulp"
 * Runs "sass" and "js" and "watch" tasks
 */
gulp.task('build', ['sass', 'js']);
