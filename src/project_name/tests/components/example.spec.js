import Example from 'components/example';


describe('Example', function() {
    it('should be able to import "Example" class', () => {
        expect(Example).toBeTruthy();
    });

    it('should return 2 when calling sum with 1 and 1', () => {
        let example = new Example();
        expect(example.sum(1, 1)).toBe(2);
    });
});
