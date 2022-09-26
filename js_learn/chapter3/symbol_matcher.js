class FooMatcher{
    static [Symbol.match](target){
        return target.includes('foo');
    }

}

console.log('foobar'.match(FooMatcher));
console.log('barbaz'.match(FooMatcher));

console.log("======================")

class StringMatcher{
    constructor(str) {
        this.str= str;
    }

    [Symbol.match](target){
        return target.includes(this.str);
    }
}

console.log('foobar'.match(new StringMatcher('foo')));
console.log('barbaz'.match(new StringMatcher('qux')))
