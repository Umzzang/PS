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



# JavaScript Reduce

```
배열의 각 요소에 대해 주어진 리듀서 (reducer) 함수를 실행하고, 하나의 결과값을 반환합니다.
```

**callback 함수**

배열의 각 element들에 대해서 실행되는 callback 함수이고, 

이 함수의 리턴값은 다음 element에 대한 callback 함수 실행시 파라미터(accumulator)로 전달됩니다.

- **accumulator** : 이전 element에 대한 callback 함수의 리턴값
- **currentValue** : 현재 처리중인 배열 element
- **currentIndex** : 현재 처리중인 배열 index
- **array** : 배열 전체

**initialValue**

callback 함수를 처음 실행할 때, accumulator의 값.



## sum 구하기

```javascript
const arr = [1, 2, 3];

const result = arr.reduce(function add(sum, currValue) {
  return sum + currValue;
}, 0);
```



**reduceRight은 reduce와 같지만 오른쪽부터 연산 시작**





# JavaScript repeat

```
repeat() 메서드는 문자열을 주어진 횟수만큼 반복해 붙인 새로운 문자열을 반환합니다.
```



```javascript
function solution(n) {
    for(let i = 1; i < n + 1; i++) {
        console.log('*'.repeat(i));
    }
}
```



# JavaScript ASCII

* charCodeAt()

```javascript
console.log('A'.charCodeAt())      // 65
```



* fromCharCode()

```javascript
console.log(String.fromCharCode(65, 66));   //'AB'
```

