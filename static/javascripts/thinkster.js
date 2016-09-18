var app = angular.module('memeStock', ['ui.router', 'ui.bootstrap']);

app.config(function ($stateProvider, $interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');

    var bruhState = {
        name: 'bruh',
        url: '/bruh',
        template: '<h3>bruh</h3>'
    };

    $stateProvider.state(bruhState);
});

app.controller('john', ['$scope', '$state', function ($scope, $state) {
    $scope.a = 4;
    $state.go('bruh');
}]);