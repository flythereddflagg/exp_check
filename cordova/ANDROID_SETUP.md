# How to build android apps without android studio

## Initial setup

1. Go to the [Android IDE download page](https://developer.android.com/studio)

2. Scroll down to the heading: **Command line tools only**

3. Download the appropriate zip file for you system. I will be doing a windows download so interpolate for your system.

4. In the folder where you downloaded the zip file, open a PowerShell window and enter the following command: 
    ```powershell
    PS C:\Users\<USERNAME>\Downloads> Expand-Archive .\commandlinetools-<PLATFORM>-<VERSION_NUMBER>_latest.zip
    ```
    
5. Look inside the extracted folder. You will see a folder called `tools`. Copy this folder into a new folder path that you will create as follows: `C:\.android\cmdline-tools\`
   
6. In `C:\.android` make a folder called `avd`. This will hold your emulator data.

## Install Java

You do need some variant of the JDK and the JRE installed. Whether you use oracle JDK, adoptopenjdk, openjdk, or ojdkbuild does not matter. What does matter is that you use version 8 or else this will not work.

## Environment variables

You will need the following environment variables in your system:

| Variable           | Value                                |
| ------------------ | ------------------------------------ |
| `ANDROID_AVD_HOME` | `C:\.android\avd` or equivalent path |
| `ANDROID_SDK_ROOT` | `C:\.android` or equivalent path     |
| `JAVA_HOME`        | `<PATH TO YOUR JAVA 8 INSTALLATION>` |

Then you will need the following values added to your `PATH` variable:

| Path                                                     |
| -------------------------------------------------------- |
| `C:\.android\cmdline-tools\tools\bin` or equivalent path |
| `C:\.android\emulator` or equivalent path                |

Now would be a good time to restart your computer so that these changes take effect.

## Install the Android environment

You may reference the [SDK Manager](https://developer.android.com/studio/command-line/sdkmanager) (to install tools and stuff) and the [AVD Manager](https://developer.android.com/studio/command-line/avdmanager) (to install an android emulator) to learn how to install everything but **you must install *at least* the following to make the emulator work**:

- emulator
- platform-tools
- a platform (you may see platforms with `sdkmanager --list`)
- a system image (you may see system images with `sdkmanager --list`)

Reference the help pages on the the [AVD Manager](https://developer.android.com/studio/command-line/avdmanager) to make your emulator **before** starting it.

## Start the Emulator

You may now start the emulator using the info on [this page](https://developer.android.com/studio/run/emulator-commandline).

## My config

My config worked with the following options:

`sdkmanager.bat --list`

Path                                        | Version | Description                                | Location         
    -------                                     | ------- | -------                                    | -------          
    emulator                                    | 30.0.12 | Android Emulator                           | emulator\        
    patcher;v4                                  | 1       | SDK Patch Applier v4                       | patcher\v4\      
    platform-tools                              | 30.0.4  | Android SDK Platform-Tools                 | platform-tools\  
    platforms;android-29                        | 5       | Android SDK Platform 29                    | platforms\android-29\
    platforms;android-30                        | 3       | Android SDK Platform 30                    | platforms\android-30\
    system-images;android-29;google_apis;x86_64 | 10      | Google APIs Intel x86 Atom_64 System Image | system-images\android-29\google_apis\x86_64\
    system-images;android-30;google_apis;x86_64 | 7       | Google APIs Intel x86 Atom_64 System Image | system-images\android-30\google_apis\x86_64\

 

`avdmanager.bat create avd -n tester_1 -k "system-images;android-30;google_apis;x86_64" -d 23`

`emulator.exe -avd tester_1`