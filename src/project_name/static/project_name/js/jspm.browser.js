SystemJS.config({
  baseURL: "/static/",
  paths: {
    "github:*": "jspm_packages/github/*",
    "npm:*": "jspm_packages/npm/*",
    "{{ project_name|lower }}/": "{{ project_name|lower }}/"
  }
});
