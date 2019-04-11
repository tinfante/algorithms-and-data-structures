module.exports = {
    factorial_stack: factorial_stack,
    factorial_recur: factorial_recur
}


/*
 * See McMillan, "Data Structures and Algorithms with Javascript",
 * Chapter 4: Stacks, pp. 55-56. At the heart of this solution is the relation
 * between recursion and the stack, which is very well explained here:
 *  https://www.htmlgoodies.com/primers/jsp/article.php/3622321
 */
function factorial_stack(n) {
    var stack = [];
    for (var i = 2; i <= n; ++i) {
        stack.push(i);
    }
    var f = 1;
    while (stack.length > 0) {
        f *= stack.pop();
    }
    return f;
}


// Traditional recursive solution using a ternary expression.
function factorial_recur(n) {
    return n == 0 ? 1 : n * factorial_recur(--n);
}
