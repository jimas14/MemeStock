var app = angular.module('memeStock', ['ui.router', 'ui.bootstrap']);

app.config(function ($stateProvider, $interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});

app.controller('John', ['$scope', '$state', '$http', '$q', '$window', function ($scope, $state, $http, $q, $window) {
    $scope.login = function()
    {
        Cookies.remove('user');
        Cookies.set('user', $scope.user);

        var request = $http({
            method: 'post',
            url: 'login_info',
            data: Cookies.get('user')
        });

        request.then(function(res) {
            $window.location.href = '/investments.html';
        }, function(err) {
            console.log('woops');
        });


    };

}]);