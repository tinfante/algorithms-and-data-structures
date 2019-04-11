module.exports = Stack;


function Stack() {
    this.data = [];
    this.size = 0;
    this.push = push;
    this.pop = pop;
    this.peek = peek;
    this.length = length;
}


/**
 * Could use data.push(), but what would be the point? Also a good
 * excuse to demonstrate the difference in the placement of ++ (before:
 * increments variable and then returns updated value; after: increments
 * variable, but returns its old value).
 */
function push(item) {
    this.data[this.size++] = item;
}


/**
 * Again: could use data.pop(), notice the placement of -- decrement.
 */
function pop() {
    if (this.size > 0) {
        var poppedItem = this.data[--this.size];
        this.data = this.data.slice(0, this.size);
        return poppedItem;
    }
}


function peek() {
    return this.data[this.size - 1];
}


function length() {
    return this.size;
}
