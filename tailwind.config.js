/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './template/**/*.html',
    './static/js/**/*.js',
    './static/library/flowbite/**/*.js',
    './static/library/preline/dist/*.js',
    './dashboard/**/*.py',
  ],
  darkMode: 'class',
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin'),
    require('preline/plugin')
  ],
}
