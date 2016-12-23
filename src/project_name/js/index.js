import 'components/menu';
import Menu from 'components/menu';


describe('menu', function() {
    it('should be able to import "Menu" class', () => {
        expect(Menu).toBeTruthy();
    });
});


// check if HMR is enabled
if (module.hot) {
    module.hot.accept();
}
