// for 循环中的let 声明
for (var i = 0; i < 5; ++i) {
    setTimeout(() => console.log(i), 0);
}

for (let i = 0; i < 5; ++i) {
    setTimeout(() => console.log(i), 0);
}

