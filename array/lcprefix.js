var longestCommonPrefix = function (strs) {
  for (let i = 0; i <= strs.length - 1; i++) {
    var str = strs[i].split("");
    console.log(str);
  }
};

console.log(longestCommonPrefix(["flower", "flow", "flight"]));
