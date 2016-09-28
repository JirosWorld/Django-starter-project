SystemJS.config({
  nodeConfig: {
    "paths": {
      "npm:": "jspm_packages/npm/",
      "{{ project_name|lower }}/": "js/"
    }
  },
  devConfig: {
    "map": {
      "plugin-babel": "npm:systemjs-plugin-babel@0.0.13"
    }
  },
  transpiler: "plugin-babel",
  packages: {
    "{{ project_name|lower }}": {
      "main": "main.js",
      "format": "esm",
      "meta": {
        "*.js": {
          "loader": "plugin-babel"
        }
      }
    }
  }
});

SystemJS.config({
  packageConfigPaths: [
    "npm:@*/*.json",
    "npm:*.json",
    "github:*/*.json"
  ],
  map: {
  },
  packages: {
  }
});
