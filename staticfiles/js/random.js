$(function () {
    var sorceList = [
    '<img >',
    '任意の画像',
    '任意の画像'
    ];
    var random = Math.floor(Math.random() * sorceList .length);
    $('.js-random').append(sorceList [random]);
  });