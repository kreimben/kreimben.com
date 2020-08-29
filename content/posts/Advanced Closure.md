---
title: Advanced Closure
date: 2020-03-08
---

> Closures are self-contained blocks of functionality that can be passed around and used in your code. - Swift.org

Swift's [closure](https://docs.swift.org/swift-book/LanguageGuide/Closures.html) is one of the most powerful featrue of swift language.

## Closure is **Magic**

you can make closure part of function or variable as a independent thing.

## Higher-Order Function

One of the most useful higher order function is Map, Filter, Reduce. 

If you've heard of JavaScript (and python), OK. JavaScript and Python *also* has those of higher order function.

<!-- more -->

***

<font size=6em>1. Map</font>

If you use *Map*, you can change internal value without any hassle coding haha

#### Using **For** (Without Map)

```
let someValue = [1, 2, 3, 4, 5]
var intArray = [Int]()

for value in someValue {
    intArray.append(value * 2)
}

print(intArray) // 2, 4, 6, 8, 10
```

#### Using Map

```
let someValue = [1, 2, 3, 4, 5]
var intArray = [Int]()

// += Result is same whatever you choice the way you map =+
//
// MARK: - First Way to Change Value
intArray = someValue.map({ (number: Int) -> Int in
    return number * 2
})

// MARK: - Second Way to Change Value
intArray = someValue.map { (number: Int) -> Int in // This is trailing closure which can be skipped parentheses
    return number * 2
}

// MARK: - Third Way to Change Value
intArray = someValue.map { return $0 * 2 }

// MARK: - Second Way to Change Value
intArray = someValue.map { $0 * 2 }
```
> If you need to pass a closure expression to a function as the function’s final argument and the closure expression is long, it can be useful to write it as a trailing closure instead. A trailing closure is written after the function call’s parentheses, even though it is still an argument to the function. When you use the trailing closure syntax, you don’t write the argument label for the closure as part of the function call ... Trailing closures are most useful when the closure is sufficiently long that it is not possible to write it inline on a single line. - Swift.org

***

<font size=6em>2. Filter</font>

Filter is **literally** filtering value.

#### Using **For** (Without Filter)

```
let num = [0, 1, 2, 3, 4, 5]
var even = [Int]()

for value in num {
    if value % 2 != 0 { continue }
    even.append(number)
}

print(evenNumbers) // [0, 2, 4]
```

#### Using Filter

```
let num = [0, 1, 2, 3, 4, 5]
var even = [Int]()

even = num.filter { $0 % 2 == 0}

print(evenNumbers) // [0, 2, 4]
```

***

<font size=6em>3. Reduce</font>

Reduce is like **sum** in math!

![ ](https://www.varsitytutors.com/assets/vt-hotmath-legacy/hotmath_help/topics/sigma-notation-of-a-series/sigma-notation.gif)

#### Using **For** (Without Reduce)

```
let num = [1, 2, 3, 4]
var sum = 0

for i in num {
    sum += i
}

print(sum) // 10
```

#### Using Reduce

```
let num = [1, 2, 3, 4]
var sum = 0

sum = num.reduce(0) { $0 + $1 } // Initial result is 0 and result is 10
```

According to Apple Developer website, `reduce(_:_:)`'s first argument is `initialResult` which is the value to use as the initial accumulating value and is passed to nextPartialResult the first time the closure is executed.

The whole function is below.

`func reduce<Result>(_ initialResult: Result, _ nextPartialResult: (Result, Element) throws -> Result) rethrows -> Result`

***

## Real Usage of Closure in Swift

You can use closure anywhere if it's related with function.

Closure can be function itself or arguments.

## @escaping and Completion Handler

Many of frameworks or APIs are using completion handler as a closure. Let's check out.

### `@nonescaping` and `@escaping`

If you don't declare closure as a `@escaping`, `@nonescaping` is **default**.

But if you are using closure as a `@escaping`, **that closure can be excuted outside of function.** Literally, `@escaping` closure become another function.

`@escaping` clusure have to reference somthing using `self` and `@nonescaping` don't need to reference somthing using `self`.

```
func someFunctionWithNonescapingClosure(closure: () -> Void) {
    closure() // non-escaping
}

class SomeClass {
    var x = 10
    func doSomething() {
        someFunctionWithEscapingClosure { self.x = 100 } // You must use "self"
        someFunctionWithNonescapingClosure { x = 200 }
    }
}

let instance = SomeClass()
instance.doSomething()
print(instance.x)
// Prints "200"

completionHandlers.first?()
print(instance.x)
// Prints "100"
```

