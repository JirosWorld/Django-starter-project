SystemJS.config({
  transpiler: "plugin-babel",
  babelOptions: {
    "optional": [
      "runtime",
      "optimisation.modules.system"
    ]
  },
  map: {
    "babel": "npm:babel-core@5.8.38"
  },
  packages: {
    "{{ project_name|lower }}": {
      "format": "esm",
      "main": "main.js"
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
    "babel-runtime": "npm:babel-runtime@5.8.38",
    "core-js": "npm:core-js@1.2.6",
    "fs": "github:jspm/nodelibs-fs@0.2.0-alpha",
    "jquery": "npm:jquery@2.2.3",
    "path": "github:jspm/nodelibs-path@0.2.0-alpha",
    "plugin-babel": "npm:systemjs-plugin-babel@0.0.9",
    "process": "github:jspm/nodelibs-process@0.2.0-alpha"
  },
  packages: {
    "npm:babel-runtime@5.8.38": {
      "map": {}
    },
    "npm:core-js@1.2.6": {
      "map": {
        "systemjs-json": "github:systemjs/plugin-json@0.1.0"
      }
    }
  }
});
