module.exports = priorityQueue;

function priorityQueue() {
    this.queue = [];
    this.enqueue = function (value) {
        return this.queue.push(value);
    };
    this.dequeue = function () {
        var outp = null;
        if (this.queue.length > 1) {
            var max_value = this.queue[0];
            var max_i = 0;
            for (var i = 1; i < this.queue.length; ++i) {
                if (this.queue[i] > max_value) {
                    max_value = this.queue[i];
                    max_i = i;
                }
            }
            outp = this.queue.splice(max_i, 1)[0];
        } else if (this.queue.length == 1) {
            outp = this.queue.pop();
        }
        return outp;
    };
}
