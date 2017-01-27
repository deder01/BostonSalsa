/**
 * Register controller
 * @namespace salsa.authentication.controllers
 */
(function () {
    'use stric';

    angular
        .module('salsa.authentication.controllers')
        .controller('RegisterController', RegisterController);

    RegisterController.$inject = ['$location', '$scope', 'Authentication'];

    /**
     * @namespace RegisterController
     */
    function RegisterController($location, $scope, Authentication) {
        var vm = this;
        console.log('hello')

        vm.register = register;

        activate();

        function activate() {
            // If the user is authenticated they should not be here
            if (Authentication.isAuthenticated()) {
                $location.url('/');
            }
        }

        /**
         * @name register
         * @desc register a new user
         * @memberOf salsa.authentication.controllers.RegisterController
         */
        function register() {
            Authentication.register(vm.email, vm.password, vm.username);
        }
    }
})();
