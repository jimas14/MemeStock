var app = angular.module('memeStock');

app.config(function ($stateProvider, $interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});

app.controller('LoginController', ['$scope', '$http', '$q', '$state', function ($scope, $http, $q, $state) {


}]);