// CSSアニメーションを間隔を空けてループ再生させる処理
function looopAnimation(id, className, delay) {
  var element = document.getElementById(id);
  element.addEventListener("animationend", listener);
  
  function listener(event) {
    event.target.classList.remove(className);
    setTimeout(playAnimation, delay);
  }

  function playAnimation() {
    element.classList.add(className);
  }
}

function getImage(id){
  //画像ファイル名を配列で保持
  var arr = ['images/angry_earth.png', 'images/confidence_earth.png', 'images/cry_earth.png'];
 
  //ランダムで画像ファイルを取得して表示する
  var obj = document.getElementById(id);
  var a = Math.floor(Math.random() * arr.length);
  obj.src = arr[a];
}