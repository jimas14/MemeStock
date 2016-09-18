var app = angular.module('memeStock');

app.config(function ($stateProvider, $interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');

});

app.controller('TransactionsController', ['$scope', '$http', '$q', '$state', function ($scope, $http, $q, $state) {

    $scope.alerts = [];

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

    $scope.buy = function()
    {
        if ($scope.memes.indexOf($scope.meme) == -1)
        {
            $scope.alerts.push({type: 'danger', msg: 'Invalid meme!'});
        }
        if ($scope.quantity <= 0)
        {
            $scope.alerts.push({type: 'danger', msg: 'Invalid quantity!'});
        }
        if ($('.datepicker').val() == '')
        {
            $scope.alerts.push({type: 'danger', msg: 'Invalid date!'});
        }

        var request = $http({
            method: 'post',
            url: 'buy_sell',
            data: {
                method: 'buy',
                user: Cookies.get('user'),
                meme: $scope.meme,
                time: $('.datepicker').val(),
                shares: parseInt($scope.quantity)
            }
        });

        request.then(function(res) {
            $scope.alerts.push({type: 'success', msg: 'Successfully bought!'});
        }, function(err) {
            $scope.alerts.push({type: 'danger', msg: 'Failed!'});
        });
    };

    $scope.sell = function ()
    {
        if ($scope.memes.indexOf($scope.meme) == -1)
        {
            $scope.alerts.push({type: 'danger', msg: 'Invalid meme!'});
        }
        if ($scope.quantity <= 0)
        {
            $scope.alerts.push({type: 'danger', msg: 'Invalid quantity!'});
        }
        if ($('.datepicker').val() == '')
        {
            $scope.alerts.push({type: 'danger', msg: 'Invalid date!'});
        }

        var request = $http({
            method: 'post',
            url: 'buy_sell',
            data: {
                method: 'sell',
                user: Cookies.get('user'),
                meme: $scope.meme,
                time: $('.datepicker').val(),
                shares: parseInt($scope.quantity)
            }
        });

        request.then(function(res) {
            $scope.alerts.push({type: 'success', msg: 'Successfully sold!'});
        }, function(err) {
            $scope.alerts.push({type: 'danger', msg: 'Failed!'});
        });
    };

    $scope.closeAlert = function(index) {
        $scope.alerts.splice(index, 1);
    };

    $scope.id = Cookies.get('user');
    $scope.memes = ['Harambe', 'Doge', 'Tree Fiddy', 'Pepe', 'John Cena', 'Miley Cyrus twerking'];
    // $scope.populateStocks();


    // $('.datepicker').pickadate({
    //     selectMonths: true, // Creates a dropdown to control month
    //     selectYears: 15 // Creates a dropdown of 15 years to control year
    // });
}]);