# Lab 2: Assembly

PLUG YOUR PI PICO INTO YOUR COMPUTER BEFORE YOU SOLDER IT JUST TO MAKE SURE IT WORKS :D

## Assembly

Download the `ibom.html` from the [release](https://github.com/dragonlock2/MMv3/releases) that matches your board revision and open it in your preferred browser. The interactive BOM (bill of materials) shows what parts are needed on your mouse's PCB (printed circuit board) and where they need to be placed.

To see images of all parts, see the Google Drive link [here](https://drive.google.com/drive/folders/1rGae82BSrE_mvmMwKTBHT9P-unDKIKQj?usp=sharing).

Also check the latest release for any manufacturing notes to make an older board functionally equivalent to the newest revision.

### Reflow Soldering

Let's start with the back of the PCB which is where the majority of parts are located. Click `B` in the top right to show just the back.

<p align="center">
    <img height="250px" src="imgs/ibom_back.png"/>
    <br>
    <a><b>iBOM Back</b></a>
</p>

Rather than solder each part by hand, we'll use reflow soldering which does it all at once. In reflow soldering, we place components on top of pads covered in solder paste before sending the whole thing through an oven to melt the solder, making permanent joints.

<p align="center">
    <img height="250px" src="https://www.omron.com/global/en/assets/img/technology/omrontechnics/vol51/015/img_01.jpg"/>
    <br>
    <a><b>Reflow Solder Process</b></a>
</p>

Let's start by applying the solder paste using a **solder stencil**. Instead of squeezing the perfect amount onto each pad by hand, we can do it all at once by spreading paste over a stencil with holes cut out precisely where we want paste. For a good solder paste application, it's important to make sure the stencil is flush against the PCB and stays aligned. The process is very forgiving, so don't worry if your paste looks messy or goes a bit outside the pads.

<p align="center">
    <img height="200px" src="imgs/stencil_align.jpg"/>
    <img height="200px" src="imgs/stencil_applied.jpg"/>
    <img height="200px" src="imgs/paste_applied.jpg"/>
    <br>
    <a><b>Solder Paste Application Process</b></a>
</p>

Now it's time for component placement. Following the `ibom.html`, place all of the components for the back side. None of the symmetric components have polarity, so don't worry about part orientation. Tweezers will be very useful, but don't squeeze too hard or your component will go flying. When placing components, press down gently so that it digs into the paste a bit to prevent it from moving. Again, the process is quite forgiving so don't worry if your parts aren't perfectly aligned as solder surface tension will generally pull them into alignment.

<p align="center">
    <img height="200px" src="imgs/place_cap.jpg"/>
    <img height="200px" src="imgs/place_res.jpg"/>
    <img height="200px" src="imgs/place_all.jpg"/>
    <br>
    <a><b>Component Placement</b></a>
</p>

Finally, let's reflow the solder! Throw your board into the reflow oven, load up the correct profile, and wait. With any luck, all of your joints will melt and the back side of your board will be done.

<p align="center">
    <img height="200px" src="imgs/reflow.jpg"/>
    <img height="200px" src="imgs/back_done.jpg"/>
    <br>
    <a><b>Reflow</b></a>
</p>

### Hand Soldering

The rest of the components need to be attached by hand. The general process is to heat up both the pad and the part before melting solder onto both of them. Adafruit has a great list of common issues and fixes which can be found [here](https://learn.adafruit.com/adafruit-guide-excellent-soldering/common-problems).  

<p align="center">
    <img height="250px" src="https://www.raypcb.com/wp-content/uploads/2021/09/SMT-Through-Hole-Soldering.jpg"/>
    <br>
    <a><b>How to Make a Solder Joint</b></a>
</p>

Let's start with the DRV8833 motor driver board. Solder the two 6-pin headers onto the board and bridge the `en` pads as shown in the following pictures. The technique that I find works best is to solder just one pin first with the part in any orientation. Then reheat that joint while pressing on the part to move it into perfect alignment. Finally, do the rest of the pins.

<p align="center">
    <img height="150px" src="imgs/DRV8833_4.jpg"/>
    <img height="150px" src="imgs/DRV8833_3.jpg"/>
    <img height="150px" src="imgs/DRV8833_2.jpg"/>
    <img height="150px" src="imgs/DRV8833_1.jpg"/>
    <br>
    <a><b>DRV8833 Motor Driver Assembly</b></a>
</p>

Next let's finish off the mouse's main PCB. Click `F` in the `ibom.html` to see the remaining components.

<p align="center">
    <img height="250px" src="imgs/ibom_front.png"/>
    <br>
    <a><b>iBOM Front</b></a>
</p>

To make alignment easier, starting with the shortest components usually works out best. The SMD components use the same soldering process except there's no hole to stick the part through. Some of the parts do have polarity, so if you're unsure make sure to ask your mentor.

<p align="center">
    <img height="200px" src="imgs/hand_1.jpg"/>
    <img height="200px" src="imgs/hand_2.jpg"/>
    <img height="200px" src="imgs/hand_3.jpg"/>
    <br>
    <a><b>Some THT Components</b></a>
</p>

For the IR LEDs, the silkscreen should denote the polarity. They also need to be mounted at a right angle so don't be afraid to bend them. Splaying the leads outward should hold them in place while you apply solder.

<p align="center">
    <img height="250px" src="imgs/ir_1.jpg"/>
    <img height="250px" src="imgs/ir_2.jpg"/>
    <br>
    <a><b>IR LEDs</b></a>
</p>

With any luck, your board should be finished!

<p align="center">
    <img height="250px" src="imgs/pcb_done.jpg"/>
    <br>
    <a><b>Assembled PCB</b></a>
</p>

### Mechanical Assembly

Let's finish assembling the mouse. Follow the pictures below. The screw threads are printed into the plastic so don't overtighten them. Don't be afraid to apply a bit of force when attaching the wheels since a tighter fit improves concentricity.

<p align="center">
    <img height="200px" src="imgs/mech_5.jpg"/>
    <img height="200px" src="imgs/mech_4.jpg"/>
    <img height="200px" src="imgs/mech_3.jpg"/>
    <img height="200px" src="imgs/mech_2.jpg"/>
    <img height="200px" src="imgs/mech_1.jpg"/>
    <br>
    <a><b>Final Assembly</b></a>
</p>

## Sanity Check

Now that your mouse is assembled, it is time to run a sanity check to make sure everything is working.

1. Follow the [setup](../README.md) instructions to get the firmware and libraries uploaded.
2. Follow the [sanity lab](sanity.md) to run the sanity check.

## IR Calibration

If you placed your mouse against a reflective surface, you may have noticed that the IR readings change. Since our sensors are currently mounted perpendicular to the mouse, they pick up some reflection from the surface the mouse sits on. To fix this, we're going to bend our IR sensors ever so slightly upwards to compensate.

Bring up the sanity check again to the IR sensor printout section. Bend your IR sensors upwards just enough so that the difference between pointing them into free space and placing them on a surface is less than 2,000.

<p align="center">
    <img height="250px" src="imgs/ir_calib.jpg"/>
    <br>
    <a><b>Bent IR Sensors</b></a>
</p>

### Checkoff #1

1. Show your mentor your assembled mouse, passing sanity check, and calibrated IR sensors.
