'use strict';

var path = require('path');
var gulp = require('gulp');
var sass = require('gulp-sass');
var bourbon = require('bourbon');
var autoprefixer = require('gulp-autoprefixer');


var sass_src = 'src/{{ project_name|lower }}/sass/**/*.scss';
var css_dir = 'src/{{ project_name|lower }}/static/{{ project_name|lower }}/css';


gulp.task('sass', function() {
    gulp.src(sass_src)
        .pipe(sass({
            // sourceMap: true, // requires extra plugin
            outputStyle: 'expanded',
            includePaths: [
                path.join(__dirname, 'node_modules/bootstrap/scss')
            ].concat(bourbon.includePaths)
        }).on('error', sass.logError))
        .pipe(autoprefixer({
            browsers: ['last 2 versions'],
            cascade: false
        }))
        .pipe(gulp.dest(css_dir));
});


// watch task
gulp.task('default',function() {
    gulp.watch(sass_src, ['sass']);
});