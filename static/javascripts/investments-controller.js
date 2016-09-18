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
            url: 'get_user_stocks/' + id
        });

        return request.then(handleSuccess, handleFailure);
    }

    function getAllStocks()
    {
        var request = $http({
           method: 'get',
            url: 'get_all_stocks'
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
        for ( var x = 0; x < $scope.myInvestments.length; x++)
        {
            $scope.myInvestments[x]['profitLoss'] = $scope.myInvestments[x].numShares * ($scope.myInvestments[x].currentValue - $scope.myInvestments[x].startValue);
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
    $scope.myInvestments = [{'name': 'harambe', 'numShares': 50, 'startValue': 100, 'currentValue': 140},
                        {'name': 'pepe', 'numShares': 1000, 'startValue': 213, 'currentValue': 195}];
    addProfitLoss();

    $scope.allStocks = [{'name': 'harambe', 'currentValue': 140},
        {'name': 'pepe', 'currentValue': 195},
        {'name': 'Tree Fiddy', 'currentValue': 133},
        {'name': 'Doge', 'currentValue': 100},
        {'name': 'John Cena', 'currentValue': 231},
        {'name': 'Miley Cyrus twerking', 'currentValue': 13}]
}]);