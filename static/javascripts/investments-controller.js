var app = angular.module('memeStock');

app.config(function ($stateProvider, $interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});

app.controller('InvestmentsController', ['$scope', '$http', '$q', '$state', function ($scope, $http, $q, $state) {
    // Get investments
    function getMyInvestments(id)
    {
        var request = $http({
            method: 'get',
            url: 'user/' + id
        });

        return request.then(handleSuccess, handleFailure);
    }

    function getAllStocks()
    {
        var request = $http({
           method: 'get',
            url: 'stocks'
        });

        return request.then(handleSuccess, handleFailure);
    }

    $scope.populateMyInvestments = function()
    {
        getMyInvestments(id).then(function(result) {
            if (null != result)
            {
                $scope.myInvestments = result.myInvestments;
            }
        }, function(err) {
            console.log('bruh something went wrong');
        });
    };

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

    $scope.n = ['a', 'c', 'b'];
    // $scope.populateMyInvestments();
    // $scope.populateStocks();
}]);