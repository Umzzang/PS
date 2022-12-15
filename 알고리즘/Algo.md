# 최대공약수 구하기

```
프로그래머스 분수의덧셈
```

```javascript
function fngcb(a, b) {
    return (a % b) ? fngcb(b, a%b):b
}
```

