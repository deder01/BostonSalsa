/**
 * Authentication
 * @namespace salsa.authentication.services
 */

(function() {
    'use strict';

    angular
        .module('salsa.authentication.services')
        .factory('Authentication', Authentication);

    Authentication.$inject = ['$cookies', '$http', 'Snackbar'];


    /**
     * @namespace Authentication
     * @returns {Factor}
     */
    function Authentication($cookies, $http, Snackbar) {
        /**
         * @name Authentication
         * @desc The Factory to be returned
         */
        var Authentication = {
            getAuthenticatedAccount: getAuthenticatedAccount,
            isAuthenticated: isAuthenticated,
            register: register,
            login: login,
            logout: logout,
            setAuthenticatedAccount: setAuthenticatedAccount,
            unauthenticate: unauthenticate,
        };

        return Authentication

        /////////////////////
    
    /**
     * @name register
     * @desc Try to register a new user
     * @param {string} username The username entered by the user
     * @param {string} password The password entered by the user
     * @param {string} email The email entered by the user
     * @returns {Promise}
     * @memberOf thinkser.authentication.services.Authentication
     */
    function register(email, password, username) {
        return $http.post('/api/v1/accounts/', {
            username: username,
            password: password,
            email: email
        }).then(registerSuccessFn, registerErrorFn);

        function registerSuccessFn(data, status, headers, config) {
            Authentication.login(email, password);
        }

        function registerErrorFn(data, status, headers, config) {
            Snackbar.error(data.data.message);
        }
    }

    function login(email, password) {
        return $http.post('api/v1/auth/login/', {
            email: email, password: password
        }).then(loginSuccessFn, loginErrorFn);
    

        function loginSuccessFn(data, status, headers, config) {
            Authentication.setAuthenticatedAccount(data.data);

            window.location = '/';
        }

        function loginErrorFn(data, status, headers, config) {
            Snackbar.error(data.data.message);
        }
    }

    function logout() {
        return $http.post('api/v1/auth/logout/')
            .then(logoutSuccessFn, logoutErrorFn);

        function logoutSuccessFn(data, status, headers, config) {
            Authentication.unauthenticate();

            window.location = '/';
        }

        function logoutErrorFn(data, status, headers, config) {
            Snackbar.error('Epic logout fail :(');
        } 
    }

    function getAuthenticatedAccount() {
        if (!$cookies.authenticatedAccount) {
            return;
        }

        return JSON.parse($cookies.authenticatedAccount);
    }

    function isAuthenticated() {
        return !!$cookies.authenticatedAccount;
    }

    function setAuthenticatedAccount(account) {
        $cookies.authenticatedAccount = JSON.stringify(account);
    }

    function unauthenticate() {
        delete $cookies.authenticatedAccount;
    }
  }
})();
