module.exports = heap;


function heap (arr) {
    this.heapSize = 0;
    this.data = [null];
    if (arr) {
        this.heapSize = arr.length;
        this.data = this.data.concat(arr);
    }
    this.left = left;
    this.right = right;
    this.maxHeapify = maxHeapify;
    this.buildMaxHeap = buildMaxHeap;
    this.buildMaxHeap();
}

function left (i) {
        return i << 1;
}

function right (i) {
        return (i << 1) + 1;
}

function maxHeapify(i) {
    var l = this.left(i);
    var r = this.right(i);
    var largest;
    if (l <= this.heapSize && this.data[i] < this.data[l]) {
        largest = l;
    } else {
        largest = i;
    }
    if (r <= this.heapSize && this.data[largest] < this.data[r]) {
        largest = r;
    }
    if (largest != i) {
        var temp = this.data[i];
        this.data[i] = this.data[largest];
        this.data[largest] = temp;
        this.maxHeapify(largest);
    }
}

function buildMaxHeap() {
    for (var i = Math.floor(this.heapSize / 2); i > 0; --i) {
        this.maxHeapify(i);
    }
}
