var portfolioApp = angular.module('portfolioApp',[]); 
portfolioApp.controller('GalleryListCtrl', function($scope) {
    $scope.title = "Moje podroze od marca 2020 roku";

    $scope.galleries = [
        
    { 'title':'Biedronka na rawskiej',
     'when':'2020-12-14',
     'thumbnailUrl':'gallery/biedra.png'
    },

    { 'title':'Sklep szafirek, po drodze do domu',
     'when':'2020-08-04',
     'thumbnailUrl':'gallery/szafirek.png'
    },

    { 'title':'Pole, na spacery',
    'when':'2020-07-19',
    'thumbnailUrl':'gallery/pole.png'
   },

  { 'title':'stacja benzynowa radziej ale czasem w niedziele',
  'when':'2021-05-11',
  'thumbnailUrl':'gallery/stacja.png'
 },
 
 { 'title':'PWSZ na wojska, tutaj to coraz rzadziej',
 'when':'2021-11-03',
 'thumbnailUrl':'gallery/pwsz.png'
},

{ 'title':'las obok pola',
    'when':'2021-01-25',
   'thumbnailUrl':'gallery/las.png'
  },
   
    ];
    });