class FooSearcher {
    static [Symbol.search](target) {
        return target.indexOf('foo')
    }
}

console.log('foobar'.search(FooSearcher))
console.log('barfoo'.search(FooSearcher))
console.log('barbaz'.search(FooSearcher))

console.log("===========================")

class StringSearcher{
    constructor(str) {
        this.str= str;
    }

    [Symbol.search](target){
        return target.indexOf(this.str);
    }
}

console.log('foobar'.search(new StringSearcher('foo')));
console.log('barfoo'.search(new StringSearcher('foo')));
console.log('barbaz'.search(new StringSearcher('qux')));