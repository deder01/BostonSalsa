(function () {
    'use strict';

    angular
        .module('salsa.authentication', [
                'salsa.authentication.controllers',
                'salsa.authentication.services'
        ]);

    angular
        .module('salsa.authentication.controllers', []);

    angular
        .module('salsa.authentication.services', ['ngCookies']);
})();
