var gulp = require("gulp");
var print = require("gulp-print");
var sass = require("gulp-sass");
var concat = require("gulp-concat");
var shell = require("gulp-shell");
var removeCode = require("gulp-remove-code");
var clean = require("gulp-clean");
var cleanCSS = require("gulp-clean-css");
var rename = require("gulp-rename");
var uglify = require("gulp-uglify");
var runSequence = require("run-sequence");
var replace = require("gulp-replace");

gulp.task("watch", function () {
    gulp.watch("src/**/*.scss", ["make_css_bundle"]);
    gulp.watch("src/**/*.js", ["make_js_bundle"]);
    gulp.watch("src/**/*.html", ["refresh_page"]);
    gulp.watch("build/static/**/*.css", ["refresh_page"]);
    gulp.watch("build/static/**/*.js", ["refresh_page"]);
    gulp.watch("build/static/**/*.html", ["refresh_page"]);
    gulp.watch("src/**/*.py", function () {
        delay(750);
        runSequence("refresh_page");
    });
});

gulp.task("make_css_bundle", function () {
    return gulp.src([
        "bower_components/bootstrap/dist/css/bootstrap.css",
        "src/front_bombril/utils.scss",
        "src/blueprints/wrappers/base/static/scss/base.scss",
        "src/**/*.scss"
    ])
        .pipe(concat("bundle.css"))
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest("build/static/css"));
});

gulp.task("make_js_bundle", function () {
    return gulp.src([
        "bower_components/jquery/dist/jquery.js",
        "bower_components/bootstrap/dist/js/bootstrap.js",
        "src/front_bombril/utils.js",
        "src/**/*.js"
    ])
        .pipe(concat("bundle.js"))
        .pipe(gulp.dest("build/static/js"));
});

gulp.task("refresh_page", shell.task([
    "./scripts/utils/refresh_page.sh"
]));

gulp.task("build", function (callback) {
    runSequence(
        "delete_old_build",
        ["copy_html_files_to_build_dir", "copy_py_files_to_build_dir", "make_css_bundle", "make_js_bundle"],
        ["minify_css_bundle", "minify_js_bundle"],
        callback);
});

gulp.task("delete_old_build", function () {
    return gulp.src("build", {read: false})
        .pipe(clean());
});

gulp.task("copy_html_files_to_build_dir", function () {
    return gulp.src(["src/**/*.html"])
        .pipe(removeCode({production: true}))
        .pipe(replace("bundle.css", "bundle.min.css"))
        .pipe(replace("bundle.js", "bundle.min.js"))
        .pipe(gulp.dest("build"));
});

gulp.task("copy_py_files_to_build_dir", function () {
    return gulp.src(["src/**/*.py"])
        .pipe(gulp.dest("build"));
});

gulp.task("minify_css_bundle", function () {
    return gulp.src("build/static/css/bundle.css")
        .pipe(cleanCSS({compatibility: "ie8"}))
        .pipe(rename({
            suffix: ".min"
        }))
        .pipe(gulp.dest("build/static/css"));
});

gulp.task("minify_js_bundle", function () {
    return gulp.src("build/static/js/bundle.js")
        .pipe(uglify())
        .pipe(rename({
            suffix: ".min"
        }))
        .pipe(gulp.dest("build/static/js"));
});

function delay(delayTime) {
    var releaseTime = (new Date()).getTime() + delayTime;
    while ((new Date()).getTime() < releaseTime) {
    }
}
