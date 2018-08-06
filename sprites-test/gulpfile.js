'use strict'

var gulp = require('gulp');
var plugins = require('gulp-load-plugins')();
var buffer = require('vinyl-buffer');
var merge = require('merge-stream');

gulp.task('sprite', function () {
    console.log(plugins);
    var spriteData = gulp.src('./src/images/*.png').pipe(plugins.spritesmith({
        imgName: 'sprite.png',
        cssName: 'sprite.css'
    }));
    var imgStream = spriteData.img
        .pipe(buffer())
        .pipe(gulp.dest('./src/dest/images/'));
    var cssStream = spriteData.css
        .pipe(gulp.dest('./src/dest/css/'));
    return merge(imgStream, cssStream);
})

gulp.task('watch',function(){
    gulp.watch('src/images/*.png',['sprite']);
})

gulp.task('default',['sprite'])