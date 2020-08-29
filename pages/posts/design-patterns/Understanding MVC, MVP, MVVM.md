---

title: Understanding MVC, MVP, MVVM

date: 2020-05-08

categories: ["Design Patterns"]

tags: ["English"]

---

Hello guys, I'm Kreimben! 🤚🏻

Today, i'm gonna talking about MV**X** family especially MVC.

# History of MV**X** Family

Since MVC is invented in 1979 by [T. Reenskaug](https://en.wikipedia.org/wiki/Trygve_Reenskaug) for GUI in PARC, It has been spreaded all around world!

And in 1988, [One young businessman](https://en.wikipedia.org/wiki/Steve_Jobs) catched it in his mind and helped to make [**GREAT** GUI Computer](https://en.wikipedia.org/wiki/NeXTSTEP).

Anyway, MVC... It's simple!

## MVC

### M - Model

>  Models represent knowledge. A model could be a single object (rather uninteresting), or it could be some structure of objects.

OK. Model can be mini framework or some of class in order to manage somethings.

### V - View

> A view is a (visual) representation of its model. It would ordinarily highlight certain attributes of the model and suppress others. It is thus acting as a presentation filter.

View is just **view** which actually displays many of things. You don't need to think about that so much because **view** is everywhere especially if you're iOS or macOS developer.

Let's think about many of **storyboards or XIBs**. That's just it :)

### C - Controller

> A controller is the link between a user and the system.

Yup, That also should be **NSViewController** or **NSWindowController** and many of things...

## MVC K&P

in 1988, Glenn E. Krasner and Stephen T. Pope published a variation of MVC.

![](https://mvc.givan.se/mvc-kp-e6a39f0b536edb298602d86542e1eb76.png)

### M - Model

> The model of an application is the domain-specific software simulation or implementation of the application's central structure.

### V - View

> Views deal with everything graphical: they request data form their model, and display the data.

### C - Controller

> Controllers contain the interface between their associated models and views and the input devices (e.g., keyboard, pointing device, time)

Just like original MVC, it's almost same and even more detaild.



## NeXTSTEP (1988)

As I talked above, Steve Jobs's NeXT confirm to take OOP and [Objective-C](https://en.wikipedia.org/wiki/Objective-C) and They built NeXT computer.

NeXTSTEP was later modified to separate the underlying operating system from the higher-level object libraries. The result was the OpenStep API, a predecessor of Mac OS X and the Cocoa API.

## MVP (1996)

MVP is derived from MVC, So basic behavior is almost same except that Controller is changed to Presenter.

### M - Model

> Deals with data management. How do i change my data? How do I specify my data? What is my data? 

### V - View

> Deals with user interface. How do i display my data? How do events map into changes in my data? It hands off events to the presenter, similar to what Application Model does. But, it observes the model, so the View updates itself.

### P - Presenter

> The View-Controller of basix MVC is refered as Presentation. This represents the function of the classic Smalltalk controller, but elevated to an application level and taking in to account the intermediate selection, command, and interator concepts. Its role is to interpret the events and gestures initialted by the user and provied business logic. The classic Controller faded in to the View. The Presenter receives the input from users via View, then process the user’s data with the help of Model and passing the results back to the View. Presenter communicates with view through interface. Interface is defined in presenter class, to which it pass the required data. Activity/fragment or any other view component implement this interface and renders the data in a way they want.

In the MVP design pattern, the presenter **manipulates** the model and also **updates** the view. In MVP View and Presenter are completely decoupled from each other’s and communicate to each other’s by an interface. Because if decoupling mocking of the view is easier and unit testing of applications that leverage the MVP design pattern over the MVC design pattern are much easier.

## MVVM (2005)

MVVM Key features:

* Relies on data binding, a mechanism that gives you boilerpate synchronization code.
* The ViewModel is easier to unit test compared to code-behind or event-driven code.

> The ViewModel, though it sounds View-ish is really more Model-is, and that means you can test it without awkward UI automation and interaction.

MVVM Issues:

* Declarative data binding can be harder to debug.
* In very large apps, data binding can result in considerable memory consumption.
* It can be overkill for simple UIs.

In MVVM, View and Model is not coupled **at all**. So they don't know each other. 🤷🏻‍♂️



### M - Model

> It is the data or business logic, completely UI independent, that sotres the state and does the processing of the problem domain.

### V - View

> Consists of the visual elements, the buttons, windows, graphics and more complex controls of a GUI. In simple examples, the View is data bound directly to the model.

### VM - View Model

> The term means "Model of a View", and be thought of as abstraction of the view, but it also provides a specialization of the Model that the View can use for data-binding. It contains data-tranformers that convert Model types into View types, and it contains Commands the View can use to interact with the Model.

# Why should I use App-Architecture?

Before I talk about it, I would like to say about **What is good architecture**.

1. Balanced **distribution** of responsibilities among entities with strict roles.
2. **Testability** usually comes from the first feature (and don’t worry: it is easy with appropriate architecture).
3. **Ease of use** and a low maintenance cost.

If you're not intermediated developer, You can't understand reason of using app-architecture right now though, It's **pretty important** because it's literally **architecture**.

App is based on it's architecture and if you write the code and make giant app without elaborate architecture and design patterns, You'll be fail to maintain your codes.

So learning and using app-architecture and design patterns is **really important**.

# Wrap up

Some basic differences can be written in short:

**MVC:**

Traditional MVC is where there is a 

1. Model: Acts as the model for data
2. View : Deals with the view to the user which can be the UI
3. Controller: Controls the interaction between Model and View, where view calls the controller to update model. View can call multiple controllers if needed. 

**MVP:**

Similar to traditional MVC but Controller is replaced by Presenter. But the Presenter, unlike Controller is responsible for changing the view as well. The view usually does not call the presenter.

**MVVM**

The difference here is the presence of View Model. It is kind of an implementation of Observer Design Pattern, where changes in the model are represented in the view as well, by the VM. Eg: If a slider is changed, not only the model is updated but the data which may be a text, that is displayed in the view is updated as well. So there is a two-way data binding.

![](https://i.stack.imgur.com/CFbNC.png)

***

This article referred to [this map](https://mvc.givan.se/), [this article](https://medium.com/@ankit.sinhal/mvc-mvp-and-mvvm-design-pattern-6e169567bbad), [this](https://medium.com/ios-os-x-development/ios-architecture-patterns-ecba4c38de52#.wtcp3gqzw) and many of Q&As. Thanks for that 🙏🏻