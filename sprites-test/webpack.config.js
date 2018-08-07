const path = require('path');
const SpritesmithPlugin = require('webpack-spritesmith');

module.export = {
  entry: path.resolve(__dirname, 'index.js'),
  output: {
    path: path.resolve(__dirname, 'build'),
    filename: 'bundle.js',
  },
  mode: 'development',
  plugins: [
    new SpritesmithPlugin({
      src: {
        cwd: path.resolve(__dirname, '/ico'),
        glob: '*.png'
      },
      target: {
        image: path.resolve(__dirname, '/assets/sprites.png'),
        css: path.resolve(__dirname, '/assets/_sprites.scss')
      },
      apiOptions: {
        cssImageRef: "~sprite.png"
      },
      spritesmithOptions: {
        algorithm: 'top-down'
      }
    })
  ]
}