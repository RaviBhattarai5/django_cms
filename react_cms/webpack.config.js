// webpack.config.js
const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  entry: {
    main: './src/index.js'
  },
  output: {
    path: path.resolve(__dirname, 'static', 'react_cms'),  // Directory path
    filename: 'main.js',                                  // Just the filename
    publicPath: 'http://localhost:3000/static/react_cms/'
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env', '@babel/preset-react']
          }
        }
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader']
      }
    ]
  },
  plugins: [
    new BundleTracker({
      path: __dirname,
      filename: 'webpack-stats.json'    // Stats file in root of frontend directory
    })
  ],
  devServer: {
    port: 3000,
    hot: true,
    headers: {
      "Access-Control-Allow-Origin": "*"
    },
  }
}