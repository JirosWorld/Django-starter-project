# Code styling

1. [HTML](#html-coding-style)
2. [SASS](#sass-coding-style)
3. [JavaScript](#javascript-coding-style)


## HTML coding style

* Common: Inline style is evil.
    ```html
    <p style="color: red;">
    Inline style cannot be cached.<br />
    Inline style is difficult to overwrite.<br />
    Inline style makes HTML less readable.<br />
    Inline style is harder to spot.<br />
    </p>
    ```
* Common: Inline script is evil (except Google Analytics).
    ```html
    <script>
        console.log('Inline script cannot be cached.');
        console.log('Inline script makes HTML less readable.');
        console.log('Inline script blocks loading of page.');
    </script>
    ```
* Common: Style your HTML, don’t HTML your style (avoid adding div’s for style).
    ```html
    <div class="wrapper">
        <div class="inner">
            <div class="content">
                <p class="text>
                    All these tags have no acutual meaning.<br />
                    Consider HTML as data model, it should represent data, not style placeholders.<br />
                    Good practice is to write you HTML first, based on the structure of the content, then style.<br />
                    It's almost never needed to add more tags, have tried :before and :after yet?<br />
                </p>
            </div>
        </div>
    </div>
    ```
* Indent: 4 spaces.
    ```html
    <html>
        <body>
        </body>
    </html>
    ```
* Indent: Indent HTML and template tags. (except {% block %} on root level).
    ```html
    {% block content %}
    <article>
        {% if show_header %}
            {% block article__header %}
                <header>
                </header>
            {% endblock article__header %}
        {% endif %}
    </article>
    {% endblock content %}
    ```
* Data: (Meta)data should be stored in data- attributes.
    ```html
    <article data-article-id="1"></article>
    ```
* Data: Variables should be passed, using data-attributes as well, no excuse for inline script.
    ```html
    <article data-some-variable="1"></article>
    ```
* Element: Avoid id (as much as possible).
    ```html
    <article id="article-1" />  <!-- wrong -->
    <article class="article" data-id="1" /> <!-- better -->
    ```
* Element: Use semantic tags (<main> <nav /> <article> <section /> </article> <aside /> <footer /> etc.)
    ```html
    <main>
        <nav>
        </nav>

        <article>
            <section>
            </section>
        </article>

        <footer>
        </footer>
    </main>
    ```

## SASS coding style

* Common: Readability first.
* Common: Annotate when useful.
* Global: Global styling is evil (consider it as bad as eval).
* Global: Global configuration should be limited to:
    - Grid
    - Breakpoints
    - Colors
    - Fonts
* Indent: 2 spaces.
    ```scss
    .block {
      width: 100%;
    }
    ```
* Nest: Namespace (nest) by (BEM) block.
    ```scss
    .block {
      // Everything should be nested inside .block
      // This makes sure nothing "bleeds" to global scope
      .block__element {
      }
    }
    ```
* Nest: Max 3 levels.
    ```scss
    .block {             // One
      .block__element {  // Two
        &:hover {        // Three
          color: #0000FF;
        }
      }
    }
    ```
* Newline: 1 Empty newline after mixin/variable block.
    ```scss
    .block__element-one {
    }

    .block__element-two {
    }
    ```
* Newline: Empty newline at the end of the file.
* Order: Block > block modifier, element > element modifier.
    ```scss
    .block {  // .block is the basic element
      &.block--active {  // --active is the modifier for .block, and should be grouped with .block
      }

      .block__element {  // __element is a child element dependent on .block
      }

      .block__element--disabled {  // --disabled is the modifier for .block__element, and should be grouped with .block__element
      }
    }
    ```
* Order: Mixins first at all times, aim for grouped attributes.
    ```scss
    .block {
      @include text(18px, 40px);  // Mixins go first so we can overide it's side effects
      background: #000;
      color: #FFF;
    }
    ```
* Selector: Use BEM class naming.
    ```scss
    // BEM (Block, Element, Modifier) is a structured naming convention for CSS classes
    // A double underscore (__) separates the element from a block
    // A double dash (--) separates the modifier from the block or element
    // These fixed patters make it also possible to be parsed by (JavaScript) code

    .block {  // A block describes a standalone component
      &.block--modifier {  // A modifier describes a state or theme for eithe a block or an element
      }

      .block__element {  // An element is a component that depends on a block
      }

      .block__element--modifier {  // This modifier desrcibes the state or theme for an element
      }
    }
    ```
* Selector: Max 1 BEM block per file.
    ```scss
    .block {  // That's it, no more blocks in this file
    }
    ```
* Selector: Only select using (BEM) class names (.block__element), not using tag/id.
    ```scss
    div {  // Bad, tags may change an that would break our code
    }

    article { // Also bad, event semantic (descriptive) tags may change
    }

    h1 {  // Also bad, a marketeer may drop in and ask you to change it into an h2 (design will break and designer will be mad)
    }

    #content {  // Bad, we can't repeat this anymore because id's must be unique
    }

    .content {  // Better, content is our block
      .content__heading {  // Better, content__heading is a valid class name for an h1, or h2 in block content
      }
      .content__body {  // This could be a class name for a paragraph in block content
      }
    }

    .wysiwyg-content {
      h1 {  // Accaptable exception, we don't expect customers to adhere to BEM
      }
    }
    ```
* Variable: Privatize variables by assigning them on top of the module.
    ```scss
    $article-color: $color;  // We copy the contents of a global variable into a private one
    $article-font: $font;    // This allow us easily "fix" the values and reuse our component

    .article {
      color: $article-color;  // We use private values here
      font-family: $article-font;
    }
    ```

## JavaScript coding style

* Common: Readability first.
* Common: Annotate when useful.
    ```js
    /**
     * Helper method to add an additional class name with a specific modifier (--modifier) to a BEM (Block Element Modifier) element
     * A modifier class is created for each of the existing class names
     * Class names containing "--" (modifier pattern) are discarded
     * Double class names are prevented
     * @param {HTMLElement} node The block/element to append the class name to (block, block__element)
     * @param {String} modifier The name of the modifier (--name)
     */
    function addModifier(node, modifier) {
    }
    ```
* Class: Use TitledCamelCase names.
    ```js
    class Header {  // Bonus points: match class to BEM block name
    }
    ```
* Conditional: space between operator and brackets.
    ```js
    if (foo === 'bar') {
    }
    ```
* Constant: use const keyword.
* Constant: Use UPPERCASE_CONSTANT names.
    ```js
    const MY_AWESOME_CONSTANT = 'foo';
    ```
* Event listener: Separate wiring from logic.
    ```js
    /**
     * We separate "wiring" from the main logic so we can resure the logic
     */
    setUpOpen() {
        BUTTON_OPEN.addEventListener('click', this.open.bind(this));
    }

    /**
     * We can now reuse this
     */
    open() {
    }
    ```
* Function: Use camelCase names.
* Function: no space between function and brackets.
* Function: newline after bracket.
    ```js
    function doFooBar() {
    }
    ```
* Indent: 4 spaces.
    ```js
    function doFooBar() {
        console.log('indent', 4, 'spaces');
    }
    ```
* Line break: 79 soft limit, 119 hard limit.
* Newline: No empty newline after logical block.
    ```js
    function doFooBar() {

        // ^ Bad, keep related code together
        console.log('indent', 4, 'spaces');
    }
    ```
* Newline: 1 Empty newline after method/variable block.
    ```js
    function doFooBar() {
        var fooBar = 'foobar';

        console.log(fooBar);
    }
    ```
* Newline: 2 Empty newlines after top level function/class/block.
    ```js
    const FOO = 'foo';
    const BAR = 'bar';


    function doFooBaz() {  // 2 Empty newlines after a block of constants
        console.log('foobaz');
    }


    class Foo {  // 2 Empty newlines after a top level function
        constructor() {
            super();
            this.doBar();
        }

        doBar() {  // 1 Empty newline after method
            var bar = new Bar();
        }
    }


    class Bar {   // 2 Empty newlines after a class
        constructor() {
            super();
            this.doBar();
        }

        doBar() {
            var bar = new Bar();
        }
    }
    ```
* Newline: Empty newline at the end of the file.
* Variable: Use let keyword.
* Variable: Group together.
* Variable: Use camelCase names.
    ```js
    function doFooBar() {
        let foo = 'foo',
            bar = 'bar',
            fooBar = foo+bar;
        console.log(fooBar);
    }
    ```
* Test: Use foo.spec.js filenames.
    ```shell
    foo.spec.js  // .spec tells us it's a test suite, .js lets us know it's js file.
    ```
