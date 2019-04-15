module.exports = DoublyLinkedList;


function Node(value) {
    this.data = value;
    this.next = null;
    this.prev = null;
}


function DoublyLinkedList() {
    this.size = 0
    this.head = null;
    this.tail = null;
    this.append = append;
    this.prepend = prepend;
    this.toString = toString;
    this.find = find;
    this.get = get;
    this.remove = remove;
    this.insert = insert;
}


function append(value) {
    var newNode = new Node(value);
    if (this.head == null) {
        this.head = newNode;
        this.tail = newNode;
    } else {
        newNode.prev = this.tail;
        this.tail.next = newNode;
        this.tail = newNode;
    }
    ++this.size;
    return newNode;
}


function prepend(value) {
    var newNode = new Node(value);
    if (this.head == null) {
        this.head = newNode;
        this.tail = newNode;
    } else {
        newNode.next = this.head;
        this.head.prev = newNode;
        this.head = newNode;
    }
    ++this.size;
    return newNode;
}


function toString() {
    var values = [];
    var currNode = this.head;
    while (currNode != null) {
        values.push(currNode.data.toString());
        currNode = currNode.next;
    }
    console.log('{ ' + values.join(', ') + ' }');
}


function find(value) {
    var currNode = this.head;
    while (currNode.data != value) {
        currNode = currNode.next;
        if (!currNode) {
            break;
        }
    }
    return currNode;
}


// gets a node by index. if given a negative index,
// function starts from tail following .prev link.
function get(index) {
    if (Math.abs(index) < this.size) {
        var n = 0;
        // positive index
        if (index >= 0) {
            currNode = this.head;
            while (n++ != index) {
                currNode = currNode.next;
            }
        }
        // negative index
        else {
            currNode = this.tail;
            while (--n != index) {
                currNode = currNode.prev;
            }
        }
        return currNode;
    }
    else {
        throw new Error('Index out of bounds.');
    }
}


function remove(index) {
    var node = this.get(index);
    // list has only 1 element
    if (this.size == 1) {
        this.head = null;
        this.tail = null;
    }
    // element is head
    else if (!node.prev) {
        this.head = node.next;
        node.next.prev = null;
    }
    // element is tail
    else if (!node.next) {
        this.tail = node.prev;
        node.prev.next = null;
    }
    else {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }
    --this.size;
    return node;
}


function insert(index, value) {
    var newNode;
    if (index == 0) {
        newNode = this.prepend(value);
    }
    else {
        newNode = new Node(value);
        var node = this.get(index);
        newNode.next = node;
        newNode.prev = node.prev;
        node.prev.next = newNode;
        node.prev = newNode;
        ++this.size;
    }
    return newNode;
}
