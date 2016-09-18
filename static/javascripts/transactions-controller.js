var app = angular.module('memeStock');

app.config(function ($stateProvider, $interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');

});

app.controller('TransactionsController', ['$scope', '$http', '$q', '$state', function ($scope, $http, $q, $state) {
    console.log('fdf');
    function getAllStocks()
    {
        var request = $http({
            method: 'get',
            url: 'stocks'
        });

        return request.then(handleSuccess, handleFailure);
    }

    $scope.populateStocks = function()
    {
        getAllStocks().then(function(result) {
            if (null != result)
            {
                $scope.allStocks = result.stocks;
            }
        }, function(err) {
            console.log('bruh something went wrong');
        });
    };

    function handleSuccess(response)
    {
        return response.data;
    }

    function handleFailure(response)
    {
        if (!angular.isObject( response.data ) || null == response.data.message){
            return( $q.reject( { message: 'An unknown error occurred.' } ) );
        }

        return $q.reject(response.data);
    }

    $scope.memes = ['Harambe', 'Doge', 'Bruh', 'Pepe'];
    // $scope.populateStocks();
}]);