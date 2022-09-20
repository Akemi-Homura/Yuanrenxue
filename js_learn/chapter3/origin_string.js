// Unicode 示例
console.log(`\u00A9`)
console.log(String.raw`\u00A9`)
console.log("=========================")
// 换行符示例
console.log(`first line\nsecond line`)
console.log(String.raw`first line\nsecond line`)
console.log("=========================")

// 对实际对换行符是不行的
console.log(`first line
second line`)
console.log(String.raw`first line
second line`)
console.log("=========================")

// 标签函数的第一个参数的.raw属性可以获得每个字符串的原始内容
function printRaw(strings) {
    console.log('Actual characters:')
    for(const string of strings){
        console.log(string)
    }

    console.log('Escaped characters')
    for(const rawString of strings.raw){
        console.log(rawString)
    }
}

printRaw`\u00A9${'and'}\n`