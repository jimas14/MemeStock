var app = angular.module('memeStock', ['ui.router', 'ui.bootstrap']);

app.config(function ($stateProvider, $interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});

app.controller('John', ['$scope', '$state', '$window', function ($scope, $state, $window) {
    $scope.login = function()
    {
        Cookies.remove('user');
        Cookies.set('user', $scope.user);

        $window.location.href = '/investments.html';
    };
}]);