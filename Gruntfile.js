/* global module:false, require:false */

"use strict";

module.exports = function (grunt) {
    var appConfig = {
        static: "base/static",
    };

    require("jit-grunt")(grunt);

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
                    cwd: "bower_components/SVGMagic/src/",
                    src: ["jquery.svgmagic.js"],
                    dest: "<%= app.static %>/js/libs/"
                }]
            }
        }
    });

    grunt.registerTask("build", [
        "copy"
    ]);
};
