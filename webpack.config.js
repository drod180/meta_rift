var path = require("path");

module.exports = {
  context: __dirname,
  entry: "./frontend/rift.jsx",
  output: {
    path: path.join(__dirname, "public", "javascript"),
    filename: "bundle.js"
  },
  resolve: {
    extensions: ["", ".js", ".jsx"]
  },
  devtool: 'source-map',
  module: {
		preloader: [
			{
				test: /\.js|\.jsx$/,
				loader: 'eslint-loader',
				include: path.join(__dirname, 'src'),
				exclude: /bundle\.js%|webpack\.config\.js$/,
			}
		]
    loaders: [
      {
        test: /\.js|\.jsx$/,
        exclude: /node_modules/,
        loader: 'babel',
        query: {
          presets: ['es2015', 'react']
        }
      },
      {
        test: /\.node$/,
        loader: "node-loader"
      }
    ]
  }
};
