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
var mkdirp = require('mkdirp');
var insert = require('gulp-insert');

gulp.task("watch", function () {
    gulp.watch("src/**/*.scss", ["make_css_bundles"]);
    gulp.watch("src/**/*.js", ["make_js_bundles"]);
    gulp.watch("src/**/*.html", ["refresh_page"]);
    gulp.watch("build/static/**/*.css", ["refresh_page"]);
    gulp.watch("build/static/**/*.js", ["refresh_page"]);
    gulp.watch("src/**/*.py", function () {
        delay(750);
        runSequence("refresh_page");
    });
});

gulp.task("make_css_bundles", function (callback) {
    runSequence(
        ["make_admin_css_bundle", "make_client_css_bundle"],
        callback);
});

gulp.task("make_admin_css_bundle", function(){
    return gulp.src([
        "bower_components/bootstrap/dist/css/bootstrap.css",
        "bower_components/eonasdan-bootstrap-datetimepicker/build/css/bootstrap-datetimepicker.css",
        "bower_components/toastr/toastr.css",
        "src/front_bombril/utils.scss",
        "src/wrappers/base/**/*.scss",
        "src/wrappers/admin_base/**/*.scss",
        "src/components/**/*.scss",
        "src/routers/admin_attended_cities/**/*.scss",
        "src/routers/admin_blog/**/*.scss",
        "src/routers/admin_clients/**/*.scss",
        "src/routers/admin_content/**/*.scss",
        "src/routers/admin_home/**/*.scss",
        "src/routers/admin_images/**/*.scss",
        "src/routers/admin_orders/**/*.scss",
        "src/routers/admin_products/**/*.scss",
        "src/routers/admin_utils/**/*.scss"
    ])
        .pipe(concat("admin_bundle.css"))
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest("build/static/css"));
});

gulp.task("make_client_css_bundle", function(){
    return gulp.src([
        "bower_components/bootstrap/dist/css/bootstrap.css",
        "bower_components/toastr/toastr.css",
        "bower_components/flipmart-v5/css/font-awesome.css",
        "bower_components/flipmart-v5/css/revslider.css",
        "bower_components/flipmart-v5/css/owl.carousel.css",
        "bower_components/flipmart-v5/css/owl.theme.css",
        "bower_components/flipmart-v5/css/jquery.bxslider.css",
        "bower_components/flipmart-v5/css/jquery.mobile-menu.css",
        "bower_components/flipmart-v5/css/style.css",
        "bower_components/flipmart-v5/css/flexslider.css",
        "bower_components/flipmart-v5/css/responsive.css",
        "bower_components/components-font-awesome/css/font-awesome.css",
        "bower_components/bootstrap-social/bootstrap-social.css",
        "src/front_bombril/utils.scss",
        "src/wrappers/base/**/*.scss",
        "src/wrappers/client_base/**/*.scss",
        "src/components/**/*.scss",
        "src/routers/client_about_us/**/*.scss",
        "src/routers/client_account/**/*.scss",
        "src/routers/client_blog/**/*.scss",
        "src/routers/client_cart/**/*.scss",
        "src/routers/client_checkout/**/*.scss",
        "src/routers/client_faq/**/*.scss",
        "src/routers/client_home/**/*.scss",
        "src/routers/client_products/**/*.scss",
        "src/routers/client_user_management/**/*.scss"
    ])
        .pipe(concat("client_bundle.css"))
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest("build/static/css"));
});

gulp.task("make_js_bundles", function (callback) {
    runSequence(
        ["make_admin_js_bundle", "make_client_js_bundle"],
        callback);
});

gulp.task("make_admin_js_bundle", function () {
    return gulp.src([
        "bower_components/jquery/dist/jquery.js",
        "bower_components/moment/min/moment-with-locales.js",
        "bower_components/bootstrap/dist/js/bootstrap.js",
        "bower_components/eonasdan-bootstrap-datetimepicker/src/js/bootstrap-datetimepicker.js",
        "bower_components/bootstrap-filestyle/src/bootstrap-filestyle.js",
        "bower_components/toastr/toastr.js",
        "src/front_bombril/utils.js",
        "src/wrappers/base/**/*.js",
        "src/wrappers/admin_base/**/*.js",
        "src/components/**/*.js",
        "src/routers/admin_attended_cities/**/*.js",
        "src/routers/admin_blog/**/*.js",
        "src/routers/admin_clients/**/*.js",
        "src/routers/admin_content/**/*.js",
        "src/routers/admin_home/**/*.js",
        "src/routers/admin_images/**/*.js",
        "src/routers/admin_orders/**/*.js",
        "src/routers/admin_products/**/*.js",
        "src/routers/admin_utils/**/*.js"
    ])
        .pipe(concat("admin_bundle.js"))
        .pipe(gulp.dest("build/static/js"));
});

gulp.task("make_client_js_bundle", function () {
    return gulp.src([
        "bower_components/jquery/dist/jquery.js",
        "bower_components/bootstrap/dist/js/bootstrap.js",
        "bower_components/toastr/toastr.js",
        "bower_components/flipmart-v5/js/parallax.js",
        "bower_components/flipmart-v5/js/revslider.js",
        "bower_components/flipmart-v5/js/common.js",
        "bower_components/flipmart-v5/js/jquery.bxslider.min.js",
        "bower_components/flipmart-v5/js/jquery.flexslider.js",
        "bower_components/flipmart-v5/js/cloud-zoom.js",
        "bower_components/flipmart-v5/js/countdown.js",
        "bower_components/flipmart-v5/js/owl.carousel.min.js",
        "bower_components/flipmart-v5/js/jquery.mobile-menu.min.js",
        "bower_components/bignumber.js/bignumber.js",
        "src/front_bombril/utils.js",
        "src/wrappers/base/**/*.js",
        "src/wrappers/client_base/**/*.js",
        "src/components/**/*.js",
        "src/routers/client_about_us/**/*.js",
        "src/routers/client_account/**/*.js",
        "src/routers/client_blog/**/*.js",
        "src/routers/client_cart/**/*.js",
        "src/routers/client_checkout/**/*.js",
        "src/routers/client_faq/**/*.js",
        "src/routers/client_home/**/*.js",
        "src/routers/client_products/**/*.js",
        "src/routers/client_user_management/**/*.js"
    ])
        .pipe(concat("client_bundle.js"))
        .pipe(gulp.dest("build/static/js"));
});

gulp.task("refresh_page", shell.task([
    "./scripts/utils/refresh_page.sh"
]));

gulp.task("build", function (callback) {
    runSequence(
        "delete_old_build",
        ["copy_html_files_to_build_dir", "copy_py_files_to_build_dir", "make_css_bundles", "make_js_bundles", "copy_fonts_to_build_dir", "copy_flipmart_fonts_to_build_dir", "copy_images_to_build_dir"],
        ["minify_admin_css_bundle", "minify_admin_js_bundle", "minify_client_css_bundle", "minify_client_js_bundle"],
        ["append_sys_path_to_build_init"],
        callback
    );
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

gulp.task("copy_images_to_build_dir", function () {
    return gulp.src(["debug_images/*"])
        .pipe(gulp.dest("build/static/imgs"));
});

gulp.task("copy_py_files_to_build_dir", function () {
    return gulp.src(["src/**/*.py"])
        .pipe(gulp.dest("build"));
});

gulp.task("append_sys_path_to_build_init", function () {
    return gulp.src(["build/__init__.py"])
        .pipe(insert.append('import sys\nsys.path.append("/vagrant")\nsys.path.append("/vagrant/build")\n'))
        .pipe(gulp.dest("build"));
});

gulp.task("copy_fonts_to_build_dir", function () {
    return gulp.src([
        "bower_components/bootstrap/dist/fonts/*",
        "bower_components/components-font-awesome/fonts/*",
        "fonts/**/*.*"
    ])
        .pipe(gulp.dest("build/static/fonts"));
});

gulp.task("copy_flipmart_fonts_to_build_dir", function () {
    return gulp.src(["bower_components/flipmart-v5/fonts/*"])
        .pipe(gulp.dest("build/static/fonts"));
});

gulp.task("minify_admin_css_bundle", function () {
    return gulp.src("build/static/css/admin_bundle.css")
        .pipe(cleanCSS({compatibility: "ie8"}))
        .pipe(rename({
            suffix: ".min"
        }))
        .pipe(gulp.dest("build/static/css"));
});

gulp.task("minify_client_css_bundle", function () {
    return gulp.src("build/static/css/client_bundle.css")
        .pipe(cleanCSS({compatibility: "ie8"}))
        .pipe(rename({
            suffix: ".min"
        }))
        .pipe(gulp.dest("build/static/css"));
});

gulp.task("minify_admin_js_bundle", function () {
    return gulp.src("build/static/js/admin_bundle.js")
        .pipe(uglify())
        .pipe(rename({
            suffix: ".min"
        }))
        .pipe(gulp.dest("build/static/js"));
});

gulp.task("minify_client_js_bundle", function () {
    return gulp.src("build/static/js/client_bundle.js")
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

gulp.task("test", function(){
    return gulp.src([
        "bower_components/flipmart-v5/css/flexslider.css",
        "bower_components/flipmart-v5/css/font-awesome.css",
        "bower_components/flipmart-v5/css/jquery.bxslider.css",
        "bower_components/flipmart-v5/css/jquery.mobile-menu.css",
        "bower_components/flipmart-v5/css/owl.carousel.css",
        "bower_components/flipmart-v5/css/owl.theme.css",
        "bower_components/flipmart-v5/css/responsive.css",
        "bower_components/flipmart-v5/css/revslider.css",
        "bower_components/flipmart-v5/css/style.css"
    ])
        .pipe(concat("client_bundle.css"))
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest("build/static/css"));
});