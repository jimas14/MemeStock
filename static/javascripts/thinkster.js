// angular.module('abc', []).controller('john', [$scope, $interpolateProvider,
//
//     function($scope, $interpolateProvider) {
//     console.log('ff');
//         $interpolateProvider.startSymbol('{[{');
//       $interpolateProvider.endSymbol('}]}');
//         $scope.a = 4;
//
//
// }]);

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

app.controller('john', function ($scope) {
    $scope.a = 4;
});