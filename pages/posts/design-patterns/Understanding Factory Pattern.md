---
title: Understanding factory pettern
date: 2020-05-17 20:40:00
categories: ["Design Patterns"]
tags: ["English"]
---
## What is "Factory Pattern"?

Factory pattern is one of the most used design pattern in the software development and is quite similar with "Facades pattern"

In Factory pattern, we create object **without exposing the creation logic** to the client and refer to newly created object using a common interface and that's the most differences between "facades pattern".

![](https://www.tutorialspoint.com/design_pattern/images/factory_pattern_uml_diagram.jpg)



```swift
protocol Shape {

  func draw()
}
```

And then create concrete classes implementing the same interface.

```swift
class Rectangle: Shape {

  func draw() {   

    print("Draw Rectangle.")
  }
}
```

```swift
class Square: Shape {

  func draw() {   

    print("Draw Square.")
  }
}
```

```swift
class Circle: Shape {

  func draw() {

    print("Draw Circle.")
  }
}
```

Above codes are same with "facades pattern" but below is different.

First I'll define some of types

```swift
enum ShapeType {
  case circle
  case rectangle
  case square
}
```

And then, Here is **"Factory"**.

```swift
class ShapeFactory {
  
  func getShape(_ type: ShapeType) -> Shape {
    
    switch type {
      case .circle: return Circle()
      case .rectangle: return Rectangle()
      case .square: return Square()
    }
  }
}
```

OK, Let's use factory classes

```swift
class MainViewController: NSViewController {
  
  var shapeGen: ShapeFactory?
  
  override func viewDidLoad() {
    super.viewDidLoad()
    
    self.shapeGen = ShapeFactory()
  }
  
  @IBAction func circleTapped(_ sender: NSButton) {
    
    let shape = self.shapeGen?.getShape(.circle)
    shape.draw()
  }
  
  @IBAction func rectangleTapped(_ sender: NSButton) {
    
    let shape = self.shapeGen?.getShape(.rectangle)
    shape.draw()
  }
  
  @IBAction func squareTapped(_ sender: NSButton) {
    
    let shape = self.shapeGen?.getShape(.square)
    shape.draw()
  }
}
```

So you can get results like below in XCode's command line when you click button.

> Draw Circle.
>
> Draw Rectangle.
>
> Draw Square.

## Wrap up

As a one of the most used design pattern, Factory pattern has strength where you've to **decouple between classes**.

For example, If you have to change class's codes and used factory pattern, You only have to change **class's codes**.

Or if you don't use factory pattern, On the other hand **you have to change so many of codes that uses changed class**.

That's for just it.

***

If you have any question or opinion, Please contact me through [my email](mailto:aksidion@kreimben.com).

Bye :)