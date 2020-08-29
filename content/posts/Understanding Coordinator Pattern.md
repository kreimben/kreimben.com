---
title: Understanding coordinator pettern
date: 2020-05-17
---
# What is "Coordinator Pattern"?

Coordinator pattern is devised from [Soroush Khanlou](https://khanlou.com).

From [hacking with swift](https://hackingwithswift.com) which is my favorite site, Coordinator pattern can be defined as

> Using the coordinator pattern in iOS apps lets us remove the job of app navigation from our view controllers, helping make them more manageable and more reusable, while also letting us adjust our app's flow whenever we need.

So, if we use Coordinator pattern, There is no need to struggle with stupid navigation controllers and view's data.

How happy it is! We don't need to coupling between class and don't need to care of previous and next view.

Thus, app flow is controlled using a coordinator, and views **communicate only with a coordinator**. If you want to have users authenticate themselves, ask the coordinator to show an authentication dialog – it can take care of figuring out what that means and presenting it appropriately.

Before show you example, there are three steps I want to cover in order to give you a good foundation with coordinators:

1. Designing **two** protocols: one that will be used by all our coordinators, and one to make our view controllers easier to create.
2. Creating a main coordinator **that will control our app flow, then starting it when our app launches.**
3. Presenting other view controllers.

OK, Let's see example!

# Example

## boilerplates

```swift
import UIKit

protocol Coordinator {
    var childCoordinators: [Coordinator] { get set }
    var navigationController: UINavigationController { get set }
  
    func start()
}
```

It's not hard to understand!

First variable's behavior is have **literally child coordinators** and second variable is property that save **UINavigationController**.

And then, when ```Coordinator``` protocol confirmed, execute ```start()``` :)

Next, We have to ready for Storyboard in case that we use ```Storyboard```.

```swift 
import UIKit

protocol Storyboarded {
    static func instantiate() -> Self
}

extension Storyboarded where Self: UIViewController {
    static func instantiate() -> Self {
        // this pulls out "MyApp.MyViewController"
        let fullName = NSStringFromClass(self)

        // this splits by the dot and uses everything after, giving "MyViewController"
        let className = fullName.components(separatedBy: ".")[1]

        // load our storyboard
        let storyboard = UIStoryboard(name: "Main", bundle: Bundle.main)

        // instantiate a view controller with that identifier, and force cast as the type that was requested
        return storyboard.instantiateViewController(withIdentifier: className) as! Self
    }
}
```

```instantiate()``` returns class itself and then below ```extension``` is [**default implementation**](https://docs.swift.org/swift-book/LanguageGuide/Protocols.html#ID277).

OK so, what about our ```ViewController```?

```swift
class SomeViewController: UIViewController, Storyboarded {
```

What a beautiful code? :)

Now that we have a way to create view controllers easily, we no longer want the storyboard to handle that for us. In iOS, storyboards are responsible not only for containing view controller designs, but also for configuring the basic app window.

We’re going to allow the storyboard to store our designs, but stop it from handling our app launch. So, please open Main.storyboard and select the view controller it contains:

1. Use the attributes inspector to **uncheck its Initial View Controller box.**
2. Now change to the identity inspector and give it the storyboard identifier “ViewController” – remember, this needs to match the class name in order for the `Storyboarded` protocol to work.

The final set up step is to stop the storyboard from configuring the basic app window:

1. Choose your project at the top of the project navigator.
2. Select “CoordinatorTest” underneath Targets.
3. Look for the Main Interface combo box – it should say “Main”.
4. Delete “Main”, leaving Main Interface blank.

That’s all our basic code complete. Your app won’t actually work now, but we’re going to fix that next…

## MainCoordinator

The next step is to create our first coordinator, which will be responsible for taking control over the app as soon as it launches.

```swift
import UIKit

class MainCoordinator: Coordinator {
    var childCoordinators = [Coordinator]()
    var navigationController: UINavigationController

    init(navigationController: UINavigationController) {
        self.navigationController = navigationController
    }

    func start() {
        let vc = viewController.instantiate()
        vc.coordinator = self
        self.navigationController.pushViewController(vc, animated: false)
    }
}
```

We can store sub-coordinator to ```childCoordinators```but won't use this example.

## AppDelegate or SceneDelegate

Now that we have a coordinator for our app, we need to use that when our app starts. Normally app launch would be handled by our storyboard, but now that we’ve disabled that we must write some code inside AppDelegate.swift to do that work by hand.

In the ```AppDelegate.swift``` or ```SceneDelegate.swift```, Please add ```var coordinator: Coordinator?``` variable. and then in ```didFinishLaunchingWithOptions```

```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {
  
    // create the main navigation controller to be used for our app
    let navController = UINavigationController()

    // send that into our coordinator so that it can display view controllers
    self.coordinator = MainCoordinator(navigationController: navController)

    // tell the coordinator to take over control
    self.coordinator?.start()

    // create a basic UIWindow and activate it
    window = UIWindow(frame: UIScreen.main.bounds)
    window?.rootViewController = navController
    window?.makeKeyAndVisible()

    return true
}
```

If everything has gone to plan, you should be able to launch the app now and see something.

## App Flow

Coordinators exist to control program flow around your app, and we’re now in the position to show exactly how that’s done.

First, We have to make ```ViewController```s in storyboard and ```ViewController``` classes.

Second, Please add ```weak var coordinator: MainCoordinator?``` in each ```ViewController``` classes.

Third, Please confirm ```Stroyboarded``` protocol to make sure identifiy your VC class names.

OK only final step is below!

```swift
/// in MainCoordinator.swift

func behaviorOne() {
  
    var vc = firstView.instantiate()
    vc.coordinator = self
    navigationcontroller.pushViewController(vc, animated: false)
}

func behaviorTwo() {
  
    var vc = secondView.instantiate()
    vc.coordinator = self
    navigationcontroller.pushViewCtonroller(vc, animated: false)
}
```

And....! in ```SomeViewController```, You can use only single function of ```MainCoordinator```'s.

For example,

```swift
/// in MainCoordinator

@IBAction func firstViewTapped(_ sender: UIButton) {
  
    self.coordinator?.behaviorOne()
}

@IBAction func secondViewTapped(_ sender: UIButton) {
  
  self.coordinator?.behaviorTwo()
}
```



## Wrap up

We can use Coordinator pattern to make viewcontroller easy to use and get independent from messive VC :)

Anyway, if you have any question or opinion, Please contact me to [my email](mailto:aksidion@kreimben.com).

Bye 'till next time :)

***

This article is referred to [this article](https://www.hackingwithswift.com/articles/71/how-to-use-the-coordinator-pattern-in-ios-apps) and Thanks to hacking with swift :)

