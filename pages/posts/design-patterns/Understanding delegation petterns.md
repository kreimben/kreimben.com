---
title: Understanding delegation petterns
date: 2020-03-02
categories: ["Design Patterns"]
tags: ["English"]
---
## What is "Delegation Pattern"?

Delegation patterns in swift is implemented using [**Protocol**](https://docs.swift.org/swift-book/LanguageGuide/Protocols.html). (I won't tell about what is protocol and what does it do.)

Delegation patterns **literally** delegate something you want to implement.

Without further ado, Let's check it out.

<!-- more -->

## Examples

For explaning some of example, I will describe something about human beings.
**Every** human beings have to breathe, eat some of foods and take a rest.

So, I will implement **HumanDelegate** which regulates what human should do.

```
protocol HumanDelegate: AnyObject {

    func breathe()

    func eat()

    func takeARest()
}
```
    
> **AnyObject** in declare of protocol means that **class only inherits this protocol**. If you want struct or enum to be inherited this protocol, remove **AnyObject**

OK. and let's make class object.

```
class Human {

    weak var delegate: HumanDelegate?
    
    var name: String
    
    init(_ name: String = "John") {
    
        self.name = name
    }
    
    func inhale() {
    
        self.delegate?.breathe()
    }
    
    func eatSomeFoods() {
    
        self.delegate?.eat()
    }
    
    func takeANap() {
    
        self.delegate?.takeARest()
    }
    
    func speakOwnName() {
    
        print("My name is \(name).")
    }
    
    func greeting() {
    
        print("Hello! Nice to meet you!")
    }
}
```

Yep! I make actual object that we will use.

```
class someViewController: UIViewController {

    func viewDidLoad() {
        super.viewDidLoad()

        let humanBeing = Human("Kreimben")
        
        humanBeign.delegate = self
    }
}

extension someViewController: HumanDelegate {

    func breathe() {

        print("Hoo, Ha!")
    }

    func eat() {

        print("I'm eating some of sandwiches.")
    }

    func takeARest() {

        print("I'm going to bed now")
    }
}
```
    
> To connect implemented actual codes and delegate protocol, We have to pass **whole class** to delegate property. and THAT'S WHAT EXACTLY I DID like **humanBeign.delegate = self**


## But why do i have to use "Delegation Pattern"?

According to above example, we implemented Human class and HumanDelegate protocol that regulates what human should do. (Eating, breathing, resting)

Let's think about **real situation**. Just like "All of people in the world should be inherited **HumanDelegate**" and you can choice how do you do it.

We can eat some foods while doing homeworks, playing games, reading this article, cheating with someone, or just sitting at the table feeling food's taste......

Whatever humans *do*, there is no problem **if human beings are eating something**. (Way human beings breathe and take a rest are also same.)

So you have to consider **Number of Cases**. if you want to implement *just* **eating, breathing, resting**, All you have to do is making delegate protocol because you can't deal with each of cases.

## Wrap up

OK! that's all about Delegation patterns.

1. We made some of common behaviour (in this example, that is **func**)
2. We imeplemented main object that is **Human**
3. In **someViewController**, we adopted **HumanDelegate** protocol and implemented approciated behaviour (some of functions).  

If you have any questions about this articles, Don't hesitate to contact me :)
