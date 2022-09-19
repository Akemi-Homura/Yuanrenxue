let a = 6;
let b = 9;

// function simpleTag(strings, aValExpression, bValExpression, sumExpression) {
//     console.log(strings)
//     console.log(aValExpression)
//     console.log(bValExpression)
//     console.log(sumExpression)
//
//     return 'foobar'
// }

function simpleTag(strings, ...expressions) {
    console.log(strings)
    for (const expression of expressions) {
        console.log(expression)
    }
    return 'foobar'
}

let untaggedResult = `${a} + ${b} = ${a + b}`
let taggedResult = simpleTag`${a} + ${b} = ${a + b}`

console.log(untaggedResult)
console.log(taggedResult)
console.log("===================================")

function zipTag(strings, ...expressions) {
    return strings[0] + expressions.map((e, i) => `${e}${strings[i + 1]}`).join('')
}

taggedResult = zipTag`${a} + ${b} = ${a + b}`
console.log(taggedResult)