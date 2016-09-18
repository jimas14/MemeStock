var app = angular.module('memeStock', ['ui.router', 'ui.bootstrap']);

app.config(function ($stateProvider, $interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');

    var loginState = {
        name: 'login',
        url: '/login',
        template: '<button type="button" class="btn btn-primary" ng-model="s" uib-btn-checkbox btn-checkbox-true="1"> dsd</button>'
        // templateUrl: '../templates/login.html',
        // controller: 'LoginController'
    };

    $stateProvider.state(loginState);
});

app.controller('john', ['$scope', '$state', function ($scope, $state) {
    $state.go('login');
}]);