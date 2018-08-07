'use strict'

var gulp = require('gulp');
var plugins = require('gulp-load-plugins')();
var buffer = require('vinyl-buffer');
var merge = require('merge-stream');
var sass = require('gulp-sass');

gulp.task('sprite', function () {
    console.log(plugins);
    var spriteData = gulp.src('./src/images/*.png').pipe(plugins.spritesmith({
        imgName: 'sprite.png',
        cssName: 'sprite.css',
        imgPath: '../images/' + 'sprite.png'
    }));
    var imgStream = spriteData.img
        .pipe(buffer())
        .pipe(gulp.dest('./src/dest/images/'));
    var cssStream = spriteData.css
        .pipe(gulp.dest('./src/dest/css/'));
    return merge(imgStream, cssStream);
})

gulp.task('watch', function () {
    gulp.watch('src/images/*.png', ['sprite']);
})

gulp.task('default', ['sprite'])

gulp.task('sprite-scss', function () {
    var spriteData = gulp.src('./src/images/*.png').pipe(plugins.spritesmith({
        imgName: 'sprite.png',
        cssName: '_sprite.scss',
        // cssTemplate: './handlebarsStr.hbs',
        imgPath: '../images/' + 'sprite.png'
    }));
    var imgStream = spriteData.img
        .pipe(buffer())
        .pipe(gulp.dest('./src/dest/images/'));
    var cssStream = spriteData.css
        .pipe(gulp.dest('./src/dest/css/'));
    return merge(imgStream, cssStream);
})

gulp.task('sass', function () {
    return gulp.src('./src/dest/css/*.scss')
    .pipe(sass({
        sourceComments: 'map',
        outputStyle: 'nested'
    }).on('error', sass.logError))
    .pipe(gulp.dest('./src/dest/css'));
})

gulp.task('sass:watch', function () {
    gulp.watch('src/images/*.png', ['sprite-scss']);
    gulp.watch('src/dest/css/*.scss', ['sass']);
});

gulp.task('sass-watch', ['sass', 'sass:watch', 'sprite-scss'])