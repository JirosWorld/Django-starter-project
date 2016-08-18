Frontend best practices
===


HTML
---
* Write HTML before styling.
* Style your HTML, don’t HTML your style.
* Don’t put content in master.html, only boilerplate here.
* Inclusion tags for reusable components, blocks otherwise.
* Block for every component/logical page block/standalone section.
* Respect the coding style. (see CODINGSTYLE.md).
* If it makes sense to divert, divert.


CSS/SASS
---
* Don’t use bootstrap anymore, only for (real) prototyping.
* BEM! [(http://stackoverflow.com/...)](http://stackoverflow.com/documentation/css/5302/bem#t=201608181228046431355
* Match component (file)names to Django template blocks.
* Max 1 BEM block per file.
* Only select using (BEM) class names (.block__element), not using tag/id (Matching id's breaks reusability, matching tags breaks flexibility).
* WYSIWYG is an exception (customers don’t type content__heading--primary).
* The Block cannot set margin on itself but on children this avoids spacing issues.
* Use Bourbon/Neat for grid, don’t overdo mixins (in doubt, only use Neat for grid).
* Respect the coding style. (see bottom).
* Compile to CSS and put in GIT.
* If it makes sense to divert, divert.


JS
---
* Consider these as deprecated:
  - Bootstrap
  - Bower
  - Django Pipeline/Compressor
  - jQuery
  - RequireJS
* Match component (file)names to Django template blocks.
* ES6! (http://es6-features.org/) or newer.
* No dialects (typescript/coffeescript).
* Use a bundler (jspm/webpack) to manage dependencies/transpiling.
* Gulp is our task runner (manage.py for frontend).
* JS per Django app.
* Respect the coding style. (see CODINGSTYLE.md).
* If it makes sense to divert, divert.


Todo
---
* Dummy components scaffolding in default project. - Jorik
* Auto BEM component creator (script/gulp). - Sven
* Make Django apps all inclusive. - Sergei
* Look into alternatives for font-awesome. - Jorik
* Default gulp tasks. - Sven
* Built sample structure. - Jorik
* Make sample coding style file. - Sven (Jorik for Python)
* Testing infrastructure. - Sergei
