// 用const 声明一个不会被修改的for 循环变量，
let i = 0;
for(const j =7;i<5;i++){
    console.log(j);
}

console.log('')

for (const key in {a:1, b:2}){
    console.log(key)
}

console.log('')

for (const value of [1,2,3,4,5]){
    console.log(value)
}