import autoprefixer from 'gulp-autoprefixer';
import babelify from 'babelify';
import browserify from 'browserify';
import concat from 'gulp-concat';
import del from 'del';
import domain from 'domain';
import flatten from 'gulp-flatten';
import filter from 'gulp-filter';
import gulp from 'gulp';
import gutil from 'gulp-util';
import hbsfy from 'hbsfy';
import plumber from 'gulp-plumber';
import sass from 'gulp-sass';
import tap from 'gulp-tap';


/* Default task */
gulp.task('default', function() {
  gulp.start('build');
});


/* Removing whole ./src/static/ directory */
gulp.task('clean', del.bind(null, './src/static'));


/* Building JS */
gulp.task('js', function() {
  return gulp.src('./src/assets/js/main.js')
    .pipe(plumber())
    .pipe(tap(function(file) {
      const dom = domain.create();
      dom.on('error', function(err) {
        gutil.log(
          gutil.colors.red('Browserify compile error:'),
          err.message, '\n\t',
          gutil.colors.cyan('in file'), file.path
        );
        gutil.beep();
      });
      dom.run(function() {
        file.contents = browserify({
          entries: [file.path],
          debug: false,
          standalone: 'Planting',
          paths: ['./node_modules/', './src/assets/'],
          transform: [
            [hbsfy, {
              global: true,
              ignore: /\/node_modules\/(?!plantingjs\/)/,
            }],
            [babelify, {
              global: true,
              ignore: /\/node_modules\/(?!plantingjs\/)/,
            }],
          ],
        }).bundle();
      });
    }))
    .pipe(gulp.dest('./src/static/js/'));
});
/* End of building JS */

/* Building CSS */
gulp.task('css:main', function() {
  return gulp.src('./src/assets/css/**/*.scss')
    .pipe(sass())
    .pipe(autoprefixer({browsers: ['last 1 version']}))
    .pipe(concat('main.css'))
    .pipe(gulp.dest('./src/static/css/'));
});

gulp.task('css:vendor', function() {
  return gulp.src([
    './node_modules/jquery-ui/themes/base/jquery-ui.css',
    './node_modules/jquery-ui/themes/base/jquery.ui.dialog.css',
    './node_modules/plantingjs/src/styles/*.scss',
  ])
    .pipe(sass())
    .pipe(concat('vendor.css'))
    .pipe(gulp.dest('./src/static/css/'));
});

gulp.task('css', ['css:vendor', 'css:main']);
/* End of building CSS */


/* Building fonts */
gulp.task('fonts', function() {
  return gulp.src('./node_modules/plantingjs/src/fonts/**/*')
    .pipe(filter('**/*.{eot,svg,ttf,woff}'))
    .pipe(flatten())
    .pipe(gulp.dest('./src/static/fonts'));
});
/* End of building fonts */


/* Building assets */
gulp.task('assets', function() {
  return gulp.src('./src/assets/assets/**/*')
    .pipe(gulp.dest('./src/static'));
});
/* End of building assets */

/* Building all frontend assets */
gulp.task('build', ['assets', 'css', 'fonts', 'js']);
/* End of building all frontend assets */
