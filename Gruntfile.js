"use strict";

module.exports = function (grunt) {
    var appConfig = {
        static: "base/static",
    };

    grunt.initConfig({
        pkg: grunt.file.readJSON("package.json"),

        app: appConfig,

        copy: {
            main: {
                files: [{
                    expand: true,
                    cwd: "bower_components/bootstrap/js/",
                    src: ["**"],
                    dest: "<%= app.static %>/js/bootstrap/"
                }, {
                    expand: true,
                    cwd: "bower_components/bootstrap/less/",
                    src: ["**"],
                    dest: "<%= app.static %>/less/bootstrap/"
                }, {
                    expand: true,
                    cwd: "bower_components/bootstrap/less/",
                    src: ["variables.less"],
                    dest: "<%= app.static %>/less/"
                }, {
                    expand: true,
                    cwd: "bower_components/font-awesome/less/",
                    src: ["**"],
                    dest: "<%= app.static %>/less/font-awesome/"
                }, {
                    expand: true,
                    cwd: "bower_components/font-awesome/fonts/",
                    src: ["**"],
                    dest: "<%= app.static %>/fonts/font-awesome/"
                }, {
                    expand: true,
                    cwd: "bower_components/jquery/dist/",
                    src: ["jquery.js"],
                    dest: "<%= app.static %>/js/libs/"
                }, {
                    expand: true,
                    cwd: "bower_components/modernizr/",
                    src: ["modernizr.js"],
                    dest: "<%= app.static %>/js/libs/"
                }, {
                    expand: true,
                    cwd: "bower_components/respond/",
                    src: ["respond.src.js"],
                    dest: "<%= app.static %>/js/libs/"
                }, {
                    expand: true,
                    cwd: "bower_components/holderjs/",
                    src: ["holder.js"],
                    dest: "<%= app.static %>/js/libs/"
                }, {
                    expand: true,
                    cwd: "bower_components/SVGMagic/src/",
                    src: ["SVGMagic.js"],
                    dest: "<%= app.static %>/js/libs/"
                }, {
                    expand: true,
                    cwd: "bower_components/fancybox/source/",
                    src: ["jquery.fancybox.js"],
                    dest: "<%= app.static %>/js/libs/"
                }, {
                    expand: true,
                    cwd: "bower_components/fancybox/source/",
                    src: ["jquery.fancybox.css"],
                    dest: "<%= app.static %>/css/fancybox/"
                }, {
                    expand: true,
                    cwd: "bower_components/fancybox/source/",
                    src: ["fancybox_loading.gif"],
                    dest: "<%= app.static %>/css/fancybox/"
                }, {
                    expand: true,
                    cwd: "bower_components/fancybox/source/",
                    src: ["fancybox_loading@2x.gif"],
                    dest: "<%= app.static %>/css/fancybox/"
                }, {
                    expand: true,
                    cwd: "bower_components/fancybox/source/",
                    src: ["fancybox_overlay.png"],
                    dest: "<%= app.static %>/css/fancybox/"
                }, {
                    expand: true,
                    cwd: "bower_components/fancybox/source/",
                    src: ["fancybox_sprite.png"],
                    dest: "<%= app.static %>/css/fancybox/"
                }, {
                    expand: true,
                    cwd: "bower_components/fancybox/source/",
                    src: ["fancybox_sprite@2x.png"],
                    dest: "<%= app.static %>/css/fancybox/"
                }]
            }
        }
    });

    grunt.loadNpmTasks("grunt-contrib-copy");

    grunt.registerTask("build", [
        "copy"
    ]);

};
