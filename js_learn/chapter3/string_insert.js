let value = 5;
let exponent = 'second';
let ret = `${value} to the ${exponent} power is ${value * value}`;
console.log(ret);
console.log("================================");
// 将表达式转换为字符串时会调用toString()
let foo = {toString: () => "World"};
console.log(`Hello, ${foo}`);
console.log("================================");

// 在插值表达式中可以调用函数和方法
function capitalize(word) {
    return `${word[0].toUpperCase()}${word.slice(1)}`;
}

console.log(`${capitalize('hello')}, ${capitalize('world')}`);
console.log("================================");

// 此外，模板也可以插入自己之前的值
value = '';

function append() {
    value = `${value}abc`
    console.log(value)
}

append();
append();
append();