// const IS_PRODUCTION = process.env.NODE_ENV === 'production'

module.exports = {
  outputDir: 'dist',
  assetsDir: 'static',
  chainWebpack: config => {
    config.module.rules.delete('eslint');
  },
  // baseUrl: IS_PRODUCTION
  // ? 'http://cdn123.com'
  // : '/',
  // For Production, replace set baseUrl to CDN
  // And set the CDN origin to `yourdomain.com/static`
  // Whitenoise will serve once to CDN which will then cache
  // and distribute
  devServer: {
    proxy: {
      '/api': {
        // Forward frontend dev server request for /api to django dev server
        changeOrigin: true,
        ws: true,
        target: 'http://localhost:8000',
        pathRewrite: {
          '^/api': '',// 替换成target中的地址
      }
      }
    }
  }
}