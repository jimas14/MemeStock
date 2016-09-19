var app = angular.module('memeStock', ['ui.router', 'ui.bootstrap']);

app.config(function ($stateProvider, $interpolateProvider, $httpProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');

    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
});

app.controller('John', ['$scope', '$state', '$http', '$q', '$window', function ($scope, $state, $http, $q, $window) {
    $scope.login = function()
    {
        Cookies.remove('user');
        Cookies.set('user', $scope.user);

        // $http({ method: 'POST',
        //         url: '/login_info/'
        //     //data: Cookies.get('user')
        // })
        $http({
            url: "/login_info/",
            method: 'POST',
            data: { 'user' : Cookies.get('user') }
        })
        .then(function(res) {
            $window.location.href = '/investments.html';
        }, function(err) {
            console.log(err);
            console.log('woops');
        });


        // var request = $http({
        //     method: 'post',
        //     url: 'login_info/' + Cookies.get('user')
        // });
    };

}]);