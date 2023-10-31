# three20

This is a custom tool I have built to help follow the 20-20-20 rule. This rule is meant to minimise eye strain when working for long periods on a computer. It states you should take a break from work every twenty minutes, and look at an object twenty feet away (roughly 6.1 meters) for twenty seconds.


## Details

This program is similar to [safe-eyes](https://github.com/slgobinath/SafeEyes) and other programs on github, though somewhat less aesthetically pleasing. However, it has some functionality that those lack, as far as I can tell.

Programs of this kind usually have an idle reset feature, triggered after a certain period of inactivity on the computer. This can happen when reading or watching a video, or if you are momentarily busy with something else. For safe-eyes, if I recall correctly, this period is one minute by default. As a consequence, if the feature is enabled, resets may sometimes happen even if you haven't looked away from the screen long enough.

This program also includes a reset feature, but it has mechanisms to mitigate this issue.
Firstly, resets are not automatic. When the user is inactive for more than two minutes, the timer is paused, and a dialog window appears, giving the user the option of resetting the timer. If the user doesn't reset the timer, and simply closes this window, the program resumes and the timer is unaffected; meaning the break prompt appears at the previously expected time. In particular, if the timer was scheduled to prompt for a break at the moment of closing, or before, the prompt will appear immediately after closing the dialog window.

Secondly, to avoid prompting for reset too often, the program defines a list of applications which, when holding the focus (their window is at the top of the system GUI), prevent it. These applications can be specified by process name, or by a phrase included in the window title. Note, however, that for some programs, the process name can't be determined and a window title must be used instead.

These phrases and process names can customised by modifying the settings.json file.

In addition, if you only want to prevent resets for a limited duration, the reset dialog includes a *stall* option. This option prevents resets from occurring until the next break.


## Dependencies
This was designed to work under Ubuntu 20.04. It requires xorg (It does not work with wayland).

It has the following dependencies:  
xdotool  
xmessage  
xprintidle  








