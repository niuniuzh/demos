var gulp = require('gulp'),
  svgSprite = require('gulp-svg-sprite');

gulp.task('default', function () {
  return gulp.src('./assets/*.svg')
    .pipe(svgSprite())
    .pipe(gulp.dest('./www'));
});