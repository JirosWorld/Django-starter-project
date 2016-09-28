/**
 * global expect, jasmine, setFixtures
 */

import {MESSAGE} from '{{ project_name|lower }}/components/message.js';


describe('The message module', () => {

    beforeEach(() => {

        setFixtures(
            "<div class=\"a-fixture\">Hello, I am an HTML fixture to test DOM operations</div>"
        );

    });

    it('exports a default message', () => {
        expect(MESSAGE).toBe('I was dynamically loaded');
    });

    it('has a failing test', () => {
        expect(true).toBe(false);
    });

});
