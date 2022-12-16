# 최대공약수 구하기

```
프로그래머스 분수의덧셈
```

```javascript
function fngcb(a, b) {
    return (a % b) ? fngcb(b, a%b):b
}
```



# JavaScript sort

```javascript
function compare(a, b) {
    return a- b
}

function solution(array) {
    var answer = 0;
    
    return array.sort(compare)[parseInt(array.length/2)];
}
```

 **sort() 안에 함수 안넣으면 문자열로 취급해서 오름차순함**

compare함수의 리턴값에 따라서 변경할지 결정





