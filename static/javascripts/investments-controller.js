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

    function addProfitLoss()
    {
        for ( var x = 0; x < $scope.allStocks.length; x++)
        {
            $scope.allStocks[x]['profitLoss'] = $scope.allStocks[x].numShares * ($scope.allStocks[x].currentValue - $scope.allStocks[x].startValue);
        }
    }

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
    $scope.id = Cookies.get('user');
    // $scope.populateMyInvestments();
    // $scope.populateStocks();
    $scope.allStocks = [{'name': 'harambe', 'numShares': 50, 'startValue': 100, 'currentValue': 140},
                        {'name': 'pepe', 'numShares': 1000, 'startValue': 213, 'currentValue': 195}];
    addProfitLoss();
    console.log($scope.allStocks);
}]);