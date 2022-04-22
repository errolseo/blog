module.exports = function(grunt) {
  grunt.config.set('clean', {
    // Delete the `assets` folder
    build: ['static'],
    release: [
      'static/css/*',
      '!static/css/style-*.min.css',
      'static/js/*',
      '!static/js/script-*.min.js'
    ]
  });
  grunt.loadNpmTasks('grunt-contrib-clean');
};
