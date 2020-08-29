---
title: Understanding strategy pettern
date: 2020-05-17 17:00:00
categories: ["Design Patterns"]
tags: ["English"]
---
## What is "Strategy Pattern"?

Hi, I'm Kriemben!

In Strategy pattern, Program can change something's mode or behavior **in runtime**.

Strategy pattern is quite easy to use, so Let's check it right below!

## Example

OK guys, I'll show some example that is **Player**.

Firstly, I got a some video to play in example app. (you can use anything.)

Second, I wanna make **Playing only music, Playing only video without sounds, Playing sound and video** modes.

OK the base codes' are below.

```swift
protocol Playable {
  
  func preparePlay()
  func play()
  func stop()
}
```

```swift
class MusicPlayer: Playable {
  
  func preparePlay() {
    if let ready = ready {
      print("Ready to play!")
    }
  }
  
  func play() {
    
    print("Music is played.")
  }
  
  func stop() {
    
    print("Music is stopped.")
  }
}
```

```swift
class VideoPlayer: Playable {
  
  func preparePlay() {
    if let ready = ready {
      print("Ready to play!")
    }
  }
  
  func play() {
    
    print("Video is played.")
  }
  
  func stop() {
    
    print("Video is stopped.")
  }
}
```

```swift
class VideoWithoutSoundPlayer: Playable {
  
  func preparePlay() {
    if let ready = ready {
      print("Ready to play!")
    }
  }
  
  func play() {
    print("Video is played without sounds!")
  }
  
  func stop() {
    
    print("Video without sounds is stopped.")
  }
}
```

Can you understand these codes? Haha these are actually really easy code i think.

Next is main class that can initiate these classes

```swift
class Player {
  
  var player: Playable?
  
  init(with player: Playable) {
    
    self.player = player
  }
  
  func play() {
    
    player?.preparePlay()
    player?.play()
  }
  
  func stop() {
    
    player?.stop()
  }
}
```



```swift
class PlayerViewController: NSViewController {
  
  /// @Variables
  var player: Player?
  // and more...
  /// @END
  
  override func viewDidLoad() {
    super.viewDidLoad()
  }
  
  /// @IBOutlet
  @IBOutlet var playTime: NSTextView!
  @IBOutlet var selectModes: NSComboBox!
  /// @END
  
  /// @IBAction
  @IBAction func playButton(_ sender: NSButton) {
    
    let selectedIndex = selectModes.indexOfSelectedItem
    
    switch selectedIndex {
      case 0: // Play music
      	self.player = Player(with: MusicPlayer())
      case 1: // Play Video
      	self.player = Player(with: VideoPlayer())
      case 2: // Play only video without sounds
      	self.player = Player(with: VideoWithoutSoundPlayer())
    }
    
    self.player?.play()
  }
  
  @IBAction func stopButton(_ sender: NSButton) {
    
    if let player = self.player {
    
    	let selectedIndex = selectModes.indexOfSelectedItem
    
    	player.stop()
      
    } else { print("User tapped stop button without initializing player and moodes.") }
  }
  /// @END
}
```

OK. Isn't it **really simple and easy to use?** Haha 
