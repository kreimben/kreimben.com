---
title: What's new in Swift 5.2?
date: 2020-02-01
categories: ["Swift"]
tags: ["English"]
---

> This post is originally posted on [What’s new in Swift 5.2 – Hacking with Swift](https://www.hackingwithswift.com/articles/212/whats-new-in-swift-5-2)  and this post is **just copy**

The first beta of Swift 5.2 just landed with Xcode 11.4 beta, and it includes a handful of language changes alongside reductions in code size and memory usage, plus a new diagnostic architecture architecture that will help you diagnose errors faster.
In this article I’m going to walk through what’s changed with some practical examples so you can see for yourself how things have evolved. I encourage you to follow the links through to the Swift Evolution proposals for more information, and if you missed my earlier  [what’s new in Swift 5.1](https://www.hackingwithswift.com/articles/182/whats-new-in-swift-5-1)  article then check that out too.

<!-- more -->

- **Tip:** You can download this article as an Xcode playground:  [https://github.com/twostraws/whats-new-in-swift-5-2](https://github.com/twostraws/whats-new-in-swift-5-2) 

# **Key Path Expressions as Functions**
 [SE-0249](https://github.com/apple/swift-evolution/blob/master/proposals/0249-key-path-literal-function-expressions.md)  introduced a marvelous shortcut that allows us to use keypaths in a handful of specific circumstances.
The Evolution proposal describes this as being able to use “**\Root.value** wherever functions of **(Root) -> Value** are allowed”, but what it means is that if previously you sent a Car into a method and got back its license plate, you can now use **Car.licensePlate** instead.
This is best understood as an example, so here’s a **User** type that defines four properties:

```
struct User {
    let name: String
    let age: Int
    let bestFriend: String?

    var canVote: Bool {
        age >= 18
    }
}
```

We could create some instance of that struct and put them into an array, like this:

```
let Eric = User(name: “Eric Effiong”, age: 18, bestFriend: “Otis Milburn”)
let maeve = User(name: “Maeve Wiley”, age: 19, bestFriend: nil)
let otis = User(name: “Otis Milburn”, age: 17, bestFriend: “Eric Effiong”)
let users = [Eric, maeve, otis]
```

Now for the important part: if you want to get an array of all the users names, you can do so by using a key path like this:

```
let userNames = users.map(\.name)
print(userNames)
```

Previously you would have had to write a closure to retrieve the name by hand, like this:

```
let oldUserNames = users.map { $0.name }
```

This same approach works elsewhere – anywhere where previously you would have received a value and passed back one of its properties, you can now use a key path instead. For example, this will return all users who can vote:

```
let voters = users.filter(\.canVote)
```

And this will return the best friends for all users who have one:

```
let bestFriends = users.compactMap(\.bestFriend)
```

**Callable values of user-defined nominal types**
 [SE-0253](https://github.com/apple/swift-evolution/blob/master/proposals/0253-callable.md)  introduces statically callable values to Swift, which is a fancy way of saying that you can now call a value directly if its type implements a method named **callAsFunction()**. You don’t need to conform to any special protocol to make this behavior work; you just need to add that method to your type.
For example, we could create a **Dice** struct that has properties for **lowerBound** and **upperBound**, then add **callAsFunction** so that every time you call a dice value you get a random roll:

```
struct Dice {
    var lowerBound: Int
    var upperBound: Int

    func callAsFunction() -> Int {
        (lowerBound…upperBound).randomElement()!
    }
}

let d6 = Dice(lowerBound: 1, upperBound: 6)
let roll1 = d6()
print(roll1)
```

That will print a random number from 1 through 6, and it’s identical to just using **callAsFunction()** directly. For example, we could call it like this:

```
let d12 = Dice(lowerBound: 1, upperBound: 12)
let roll2 = d12.callAsFunction()
print(roll2)
```

Swift automatically adapts your call sites based on how **callAsFunction()** is defined. For example, you can add as many parameters as you want, you can control the return value, and you can even mark methods as **mutating** if needed.
For example, this creates a **StepCounter** struct that tracks how far someone has walked and reports back whether they reached their target of 10,000 steps:

```
struct StepCounter {
    var steps = 0

    mutating func callAsFunction(count: Int) -> Bool {
        steps += count
        print(steps)
        return steps > 10_000
    }
}

var steps = StepCounter()
let targetReached = steps(count: 10)
```

For more advanced usage, **callAsFunction()** supports both **throws** and **rethrows**, and you can even define multiple **callAsFunction()** methods on a single type – Swift will choose the correct one depending on the call site, just like regular overloading.


# Subscripts can now declare default arguments
When adding custom subscripts to a type, you can now use default arguments for any of the parameters. For example, if we had a **PoliceForce** struct with a custom subscript to read officers from the force, we could add a **default** parameter to send back if someone tries to read an index outside of the array’s bounds:

```
struct PoliceForce {
    var officers: [String]

    subscript(index: Int, default default: String = “Unknown”) -> String {
        if index >= 0 && index < officers.count {
            return officers[index]
        } else {
            return `default`
        }
    }
}

let force = PoliceForce(officers: [“Amy”, “Jake”, “Rosa”, “Terry”])
print(force[0])
print(force[5])
```

That will print “Amy” then “Unknown”, with the latter being caused because there is no officer at index 5. Note that you do need to write your parameter labels twice if you want them to be used, because subscripts don’t use parameter labels otherwise.
So, because I use **default default** in my subscript, I can use a custom value like this:

```
print(force[-1, default: “The Vulture”])
```


# New and improved diagnostics
Swift 5.2 introduced a new diagnostic architecture that aims to improves the quality and precision of error messages issued by Xcode when you make a coding error. This is particularly apparent when working with SwiftUI code, where Swift would often produce false positive error messages.
For an example, consider code like this:

```
struct ContentView: View {
    @State private var name = 0

    var body: some View {
        VStack {
            Text(“What is your name?”)
            TextField(“Name”, text: $name)
                .frame(maxWidth: 300)
        }
    }
}
```

That attempts to bind a **TextField** view to an integer **@State** property, which is invalid. In Swift 5.1 this caused an error for the **frame()** modifier saying **’Int’ is not convertible to ‘CGFloat?’**, but in Swift 5.2 and later this correctly identifies the error is the **$name** binding: **Cannot convert value of type ‘Binding’ to expected argument type ‘Binding’**.
You can find out more about the new diagnostic architecture on the  [Swift.org blog](https://swift.org/blog/new-diagnostic-arch-overview/) .
