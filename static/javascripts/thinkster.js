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

var app = angular.module('abc', []);

app.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});

app.controller('john', function($scope) {
    $scope.a = 4;
});