---
title: Understanding Facades pettern
date: 2020-05-17 20:00:00
categories: ["Design Patterns"]
tags: ["English"]
---
## What is "Facades Pattern"?

![](https://www.tutorialspoint.com/design_pattern/images/facade_pattern_uml_diagram.jpg)



Facades pattern is used quite everywhere. Literally, It's common and also easy to use.

> Facades is the face of a building, especially the principal front that looks onto a street or open space.

You can use many of variables **just like facades of buildings**.

Let's check example right below!

## Codes

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

And then I'll make ```ShapeMaker``` which generate ```Shape```s.

```swift
class ShapeMaker {
  
    private circle: Shape
    private rectangle: Shape
    private square: Shape
  
    init() {
        self.circle = Circle()
        self.rectangle = Rectangle()
        self.square = Square()
    }
  
    func drawCircle() {
        self.circle.draw()
    }
  
    func drawRectangle() {
        self.rectangle.draw()
    }
  
    func drawSquare() {
        self.square.draw()
    }
}
```

OK haha Now, We can use ```ShapeMaker``` class to make various shapes.

```swift
class MainViewController: NSViewController {
  
    var shapeMaker: ShapeMaker?
  
    override func viewDidLoad() {
        super.viewDidLoad()
      
        self.shapeMaker = ShapeMaker()
    }
  
    @IBAction func executeTapped(_ sender: NSButton) {
      
        self.shapeMaker?.drawCircle()
        self.shapeMaker?.drawSquare()
        self.shapeMaker?.drawRectangle()
    }
}
```

If you tap button, you can see in XCode's command line

> Draw Circle.
>
> Draw Square.
>
> Draw Rectangle.

## Wrap up

Facades pattern can be used as manager that manages multiple classes or different features.

***

If you have any question or opinion, Please contact me through [my email](mailto:aksidion@kreimben.com).

Bye 'till next time :)