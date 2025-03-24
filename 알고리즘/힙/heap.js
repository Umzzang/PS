class MinHeap {
  constructor() {
    this.heap = [null];
  }

  getMin() {
    return this.heap[1];
  }

  getSize() {
    return this.heap.length - 1;
  }

  isEmpty() {
    return this.heap.length < 2;
  }

  insert(node) {
    let current = this.heap.length;

    while (current > 1) {
      const parent = Math.floor(current / 2);
      if (this.heap[parent] > node) {
        this.heap[current] = this.heap[parent];
        current = parent;
      } else {
        break;
      }
    }
    this.heap[current] = node;
  }

  pop() {
    let min = this.heap[1];
    if (this.heap.length > 2) {
      this.heap[1] = this.heap.pop();

      let current = 1;
      let left = current * 2;
      let right = left + 1;

      while (this.heap[left]) {
        let compareIndex = left;
        if (this.heap[right] && this.heap[right] < this.heap[left]) {
          compareIndex = right;
        }

        if (this.heap[compareIndex] < this.heap[current]) {
          [this.heap[compareIndex], this.heap[current]] = [
            this.heap[current],
            this.heap[compareIndex],
          ];
          current = compareIndex;
        } else break;
        left = current * 2;
        right = left + 1;
      }
    } else if (this.heap.length == 2) {
      this.heap.pop();
    } else return null;
    return min;
  }
}

const heap = new MinHeap();
heap.insert(5);
heap.insert(4);
heap.insert(1);
console.log(heap);
console.log(heap.pop());
