# Working with the camera from the command line

## Basic testing

To test the camera from the command line / Terminal, you'll use the utility [raspistill](https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspistill.md):

    raspistill -k

You should see the camera output. Type `Ctrl+C` to quit. Be careful not to click away from the terminal window, becuase it's being totally covered up by the preview.

In order to see the preview and the terminal, set the opacity of the preview to be semi-transparent:

    raspistill -k -op 200

## Capturing Images

To capture a file called `myImage.jpg`:

    raspistill -o myImage.jpg
    
## Recording video

To record video, use [raspivid](https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspivid.md) on the terminal. This will record a 5 second video called `myVideo.h264`:

    raspivid -o myVideo.h264 -t 5000

## Playing back video

To playback the raw H264 file, you can use `omxplayer`:

    omxplayer myVideo.h264

You'll notice the frame rate is off. To fix, install some software. You'll need to do this just once:

    sudo apt-get install -y gpac

And then use `MP4Box` to convert put the H264 file into the mp4 container format:

    MP4Box -add myVideo.h264 myVideo.mp4
