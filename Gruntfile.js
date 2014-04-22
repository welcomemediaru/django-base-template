"use strict";

module.exports = function (grunt) {

    grunt.initConfig({
        pkg: grunt.file.readJSON("package.json"),

        copy: {
            main: {
                files: [{
                    expand: true,
                    cwd: "bower_components/bootstrap/js/",
                    src: ["**"],
                    dest: "base/static/js/bootstrap/"
                }, {
                    expand: true,
                    cwd: "bower_components/bootstrap/less/",
                    src: ["**"],
                    dest: "base/static/less/bootstrap/"
                }, {
                    expand: true,
                    cwd: "bower_components/font-awesome/less/",
                    src: ["**"],
                    dest: "base/static/less/font-awesome/"
                }, {
                    expand: true,
                    cwd: "bower_components/font-awesome/fonts/",
                    src: ["**"],
                    dest: "base/static/fonts/font-awesome/"
                }, {
                    expand: true,
                    cwd: "bower_components/jquery/dist/",
                    src: ["jquery.js"],
                    dest: "base/static/js/libs/"
                }, {
                    expand: true,
                    cwd: "bower_components/modernizr/",
                    src: ["modernizr.js"],
                    dest: "base/static/js/libs/"
                }, {
                    expand: true,
                    cwd: "bower_components/respond/",
                    src: ["respond.src.js"],
                    dest: "base/static/js/libs/"
                }, {
                    expand: true,
                    cwd: "bower_components/holderjs/",
                    src: ["holder.js"],
                    dest: "base/static/js/libs/"
                }]
            }
        }
    });

    grunt.loadNpmTasks("grunt-contrib-copy");

    grunt.registerTask("build", [
        "copy"
    ]);

};
