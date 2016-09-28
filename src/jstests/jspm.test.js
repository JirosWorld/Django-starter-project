SystemJS.config({
  packages: {
    "{{ project_name|lower }}": {
      // the Babel pre-processor transpiles the ESM modules into CJS already,
      // so we no longer need to define a loader to use (let systemjs figure it
      // out by itself)
      "format": "cjs",
      "meta": {
        "*.js": {
          "loader": null,
        }
      }
    }
  }
});
