var app = angular.module('memeStock');

app.config(function ($stateProvider, $interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});

app.controller('LoginController', ['$scope', '$state', function ($scope, $state) {
    console.log('reached login controller');
}]);