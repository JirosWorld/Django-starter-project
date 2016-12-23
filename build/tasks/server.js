var gulp = require('gulp');
var webpack = require('webpack');
var paths = require('../paths');
var webpackConfig = require('../../webpack.config.js');

var WebpackDevServer = require("webpack-dev-server");


/**
 * Js task
 * Run using "gulp js"
 * Runs webpack to compile javascript
 */
gulp.task('server', function() {
    webpackConfig.entry.unshift(
        "webpack-dev-server/client?http://localhost:8080",
        "webpack/hot/only-dev-server"
    );
    webpackConfig.plugins = [
        new webpack.HotModuleReplacementPlugin(),
        new webpack.NamedModulesPlugin()
    ];
    var compiler = webpack(webpackConfig);
    server = new WebpackDevServer(compiler, {
        hot: true,
        publicPath: "/static/js/",
        proxy: {
            '/': {
                target: 'http://localhost:8000/',
                secure: false,
                bypass: function(request, response, proxyOptions) {
                    if (request.path.startsWith('/static/js/')) {
                        return request.path;
                    } else if (request.path.indexOf('hot-update') > 0) {
                        // ugly hack, but publicPath is not properly supported :/
                        return '/static/js' + request.path;
                    }
                    return false;
                }
            }
        }
    });
    server.listen(8080);
});
