/**
 * Example module
 * @module
 */


/**
 * Example class
 * @class
 */
class Example {
    /**
     * Constructor method
     * Gets called when class get instantiated
     */
    constructor() {
        console.log(this.sum(1, 1));
    }

    /**
     * Returns the sum of a + b
     * @param {number} a
     * @param {number} b
     * @returns {number}
     */
    sum(a, b) {
        return a + b;
    }
}



module.hot.accept();  // https://webpack.github.io/docs/hot-module-replacement.html
new Example();  // Initiate this module
