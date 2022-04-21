module.exports = function(grunt) {
  grunt.config.set('clean', {
    // Delete the `assets` folder
    build: ['static'],
    release: ['static/css/*', '!static/css/style-*', 'static/js/*', '!static/js/script-*']
  });
  grunt.loadNpmTasks('grunt-contrib-clean');
};
