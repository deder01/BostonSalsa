(function () {
    'use strict';

    angular
        .module('salsa', [
                'salsa.authentication',
                'salsa.config',
                'salsa.routes'
        ]);

    angular
        .module('salsa.routes', ['ngRoute']);

    angular
        .module('salsa.config', []);

    angular
        .module('salsa')
        .run(run);

    run.$inject = ['$http'];

    /**
     * @name run
     * @desc Update xsrf $http headers to align with Django's defaults
    */
    function run($http) {
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.defaults.xsrfCookieName = 'csrftoken';
    }

})();
