/**
 * global expect, jasmine
 */

import {MESSAGE} from '{{ project_name|lower }}/components/message.js';


describe('The message module', () => {

    it('exports a default message', () => {
        expect(MESSAGE).toBe('I was dynamically loaded');
    });

    it('has a failing test', () => {
        expect(true).toBe(false);
    });

});
