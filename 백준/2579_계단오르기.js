let input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
let n = Number(input[0]);
let answerStr = "";
let stairs = [];
// console.log(input);
for (let i = 1; i <= n; i++) {
  let num = +input[i].split(" ");
  stairs.push(num);
}

const dp = Array.from(Array(n), () => Array(2).fill(0));
// console.log(dp);
dp[0][0] = 0;
dp[0][1] = stairs[0];

if (n > 1) {
  dp[1][0] = stairs[0] + stairs[1];
  dp[1][1] = stairs[1];

  for (let i = 2; i < n; i++) {
    dp[i][0] = dp[i - 1][1] + stairs[i];
    dp[i][1] = Math.max(dp[i - 2][0], dp[i - 2][1]) + stairs[i];
  }
}
console.log(Math.max(dp[n - 1][0], dp[n - 1][1]));
