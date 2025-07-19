var isPalindrome = function (x) {
  var X = x.toString().split("");
  if (X.length <= 1) {
    return true;
  }
  let h = 0;
  let t = X.length - 1;
  for (let i = 0; i < X.length / 2; i++) {
    if (X[h] != X[t]) {
      console.log(`${X[h]} != ${X[t]}`);
      return false;
    } else {
      h++;
      t--;
      console.log(h, t);
    }
  }
  return true;
};
console.log(isPalindrome(101010001));
