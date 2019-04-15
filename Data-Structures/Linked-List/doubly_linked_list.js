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


function get(value) {
    var currNode = this.head;
    while (currNode.data != value) {
        currNode = currNode.next;
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

// TODO: No funciona si queda un item en la lista.
function remove(index) {
    var node = this.get(index);
    if (node.prev) {
        node.prev.next = node.next;
    }
    else {
        node.next.prev = null;
        this.head = node.next;
    }
    if (node.next) {
        node.next.prev = node.prev;
    }
    else {
        node.prev.next = null;
        this.tail = node.prev;
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
